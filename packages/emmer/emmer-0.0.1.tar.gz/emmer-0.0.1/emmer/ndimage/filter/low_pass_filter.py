## Script to perform low pass filtering of cryo EM maps
import numpy as np
def low_pass_filter(im, cutoff, apix):

    """
    Returns a low-pass filter image from a tanh filter.
    """
    import numpy as np

    from emmer.ndimage.filter.filter_utils import calculate_fourier_frequencies, tanh_filter
    
    im_freq     = calculate_fourier_frequencies(im, apix=apix)
    im_filter   = tanh_filter(im_freq, cutoff);
    im_fft      = np.fft.rfftn(im)
    im_fft_filtered = im_fft * im_filter
    im_filtered = np.fft.irfftn(im_fft_filtered)
    return im_filtered