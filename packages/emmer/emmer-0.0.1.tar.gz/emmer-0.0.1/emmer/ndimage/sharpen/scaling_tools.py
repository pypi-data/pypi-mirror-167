#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 14:56:33 2022

@author: alok
"""
import mrcfile
import numpy as np

def compute_radial_profile_proper(vol, frequency_map):

    vol_fft = np.fft.rfftn(vol, norm="ortho");
    dim = vol_fft.shape;
    ps = np.real(np.abs(vol_fft));
    frequencies = np.fft.rfftfreq(dim[0])[1:];
    #bins = np.digitize(frequency_map, frequencies);
    #bins = bins - 1;
    x, y, z = np.indices(ps.shape)
    radii = np.sqrt(x**2 + y**2 + z**2)
    radii = radii.astype(int)
    radial_profile = np.bincount(radii.ravel(), ps.ravel()) / np.bincount(radii.ravel())
    radial_profile = radial_profile[1:int(ps.shape[0]/2)+1]

    return radial_profile, frequencies;

def compute_radial_profile_simple(vol, return_frequencies=False):
    from emmer.include.confidenceMapUtil import FDRutil
    frequency_map = FDRutil.calculate_frequency_map(np.zeros(vol.shape))
    
    em_profile, frequencies_map = compute_radial_profile_proper(vol, frequency_map)
    
    if return_frequencies:
        return em_profile, frequencies_map
    else:
        return em_profile
    
def set_radial_profile_proper(vol, scale_factors, frequencies, frequency_map, shape):
    vol_fft = np.fft.rfftn(np.copy(vol), norm='ortho');
    scaling_map = np.interp(frequency_map, frequencies, scale_factors);
    scaled_map_fft = scaling_map * vol_fft;
    scaled_map = np.real(np.fft.irfftn(scaled_map_fft, shape, norm='ortho'));

    return scaled_map, scaled_map_fft;


def set_radial_profile_simple(vol, scale_factors, frequencies):
    from emmer.include.confidenceMapUtil import FDRutil
    frequency_map = FDRutil.calculate_frequency_map(np.zeros(vol.shape))
    
    map_shape = vol.shape
    map_b_sharpened, _ = set_radial_profile_proper(vol, scale_factors, frequencies, frequency_map, map_shape);
    
    return map_b_sharpened



def compute_scale_factors(em_profile, ref_profile):
    scale_factor = np.sqrt(ref_profile**2/em_profile**2)
    return scale_factor



