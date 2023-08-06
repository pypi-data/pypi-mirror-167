## Script to scale a target profile to match B factor of a reference profile

def scale_profiles(reference_profile_tuple, target_profile_tuple, wilson_cutoff, fsc_cutoff, return_bfactor_properties=False):
    '''
    Function to scale an input theoretical profile to a reference profile

    Parameters
    ----------
    reference_profile_tuple : tuple
        (freq_reference, amplitude_reference)
    target_profile_tuple : tuple
        (freq_theoretical, amplitude_theoretical)
    just_use_exponential : bool, optional
        Returns just an exponential fit and not a scaled profile
    using_reference_profile : TYPE, optional
        DESCRIPTION. The default is False.
    start_freq : TYPE, optional
        DESCRIPTION. The default is 0.3.

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    import numpy as np
    from emmer.ndimage.radial_profile.estimate_bfactor_standard import estimate_bfactor_standard
    
    freq = reference_profile_tuple[0]
    reference_amplitude = reference_profile_tuple[1]
    
    freq_scale = target_profile_tuple[0]
    scale_amplitude = target_profile_tuple[1]
 
    bfactor_reference, fit_amp_reference, quality_of_fit = estimate_bfactor_standard(freq, reference_amplitude, wilson_cutoff=wilson_cutoff, fsc_cutoff=fsc_cutoff, return_amplitude=True,return_fit_quality=True)
    bfactor_scale, fit_amp_scale = estimate_bfactor_standard(freq_scale, scale_amplitude, wilson_cutoff=wilson_cutoff, fsc_cutoff=fsc_cutoff, return_amplitude=True)
    
    bfactor_diff = bfactor_reference-bfactor_scale
    
    amp_scaling_factor = fit_amp_reference / fit_amp_scale
        
    amplitude_scaled = amp_scaling_factor * scale_amplitude * np.exp(bfactor_diff * freq**2 / 4)
    
    
    if return_bfactor_properties:
        return (freq,amplitude_scaled), (bfactor_reference, fit_amp_reference, quality_of_fit)
    else:
        return (freq, amplitude_scaled)