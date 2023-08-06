## Script to calculate FSC curve for two maps

def calculate_fsc_curve(input_map_1, input_map_2):
    '''
    Wrapper to calculate FSC curve from the above functions

    Parameters
    ----------
    input_map_1 :  either numpy.ndarray or path to mrc file
        First halfmap
    input_map_2 : either numpy.ndarray or path to mrc file
        Second halfmap

    Returns
    -------
    fsc_curve : numpy.ndarray

    '''
    import numpy as np
    from emmer.ndimage.fsc.fsc_utils import calculate_fsc
    from emmer.ndimage.radial_profile.compute_radial_profile import compute_radial_profile
    from emmer.ndimage.map_utils import parse_input

    
    emmap_1 = parse_input(input_map_1)
    emmap_2 = parse_input(input_map_2)
    
    fft_1 = np.fft.rfftn(emmap_1)
    fft_2 = np.fft.rfftn(emmap_2)
    
    _, radii = compute_radial_profile(emmap_1, return_indices=True)
    
    map_shape = emmap_1.shape
    
    _, fsc, _ = calculate_fsc(fft_1, fft_2, radii, map_shape)
    fsc = np.array(fsc)
    return np.array(fsc)
