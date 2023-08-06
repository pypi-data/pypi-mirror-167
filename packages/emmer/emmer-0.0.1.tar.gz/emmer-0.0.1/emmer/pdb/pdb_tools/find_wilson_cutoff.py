#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:11:29 2020

@author: Alok, Arjen, Maarten, Stefan, Reinier 
"""

# pdb_tools contains several useful fucntions for common manipulations with
# pdb structures, making use of the gemmi package. functions are classified 
# into pdb_tools when they can be considered an application on their own
# but do not have so many distinct features that they warrent their own script.

# global imports
import mrcfile
import gemmi
import numpy as np

#%% functions

def find_wilson_cutoff(input_pdb=None, mask_path=None, mask = None, apix=None, method='Singer', return_as_frequency=False, verbose=False):
    '''
    Function to find the cutoff frequency above which Wilson statistics hold true. If a PDB file is passed either as a gemmi structure as a PDB path, then radius of gyration is found rigorously by the mean distance to center of mass of protein. If a mask is passed, however, then radius of gyration is estimated from the num_atoms calculated from the mask volume. 
    
Reference: 
    1) Estimating Radius of gyration from num_atoms John J. Tanner,  2016 (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5053138/)
    
    2) Estimating cutoff frequency: Amit Singer, 2021 (https://www.biorxiv.org/content/10.1101/2021.05.14.444177v1.full)
    
    3) Estimating cutoff frequency: Guiner method - Rosenthal & Henderson, 2003 (https://doi.org/10.1016/j.jmb.2003.07.013)

    Parameters
    ----------
    model_path : string, optional
        path to pdb file. The default is None.
    input_gemmi_st : gemmi.Structure(), optional
        
    mask_path : string, optional
        path to mask. The default is None.
    method : string, optional
        Method used to find the cutoff frequency. Two accepted values are: 'Singer', and 'Rosenthal_Henderson' (case insensitive). The default is 'Singer'.
    return_as_frequency : TYPE, optional
        DESCRIPTION. The default is False.

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    
    from emmer.ndimage.map_utils import load_map
    from emmer.ndimage.map_tools import measure_mask_parameters
    from emmer.pdb.pdb_utils import find_radius_of_gyration, detect_pdb_input
    
    if input_pdb is not None:
        gemmi_st = detect_pdb_input(input_pdb)
        num_atoms = gemmi_st[0].count_atom_sites()
        Rg = find_radius_of_gyration(input_pdb=gemmi_st)

    else:
        if mask_path is not None:
            mask, apix = load_map(mask_path)
        
        assert mask
        assert apix
    
        mask_vol_A3, protein_mass, num_atoms, mask_dims,maskshape = measure_mask_parameters(mask=mask, apix=apix, detailed_report=True)

        R_constant = 2 #A
        v = 0.4 # Exponent derived empirically Ref. 1 for monomers and oligomers
        Rg = R_constant * num_atoms**v
  
    if verbose:
        print("Number of atoms: {} \nRadius of Gyration: {:.2f}".format(num_atoms,Rg))
    if method.lower() == 'rosenthal_henderson':
        d_cutoff = 2*np.pi*Rg
        f_cutoff = 1/d_cutoff
    elif method.lower() == 'singer':
        ko = num_atoms**(-1/12) # Guiner transition non-dimensional
        
        Ro = Rg * np.cbrt(1/num_atoms) # Unit cell dimension around each atom
        
        f_cutoff = ko/Ro
        d_cutoff = 1/f_cutoff
    else:
        raise UserWarning("Enter rosenthal_henderson or singer as method")
    
    if verbose:
        print("Frequency cutoff: {:.2f} (in 1/A) \n".format(f_cutoff))
        print("Frequency cutoff: {:.2f} (in A) \n ".format(d_cutoff))
    
    if return_as_frequency:
        return f_cutoff
    else:
        return d_cutoff
