## Script to perform band pass filtering of cryo EM maps

from emmer.ndimage.filter.low_pass_filter import low_pass_filter
from emmer.ndimage.filter.high_pass_filter import high_pass_filter

def band_pass_filter(im, minimum_resolution, maximum_resolution, apix):
    
    im_low_pass = low_pass_filter(im, maximum_resolution, apix)
    im_high_pass = high_pass_filter(im_low_pass, minimum_resolution, apix)
    
    return im_high_pass
    