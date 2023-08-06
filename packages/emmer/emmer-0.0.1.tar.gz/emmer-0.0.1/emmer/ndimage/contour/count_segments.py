## Script to count the number of segments in a map at a given threshold

def count_segments(emmap, reference_threshold):
    from skimage import measure
    import numpy as np

    binarised_emmap = (emmap>reference_threshold).astype(np.int_)
    labels, num_regions = measure.label(binarised_emmap, background=0, return_num=True)
    
    return num_regions
    