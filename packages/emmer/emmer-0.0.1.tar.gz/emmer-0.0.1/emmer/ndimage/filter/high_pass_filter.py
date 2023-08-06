## Script to perform high pass filtering of cryo EM maps

def high_pass_filter(im, cutoff, apix):
    """
    Returns a high-pass filter image from a tanh filter.
    """
    from emmer.ndimage.filter.filter_utils import calculate_fourier_frequencies, tanh_filter
    import numpy as np

    im_freq     = calculate_fourier_frequencies(im, apix=apix)
    im_filter   = 1-tanh_filter(im_freq, cutoff);
    im_fft      = np.fft.rfftn(im)
    im_fft_filtered = im_fft * im_filter
    im_filtered = np.fft.irfftn(im_fft_filtered)
    return im_filtered

    