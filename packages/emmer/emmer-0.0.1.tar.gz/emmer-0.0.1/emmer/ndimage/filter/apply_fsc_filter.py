## Script to apply FSC filter to EMMAP based on either FSC curve or two halfmaps

def apply_fsc_filter(emmap, apix, fsc_curve=None, halfmap_1=None, halfmap_2=None):    
    '''
    Function to apply a FSC filter to a cryo EM map from either a FSC curve or two halfmaps.
    emmap : numpy.ndarray
        Cryo EM map
    apix : float
        Pixel size in Angstroms
    fsc_curve : numpy.ndarray
        FSC curve
    halfmap_1 : numpy.ndarray or path to halfmap 1
        First halfmap
    halfmap_2 : numpy.ndarray or path to halfmap 2
        Second halfmap

    '''
    from emmer.ndimage.sharpen.scaling_tools import compute_radial_profile_simple
    from emmer.ndimage.sharpen.set_radial_profile_to_volume import set_radial_profile_to_volume
    from emmer.ndimage.filter.filter_utils import get_fsc_filter

    
    if fsc_curve is not None:
        C_ref = 2*fsc_curve / (1+fsc_curve)
    elif halfmap_1 is not None and halfmap_2 is not None:
        C_ref = get_fsc_filter(halfmap_1, halfmap_2)
    
    
    rp_emmap = compute_radial_profile_simple(emmap, return_frequencies=False)
    fsc_filtered_rp = rp_emmap * C_ref
    
    filtered_emmap = set_radial_profile_to_volume(emmap, fsc_filtered_rp)

    return filtered_emmap