## Script to compute the center of mass of a given input emmap.

def get_center_of_mass(emmap, apix, background_threshold=None):
    '''
    Computes the center of mass of a given input emmap. 
    Note: converts the negative intensities to positive to calculate COM

    Parameters
    ----------
    emmap : numpy.ndarray
        
    apix : float or any iterable
        Voxelsize

    Returns
    -------
    com_real : numpy.ndarray
        units: (A * A * A)

    '''
    from scipy.ndimage import center_of_mass
    from emmer.pdb.convert.convert_mrc_to_pdb_position import convert_mrc_to_pdb_position

    if background_threshold is not None:
        emmap[emmap < background_threshold] = 0
    
    COM_mrc_position = list(center_of_mass(abs(emmap)))
    COM_pdb_position = convert_mrc_to_pdb_position([COM_mrc_position], apix)[0]
    
    
    return COM_pdb_position
    