## Script to smoothen a binarised map using cosine edge falloff

def smoothen_mask(binarised_mask,cosine_falloff_length):
    '''
    binarised_mask: a binarised map
    cosine_falloff_length: length of cosine falloff
    '''
    from emmer.ndimage.filter.filter_utils import window3D
    from scipy import signal
    
    cosine_window_1d = signal.cosine(cosine_falloff_length)
    cosine_window_3d = window3D(cosine_window_1d)
    cosine_mask = signal.fftconvolve(binarised_mask,cosine_window_3d,mode='same')
    cosine_mask = cosine_mask/cosine_mask.max()
    return cosine_mask