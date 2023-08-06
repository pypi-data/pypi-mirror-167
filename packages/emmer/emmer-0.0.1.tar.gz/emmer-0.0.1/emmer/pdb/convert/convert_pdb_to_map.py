# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 10:06:12 2021
"""

import numpy as np
import pypdb
import gemmi
from emmer.ndimage.sharpen.sharpen_maps import sharpen_maps
from emmer.ndimage.map_utils import convert_to_tuple
from emmer.pdb.pdb_utils import detect_pdb_input
from scipy.ndimage import center_of_mass
import warnings

def eval_size_apix_unitcell(pdb_structure, size, apix, unitcell, verbose):
    # out of (size, apix, unitcell) at least 2 parameters need to be given. If all three are given, the parameters must be in agreement. If only one of (size, apix) is given, the function will use whatever unitcell is in the gemmi structure
    
    # case 1: the user specifies (size, apix)
    if size is not None and apix is not None and unitcell is None:
        if verbose:
            print("Map size and pixelsize are given as inputs. Unitcell present in input structure will be ignored.")
        size_gemmi = size
        apix_gemmi = convert_to_tuple(apix, num_dims=3) # If apix is scalar, then the function returns a tuple of len 3
        # determine unknown
        unitcell_gemmi = gemmi.UnitCell(size[0]*apix_gemmi[0], size[1]*apix_gemmi[1], size[2]*apix_gemmi[2], 90, 90, 90)
        
    # case 2: the user specifies (size, unitcell)
    elif size is not None and apix is None and unitcell is not None:
        if verbose:
            print("Map size and unitcell are given as inputs. Unitcell present in input structure will be ignored.")
        unitcell_gemmi = unitcell
        size_gemmi = size
        # determine unknown
        apix_gemmi = (unitcell_gemmi.a/size_gemmi[0],unitcell_gemmi.b/size_gemmi[1],unitcell_gemmi.c/size_gemmi[2])
    
    # case 3: the user specifies (apix, unitcell)
    elif size is None and apix is not None and unitcell is not None:
        if verbose:
            print("Pixel size and unitcell are given as inputs. Unitcell present in input structure will be ignored.")
        unitcell_gemmi = unitcell
        apix_gemmi = convert_to_tuple(apix,num_dims=3)
        # determine unknown
        size_gemmi = [int(round(unitcell.a/apix_gemmi[0])), int(round(unitcell.b/apix_gemmi[1])), int(round(unitcell.c/apix_gemmi[2]))]
        
    # case 4: the user specifies only size
    elif size is not None and unitcell is None:  # in this case, program will use whatever unitcell is present in the gemmi structure
        if verbose:
            print("Map size is given as input. Unitcell present in the structure will be used")
        size_gemmi = size
        unitcell_gemmi = pdb_structure.cell
        # determine unknown
        apix_gemmi = (pdb_structure.cell.a/size_gemmi[0],pdb_structure.cell.b/size_gemmi[1],pdb_structure.cell.c/size_gemmi[2])
        
    # case 5: the user specifies only apix
    elif apix is not None and unitcell is None:
        if verbose:
            print("Pixel size is given as input. Unitcell present in the structure will be used")
        apix_gemmi = apix
        unitcell_gemmi = pdb_structure.cell
        # determine unknown
        size_gemmi = [int(round(unitcell_gemmi.a/apix_gemmi[0])), int(round(unitcell_gemmi.b/apix_gemmi[1])), int(round(unitcell_gemmi.c/apix_gemmi[2]))]

    # case 6: the used specifies (size, apix, unitcell). Raises warning if not in agreement and then proceeds to use the size and the apix
    elif size is not None and apix is not None and unitcell is not None:
        if verbose:
            print("Map size, pixel size and unitcell are given as inputs. Unitcell present in input structure will be ignored. Checking if parameters are self-consistent")
        size_gemmi = size
        apix_gemmi = convert_to_tuple(apix,num_dims=3)
        unitcell_gemmi = unitcell
        if int(round(unitcell_gemmi.a / apix_gemmi[0])) != size_gemmi[0] or int(round(unitcell_gemmi.b / apix_gemmi[1])) or int(round(unitcell_gemmi.c / apix_gemmi[2])):
            warnings.warn("size, pixel size and unitcell parameters are inconsistent. Proceeding with only size and pixel size")
            unitcell_gemmi = gemmi.UnitCell(size[0]*apix_gemmi[0], size[1]*apix_gemmi[1], size[2]*apix_gemmi[2], 90, 90, 90)
        
    return size_gemmi, apix_gemmi, unitcell_gemmi
        

def convert_pdb_to_map(input_pdb=None, unitcell=None, size=None, apix=None, return_grid=False, verbose=False, 
            mdlidx=0,align_output=True,set_refmac_blur=True,set_unblur=True, blur=0):
    '''
    Cleaner function to convert a gemmi_structure to EM map. Make sure the input structure, or the pdb in the 
    path you input are correct. Common check include: 
        a) center of mass of the gemmi structure should be roughly in the center of unitcell (important)
        b) Remove waters 
        c) Check if atomic bfactors make sense
    
    Note: if you use a single value for apix then the program will assume same voxelsize in all dimensions

    Parameters
    ----------
    input_pdb : str or gemmi.Structure, required
        Input can be either 
        a) string: either (i) pdb path, for ex: "path/to/pdb.pdb" or 
                          (ii)pdb_id "3j5p"
        b) gemmi.Structure()

    unitcell : gemmi.UnitCell, 
        
    size : tuple, 
        Expected map shape
    apix : float, optional
        Expected voxelsize
    Either two of the three (unitcell/size/apix) allowed. In case only size is given as input, unitcell is taken 
    from gemmi structure
    return_grid : bool, optional
        
    verbose : TYPE, optional
        The default is False.
    mdlidx : int
        If gemmi.Structure has multiple models this index tells which model to select. Default is zero
    align_output : bool
        If selected, this transforms to output to align according to mrcfile convenctions 
        Transformation: flip axis: 2 then rotate in plane (2,0) by angle 90
        

    Returns
    -------
    if return_grid is set True: emmap (numpy.ndarray), grid (gemmi.FloatGrid)
    
    Else, only emmap is returned

    '''
    pdb_structure = detect_pdb_input(input_pdb)
    size_gemmi, apix_gemmi, unitcell_gemmi = eval_size_apix_unitcell(pdb_structure, size, apix, unitcell, verbose)
    pdb_structure.cell = unitcell_gemmi
    
    reporter = {}
    reporter['pdb_struct_name'] =    pdb_structure.name
    reporter['unit_cell_exp'] =      pdb_structure.cell.parameters
    reporter['shape_exp'] = size_gemmi
    reporter['apix_exp'] = apix_gemmi
    reporter['com_pdb'] = np.array(pdb_structure[mdlidx].calculate_center_of_mass().tolist())
    if verbose:   # Make a check: 
        float_formatter = "{:.4f}".format
        np.set_printoptions(formatter={'float_kind':float_formatter})
        print("Simulating EM-map using: \t ", reporter['pdb_struct_name'], " \nwith the following properties: \n")
        print("Unit-cell (A*A*A): \t\t", reporter['unit_cell_exp'])
        print("Expected shape: \t\t", reporter['shape_exp'])
        print("Expected voxelsize (A*A*A): \t\t", reporter['apix_exp'])
        print("Center of mass: (A*A*A): \t\t",reporter['com_pdb'] )
    
    ## At this point, the values for size, pixelsize the unit cell are set 
    ## we should use the variable size_gemmi in density calculator

    if mdlidx > len(pdb_structure):  # Select model index from the pdb_structure
        print("selected model number not in pdb")
        return 0
    model = pdb_structure[mdlidx]
    dencalc = gemmi.DensityCalculatorE()
    dencalc.d_min = apix_gemmi[0] / 2
    dencalc.rate = 1
    if blur > 0:
        dencalc.blur=blur
    if set_refmac_blur:
        dencalc.set_refmac_compatible_blur(model)
        inv_d2 = dencalc.blur
        if verbose:
            print("Setting a blur of {:.2f}".format(dencalc.blur))
            
    dencalc.set_grid_cell_and_spacegroup(pdb_structure)
    try:
        dencalc.grid.set_size(*size_gemmi)
        dencalc.add_model_density_to_grid(model)
    except:
        dencalc.put_model_density_on_grid(model)
        print("WARNING: You are using an older version of gemmi. " +
              "The map size of the pdb generated map might not be as expected")
        print("--> Please update your gemmi package to the newest version")

    emmap = np.array(dencalc.grid,copy=False)
    
    if set_refmac_blur:
        if verbose: 
            print("Applying a unblur for the sampled density equal to: {:.2f}".format(-inv_d2))
        emmap = sharpen_maps(emmap, apix=apix_gemmi[0], sharpening_bfactor=-inv_d2)
        
    
    if align_output:
        from scipy.ndimage import rotate
        emmap_flipped = np.flip(emmap,axis=2)
        emmap_rotated = rotate(emmap_flipped, angle=90, axes=(2,0))
        emmap = emmap_rotated
    
    reporter['shape_final'] = emmap.shape
    reporter['apix_final'] = np.array(dencalc.grid.spacing)
    reporter['com_map'] = np.array(center_of_mass(abs(emmap)))*reporter['apix_final']
    if verbose: ## Check output if it matches expectation
        print("\nMap simulated! Final parameters:")
        print("Emmap shape \t\t",reporter['shape_final'])
        print("Grid spacing (A*A*A): \t\t", reporter['apix_final'])
        print("Center of mass of Emmap: (A*A*A)\t", reporter['com_map'])
    
    if return_grid:
        return emmap, dencalc.grid
    
    else:
        return emmap
    