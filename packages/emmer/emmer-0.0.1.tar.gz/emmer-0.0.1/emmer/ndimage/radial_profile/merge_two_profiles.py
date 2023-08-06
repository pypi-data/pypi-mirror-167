## Script to merge two profiles

def merge_two_profiles(amplitudes_low_freq,amplitudes_high_freq,freq, smooth=1, d_cutoff=None, f_cutoff=None):
    '''
    Function to merge two profiles at a cutoff threshold based on differential weighting of two profiles

    Parameters
    ----------
    profile_1 : numpy.ndarray
        
    profile_2 : numpy.ndarray
        same size of profile_1
    freq : numpy.ndarray
        Frequencies corresponding to both profile_1 and profile_2
    d_cutoff : float
        Cutoff frequency defined in terms of distance (unit = A)
    f_cutoff : float
        Cutoff frequency given in terms of spatial frequency (unit = 1/A)
    smooth : float, optional
        smoothening parameter to control the transition region of two profiles

    Returns
    -------
    merged_profile : tuple of two numpy.ndarray
    

    '''
    import numpy as np
    if not (len(freq) == len(amplitudes_low_freq) and len(freq) == len(amplitudes_high_freq)):
        print("Size of two profiles not equivalent. Please check the dimensions and give another input")
        return None
    
    k = smooth
    d = 1 / freq
    
    if d_cutoff is not None:
        d_cutoff = d_cutoff
    
    elif f_cutoff is not None:
        d_cutoff = 1 / f_cutoff
    
    else:
        print("Please enter a cutoff frequency either in terms of spatial frequency (1/A) or distance (A)")
        return None
    
    weight_1 = 1 / (1 + np.exp(k * (d_cutoff - d)))
    weight_2 = 1 - weight_1
    
    merged_profile = weight_1 * amplitudes_low_freq + weight_2 * amplitudes_high_freq
    
    return merged_profile