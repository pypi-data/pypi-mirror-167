#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:23:14 2021

@author: alok
"""

import numpy as np
  
def get_index_at_resolution(freq, resolution):
    probe_freq = 1/resolution
    index_at_resolution = np.argmin(abs(freq-probe_freq))
    return index_at_resolution

def crop_profile_between_resolution(freq, amplitude, low_resolution, high_resolution):
    ## Check if inverse of minimum resolution and inverse of maximum resolution are within freq range
    if 1/low_resolution < freq[0] or 1/high_resolution > freq[-1]:
        raise UserWarning("Minimum resolution or maximum resolution is out of range")
    
    low_frequency_index = get_index_at_resolution(freq, low_resolution)
    high_frequency_index = get_index_at_resolution(freq, high_resolution)

        
    crop_freq = freq[low_frequency_index:high_frequency_index]
    crop_amplitude = amplitude[low_frequency_index:high_frequency_index]
    
    return crop_freq, crop_amplitude
       
def resample_1d(x_old,y_old,num,xlims=None):
    '''
    Sample an given x-y data in a new grid 

    Parameters
    ----------
    x_old : numpy.ndarray
        data in x axis (same dim as y_old)
    y_old : numpy.ndarray
        data in y axis (same dim as x_old)
    num : int
        new number of data points

    Returns
    -------
    x_new : numpy.ndarray
        resampled x axis
    y_new : numpy.ndarray
        resampled y axis

    '''
    from scipy.interpolate import interp1d
    
    f = interp1d(x_old, y_old,kind='slinear',fill_value='extrapolate')
    if xlims is None:
        x_new = np.linspace(x_old[0], x_old[-1], num=num)
    else:
        xmin = xlims[0]
        xmax = xlims[1]
        x_new = np.linspace(xmin, xmax,num=num)
        
    y_new = f(x_new)
    #y_new[y_new>1]=1
    return x_new, y_new
  


def measure_wilson_deviation(freq, amplitudes, wilson_cutoff, fsc_cutoff, wilson_range=None, return_exponential_fit=False):
    '''
    Function to measure the deviations in wilson region from an exponential behaviour
    '''
    import numpy as np
    ## import estimate_bfactor_standard
    from emmer.ndimage.radial_profile.estimate_bfactor_standard import estimate_bfactor_standard
    if wilson_range is None:
        wilson_range_start = wilson_cutoff
        wilson_range_end = fsc_cutoff
    else:
        low_freq_cutoff_wilson = wilson_range.max()
        high_freq_cutoff_wilson = wilson_range.min()
        assert low_freq_cutoff_wilson > wilson_cutoff and low_freq_cutoff_wilson < 1/freq[0]
        assert high_freq_cutoff_wilson < fsc_cutoff and high_freq_cutoff_wilson < 1/freq[-1]
        
        wilson_range_start = low_freq_cutoff_wilson
        wilson_range_end = high_freq_cutoff_wilson
        
    bfactor, amp = estimate_bfactor_standard(freq, amplitudes, wilson_cutoff=wilson_cutoff, fsc_cutoff=fsc_cutoff, 
                                             return_amplitude=True)
    
    exponential_fit = amp * np.exp(bfactor * 0.25 * freq**2)
    
    deviations = amplitudes - exponential_fit
    
    deviation_start_index = get_index_at_resolution(freq,wilson_range_start)
    deviation_end_index = get_index_at_resolution(freq,wilson_range_end)
    
    deviations[:deviation_start_index] = 0
    deviations[deviation_end_index:] = 0
    
    if return_exponential_fit:
        return deviations, exponential_fit
    else:
        return deviations
    
def get_average_profile(profile_list, return_variance=False):
    profile_list = np.array(profile_list)
    average_profile = np.einsum("ij->j", profile_list) / len(profile_list)
    
    variation = []
    for col_index in range(profile_list.shape[1]):
        col_extract = profile_list[:,col_index]
        variation.append(col_extract.std())

    variation = np.array(variation)
    
    if return_variance:
        return average_profile, variation
    else:
        return average_profile

