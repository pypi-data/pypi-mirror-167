## Script to apply a radial profile to a given EM density map

def set_radial_profile_to_volume(emmap, ref_profile):
    '''
    emmap : numpy.ndarray (dims=3)
        Input map
    ref_profile : numpy.ndarray (dims=1)
        Reference profile
    
    Returns
    -------
    scaled_map : numpy.ndarray (dims=3)
    
        '''
    from emmer.ndimage.sharpen.scaling_tools import compute_radial_profile_simple, compute_scale_factors, set_radial_profile_simple
    em_profile,frequencies = compute_radial_profile_simple(emmap, return_frequencies=True)
    scale_factors = compute_scale_factors(em_profile, ref_profile)
    scaled_map = set_radial_profile_simple(emmap, scale_factors, frequencies)
    
    return scaled_map