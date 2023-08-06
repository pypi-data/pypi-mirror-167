## Script to extract map intensities around atoms between a given residue range

def trim_map_between_residues(emmap_path, pdb_path, chain_name, residue_range=None, dilation_radius=3, verbose=False):
    '''
    Function to extract map intensities around atoms between a given residue range

    Parameters
    ----------
    emmap_path : str
        Path to a map file 
    pdb_path : str
        Path to a PDB/MMCIF file
    chain_name : str
        Chain name
    residue_range : list, optional
        To extract all atoms between residue id
        residue_range=[start_res_id, end_res_id] (both incl). The default is [0,-1], which returns all residues present in a chain. 
    dilation_radius : float, optional
        The radius of the sphere (in Ang) to place at atomic positions determined by the PDB file. Default is 3A.

    Returns
    -------
    trimmed_map : numpy.ndarray
    

    '''
    import numpy as np
    from emmer.pdb.pdb_utils import detect_pdb_input
    from emmer.pdb.pdb_utils import get_atomic_positions_between_residues
    from emmer.pdb.convert.convert_pdb_to_mrc_position import convert_pdb_to_mrc_position
    from emmer.ndimage.map_utils import dilate_mask, load_map
    
    emmap, apix = load_map(emmap_path)
        
    map_shape = emmap.shape
    
    mask = np.zeros(map_shape)
    
    gemmi_st = detect_pdb_input(pdb_path)
    
    pdb_positions = get_atomic_positions_between_residues(gemmi_st, chain_name, residue_range)
    
    if verbose:
        print("Found {} atom sites".format(len(pdb_positions)))
    
    mrc_position = convert_pdb_to_mrc_position(pdb_positions, apix)
    zz,yy,xx = zip(*mrc_position)
    mask[zz,yy,xx] = 1
    
    #dilation_radius = 3 #A
    dilation_radius_int = round(dilation_radius / apix)
    dilated_mask = dilate_mask(mask, radius=dilation_radius_int)
    
    trimmed_map = emmap * dilated_mask
    
    return trimmed_map
