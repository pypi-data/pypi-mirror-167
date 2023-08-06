## Script to return the threshold that gives the closest volume to a reference volume

def volume_matching_threshold(emmap, apix, reference_volume, num_bins=100, min_threshold=None, max_threshold=None):
    import numpy as np
    
    if min_threshold is None:
        min_threshold = 0
    
    if max_threshold is None:
        max_threshold = 0.97 * emmap.max()
        
    threshold_bins = np.linspace(min_threshold, max_threshold, num=num_bins)
    volumes = []
    for threshold in threshold_bins:
        binarised_map = (emmap>=threshold).astype(np.int_)
        sum_of_voxels = binarised_map.sum()
        volume_real_units = sum_of_voxels * apix**3
        volumes.append(volume_real_units)
    
    volumes = np.array(volumes)
    index_min_delta = np.argmin(abs(volumes-reference_volume))
    matching_threshold = threshold_bins[index_min_delta]
    
    return matching_threshold
