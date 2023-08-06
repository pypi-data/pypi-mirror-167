## Script to generate different mask from an MRC file
import numpy as np
def get_atomic_model_mask(emmap, apix, pdb_path, dilation_radius=3, softening_parameter=5,  verbose=False):
    '''
    Function to generate a mask in the same grid as an emmap file based on atomic positions in a PDB file

    Parameters
    ----------
    emmap_path : str
        Path to a reference emmap for metadata
    pdb_path : str
        Path to a PDB/MMCIF file
  
    dilation_radius : float, optional
        The radius of the sphere (in Ang) to place at atomic positions determined by the PDB file. Default is 3A.

    Returns
    -------
    model_mask : str
    

    '''
    from emmer.ndimage.mask.mask_utils import get_atomic_point_map
    from emmer.ndimage.map_utils import dilate_mask
    from emmer.ndimage.filter.smoothen_mask import smoothen_mask
        
    map_shape = emmap.shape

    atomic_point_map = get_atomic_point_map(pdb_path, map_shape, apix)    
        
    dilation_radius_int = round(dilation_radius / apix)
    dilated_mask = dilate_mask(atomic_point_map, radius=dilation_radius_int)
    
    softened_mask = smoothen_mask(dilated_mask, softening_parameter)

    return softened_mask