## Script to compute a shaken PDB structure within a molecular boundary


def perturb_within_mask(pdb_path, mask_path, rmsd_magnitude,mask_threshold=0.5, verbose=False):
    '''
    Function to perturb a PDB structure within a molecular boundary
    
    Parameters
    ----------
    pdb_path : str
        Path to a PDB/MMCIF file
    mask_path : str
        Path to a MRC file
    rmsd_magnitude : float
        The magnitude of the RMSD to apply to the PDB structure
    mask_threshold : float, optional
        The threshold for the mask. The default is 0.5.
    verbose : bool, optional
        Verbose. The default is False.
    
    Returns
    -------
    shaken_pdb_path : str
        Path to the shaken PDB structure
    '''
    from emmer.pdb.pdb_tools.shake_pdb_within_mask import shake_pdb_within_mask

    shaken_pdb_path = shake_pdb_within_mask(pdb_path, mask_path, rmsd_magnitude, mask_threshold=mask_threshold, verbose=verbose)
    return shaken_pdb_path