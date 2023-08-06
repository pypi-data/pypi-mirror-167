import numpy as np
def sum_of_psd_2d(images):
    from emmer.ndimage.spectrum.spectrum_utils import psd2D
    psd2D_sum = None
    for image in images:
        if psd2D_sum is None:
            psd2D_sum = psd2D(image)
        else:
            psd2D_sum += psd2D(image)
    return np.array(psd2D_sum)


