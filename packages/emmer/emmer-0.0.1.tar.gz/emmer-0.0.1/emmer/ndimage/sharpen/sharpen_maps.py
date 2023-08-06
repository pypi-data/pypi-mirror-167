## Script to perform map sharpening using B factors

def sharpen_maps(emmap, apix, sharpening_bfactor):
    '''
    Function to apply a global sharpening factor to EM density maps 

    Parameters
    ----------
    emmap : numpy.ndarray (dims=3)
        Input map
    apix : Float
        Pixelsize (one dimension only)
    sharpening_bfactor : float
        Global sharpening factor (negative if you want to sharpen, positive if you want to blur)

    Returns
    -------
    sharpened_map : numpy.ndarray (dims=3)

    '''
    import numpy as np
    from emmer.ndimage.radial_profile.frequency_array import frequency_array
    from emmer.ndimage.sharpen.set_radial_profile_to_volume import set_radial_profile_to_volume
    from emmer.ndimage.sharpen.scaling_tools import compute_radial_profile_simple
        
    emmap_profile = compute_radial_profile_simple(emmap)
    freq = frequency_array(amplitudes=emmap_profile, apix=apix)
    
    sharpened_profile = emmap_profile * np.exp(-1*sharpening_bfactor/4 * freq**2)

    sharpened_map = set_radial_profile_to_volume(emmap, sharpened_profile)
    
    return sharpened_map