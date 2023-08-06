## Script to compute B factor from a radial profile

def estimate_bfactor_standard(freq, amplitude, wilson_cutoff, fsc_cutoff, return_amplitude=False, return_fit_quality=False, standard_notation=False):
    '''
    From a given radial profile, estimate the b_factor from the high frequency cutoff

    Parameters
    ----------
    freq : numpy.ndarray
        Frequency array
    amplitude : numpy.ndarray
        Amplitudes
    wilson_cutoff : float
        Frequency from which wilson statistics are valid. Units: Angstorm
    fsc_cutoff : float
        FSC resolution calculated at 0.143 (for halfmaps). Units: Angstorm
        

    Returns
    -------
    b_factor : float
        The estimated b factor
    
    amp : float
        The estimated amplitude of the exponential fit

    '''
    from scipy.optimize import curve_fit
    from sklearn.metrics import r2_score
    from emmer.ndimage.radial_profile.profile_tools import crop_profile_between_resolution
    import numpy as np
    def linear_fit(xdata,slope,const):
        ydata = const + slope*xdata
        return ydata
    
    cropped_freq, cropped_amplitude = crop_profile_between_resolution(freq, amplitude, wilson_cutoff, fsc_cutoff)
    
    xdata = cropped_freq**2
    ydata = np.log(cropped_amplitude)
        
    param, _ = curve_fit(linear_fit,xdata,ydata)
    
    if standard_notation:
        b_factor = -1 * param[0] * 4   ## Inverse of slope
    else:
        b_factor = param[0] * 4
    
    exp_fit_amplitude = np.exp(param[1])
    
    
    y_pred = linear_fit(xdata, slope=param[0], const=param[1])
    r2 = r2_score(y_true=ydata, y_pred=y_pred)
    
    if return_amplitude:
        if return_fit_quality:
            return b_factor,exp_fit_amplitude, r2
        else:
            return b_factor,exp_fit_amplitude
    else:
        if return_fit_quality:
            return b_factor, r2
        else:
            return b_factor