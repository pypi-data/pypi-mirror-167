import numpy as np
def psd2D(image):
    from scipy import fft
    F1 = fft.fft2(image)
    F2 = fft.fftshift( F1 )
    psd2D = np.abs( F2 )**2
    return psd2D