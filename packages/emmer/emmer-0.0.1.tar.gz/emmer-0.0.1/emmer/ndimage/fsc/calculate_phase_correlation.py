## Script to calculate phase correlation curve

def calculate_phase_correlation_maps(input_map_1, input_map_2):
    '''
    Wrapper to calculate FSC curve from the above functions

    Parameters
    ----------
    input_map_1 : either numpy.ndarray or path to mrc file
        First halfmap
    input_map_2 : either numpy.ndarray or path to mrc file
        Second halfmap

    Returns
    -------
    fsc_curve : numpy.ndarray

    '''
    import numpy as np
    from emmer.ndimage.fsc.fsc_utils import calculate_phase_correlation
    from emmer.ndimage.radial_profile.compute_radial_profile import compute_radial_profile
    from emmer.ndimage.map_utils import parse_input
    
    emmap_1 = parse_input(input_map_1)
    emmap_2 = parse_input(input_map_2)
    
    fft_1 = np.fft.rfftn(emmap_1)
    fft_2 = np.fft.rfftn(emmap_2)
    
    _, radii = compute_radial_profile(emmap_1, return_indices=True)
    
    map_shape = emmap_1.shape
    
    _, phase_correlation, _ = calculate_phase_correlation(fft_1, fft_2, radii, map_shape)
    phase_correlation = np.array(phase_correlation)
    return np.array(phase_correlation)
