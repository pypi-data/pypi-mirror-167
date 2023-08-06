## Script to measure the volume of a cryo EM map at a given threshold using the ConvexHull algorithm

def volume_at_threshold(emmap, apix, reference_threshold):
    import numpy as np

    binarised_emmap = (emmap>=reference_threshold).astype(np.int_)
    sum_of_voxels = binarised_emmap.sum()
    volume_real_units = sum_of_voxels * apix**3

    return volume_real_units

    
