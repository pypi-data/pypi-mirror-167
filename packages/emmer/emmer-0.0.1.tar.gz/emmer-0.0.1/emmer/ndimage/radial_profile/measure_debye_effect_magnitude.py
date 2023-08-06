## Script to measure the debye effect magnitude from a radial profile

def measure_debye_effect_magnitude(freq, amplitudes, wilson_cutoff, fsc_cutoff, wilson_range=None, return_exponential_fit=False):
    '''
    Function to measure the debye effect magnitude from a radial profile
    freq : array
        Frequency axis
    amplitudes : array
        Amplitude axis
    wilson_cutoff : float   
        Wilson cutoff
    fsc_cutoff : float
        FSC cutoff
    wilson_range : array
        Range of frequencies to use for the wilson region
    return_exponential_fit : bool
        If true, return the exponential fit
    
    '''
    from emmer.ndimage.radial_profile.profile_tools import measure_wilson_deviation
    wilson_deviations = measure_wilson_deviation(freq, amplitudes, wilson_cutoff, fsc_cutoff, wilson_range, return_exponential_fit)
    absolute_deviations = abs(wilson_deviations)
    return absolute_deviations.sum()
    