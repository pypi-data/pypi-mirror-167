## Script to estimate global bfactor of a cryo EM map using the radial profile

def estimate_bfactor_map(emmap_path, wilson_cutoff, fsc_cutoff, return_fit=False):
    '''
    Script to estimate the global bfactor of a cryo EM density map using the radial profile.
    emmap_path: path to the cryo EM density map
    wilson_cutoff: the Wilson score cutoff for the global bfactor estimation
    fsc_cutoff: the FSC cutoff for the global bfactor estimation
    return_fit: whether to return the fit quality of the bfactor (True)
    returns:
    bfactor: the estimated bfactor (float)
    '''
    from emmer.ndimage.map_utils import load_map
    from emmer.ndimage.radial_profile.frequency_array import frequency_array 
    from emmer.ndimage.radial_profile.compute_radial_profile import compute_radial_profile
    from emmer.ndimage.radial_profile.estimate_bfactor_pwlf import estimate_bfactor_pwlf
    
    emmap, apix = load_map(emmap_path)

    rp_unsharp = compute_radial_profile(emmap)
    freq = frequency_array(amplitudes=rp_unsharp, apix=apix)
        
    bfactor,_,(fit,z,slopes) = estimate_bfactor_pwlf(freq,rp_unsharp, 
                                                             wilson_cutoff=wilson_cutoff, 
                                                             fsc_cutoff=fsc_cutoff)
    
    if return_fit:
        return bfactor, fit
    else:
        return bfactor