## Script to estimate the local bfactor of a cryo EM density map at a given point in the map

def estimate_local_bfactor(emmap_path, center, wilson_cutoff, fsc_cutoff, boxsize=None, standard_notation=True, return_fit_quality=False):
    '''
    Script to estimate the local bfactor of a cryo EM density map at a given point in the map.
    emmap_path: path to the cryo EM density map
    center: the center of the local bfactor estimation
    wilson_cutoff: the Wilson score cutoff for the local bfactor estimation
    fsc_cutoff: the FSC cutoff for the local bfactor estimation
    boxsize: the size of the box to extract around the point in the map
    standard_notation: whether to use the standard notation for the bfactor (True)
    return_fit_quality: whether to return the fit quality of the bfactor (True)

    returns:
    bfactor: the estimated bfactor (float)
    '''

    from emmer.ndimage.radial_profile.estimate_bfactor_standard import estimate_bfactor_standard
    from emmer.ndimage.radial_profile.compute_radial_profile import compute_radial_profile
    from emmer.ndimage.radial_profile.frequency_array import frequency_array
    from emmer.ndimage.map_utils import extract_window, load_map
    from emmer.include.emmer_utils import round_up_to_even

    emmap, apix = load_map(emmap_path)
       
    if boxsize is None:
        boxsize = round_up_to_even(25 / apix)
    else:
        boxsize = round_up_to_even(boxsize)

    emmap_window = extract_window(emmap, center, boxsize)
            
    rp_local = compute_radial_profile(emmap_window)
    freq = frequency_array(rp_local, apix)
            
    bfactor,qfit = estimate_bfactor_standard(freq, rp_local, wilson_cutoff, fsc_cutoff, standard_notation=standard_notation, return_fit_quality=True)
    
    if return_fit_quality:
        return bfactor, qfit
    else:
        return bfactor