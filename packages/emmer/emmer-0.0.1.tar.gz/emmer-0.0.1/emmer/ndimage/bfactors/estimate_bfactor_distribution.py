
import numpy as np

def estimate_bfactor_distribution(emmap_path, binarised_mask, wilson_cutoff, fsc_cutoff, boxsize=None, num_centers=1000, standard_notation=True):
    '''
    Script to estimate the local bfactor distribution of a cryo EM density map by random sampling of points in the map.

    emmap_path: path to the cryo EM density map
    binarised_mask: a binary mask of the same size as the cryo EM density map
    wilson_cutoff: the Wilson score cutoff for the local bfactor estimation
    fsc_cutoff: the FSC cutoff for the local bfactor estimation
    boxsize: the size of the box to extract around each point in the map
    num_centers: the number of points to extract from the map
    standard_notation: whether to use the standard notation for the bfactor (True) 

    returns:
    bfactors: the estimated bfactors (numpy array)
    
    '''

    from emmer.ndimage.radial_profile.estimate_bfactor_standard import estimate_bfactor_standard
    from emmer.ndimage.radial_profile.compute_radial_profile import compute_radial_profile
    from emmer.ndimage.radial_profile.frequency_array import frequency_array
    from emmer.ndimage.map_utils import  get_all_voxels_inside_mask, extract_window, load_map
    from emmer.include.emmer_utils import round_up_to_even
    import random
    from tqdm import tqdm
    
    emmap, apix = load_map(emmap_path)   
    
    if boxsize is None:
        boxsize = round_up_to_even(25 / apix)
    else:
        boxsize = round_up_to_even(boxsize)
        
    all_points = get_all_voxels_inside_mask(binarised_mask)
    random_centers = random.sample(all_points,num_centers)
    
    bfactor_distributions = {}
    
    for center in tqdm(random_centers, desc="Analysing local bfactors distribution"):
        try:            
            emmap_window = extract_window(emmap, center, boxsize)
            rp_local = compute_radial_profile(emmap_window)
            freq = frequency_array(rp_local, apix)                        
            bfactor,qfit = estimate_bfactor_standard(freq, rp_local, wilson_cutoff, fsc_cutoff, standard_notation=standard_notation, return_fit_quality=True)
            bfactor_distributions[tuple(center)] = tuple([bfactor, qfit])
        except Exception as e:
            print("Error at {}".format(center))
            print(e)
            raise
    
    return bfactor_distributions

