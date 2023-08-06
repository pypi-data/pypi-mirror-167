## Script to compute bfactor from radial profile using PWLF 

def estimate_bfactor_pwlf(freq,amplitudes,wilson_cutoff,fsc_cutoff, return_all=True, num_segments=3):
    '''
    Function to automatically find out linear region in a given radial profile 


    @Manual{pwlf,
            author = {Jekel, Charles F. and Venter,     Gerhard},
            title = {{pwlf:} A Python Library for Fitting 1D Continuous Piecewise Linear Functions},
            year = {2019},
            url = {https://github.com/cjekel/piecewise_linear_fit_py}
}

    Parameters
    ----------
    freq : numpy.ndarray
        
    amplitudes : numpy.ndarray
        

    Returns
    -------
    start_freq_in_angstorm, estimated_bfactor

    '''
    import numpy as np
    import pwlf
    from emmer.ndimage.radial_profile.profile_tools import crop_profile_between_resolution
    cropped_freq, cropped_amplitude = crop_profile_between_resolution(freq, amplitudes, wilson_cutoff, fsc_cutoff)
    
    x_data = cropped_freq**2
    y_data = np.log(cropped_amplitude)
    
    piecewise_linfit = pwlf.PiecewiseLinFit(x_data, y_data)
    z = piecewise_linfit.fit(n_segments=num_segments)
    
    slopes = piecewise_linfit.calc_slopes()
    
    bfactor = slopes[-1] * 4
    
    amplitude_zero_freq = piecewise_linfit.predict(0)
    
    if return_all:
        return bfactor, amplitude_zero_freq, (piecewise_linfit, z, slopes)
    else:
        return bfactor