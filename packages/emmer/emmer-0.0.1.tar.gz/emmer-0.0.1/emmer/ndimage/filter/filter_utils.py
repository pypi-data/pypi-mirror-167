import numpy as np
import mrcfile

def calculate_fourier_frequencies(im, apix):
    """Return the image frequency for every voxel in Fourierspace
    for n-dimensional images
    """
    per_axis_freq = [np.fft.fftfreq(N) for N in im.shape[:-1]]
    per_axis_freq.append(np.fft.rfftfreq(im.shape[-1]))
    dims = np.meshgrid(*per_axis_freq, indexing='ij', sparse=True)
    fourier_frequencies = np.sqrt(np.sum([dim**2 for dim in dims]))
    fourier_frequencies_angstrom = fourier_frequencies / apix
    return fourier_frequencies_angstrom

def tanh_filter(im_freq, cutoff):
    """Returns filter coefficients for a hyperbolic tangent filter. 
    """
    cutoff_freq = 1/cutoff
    filter_fall_off = 0.1;
    filter_coefficients = 1.0 - (1.0 - 0.5*(np.tanh((np.pi*(im_freq+cutoff_freq)/(2*filter_fall_off*cutoff_freq))) - np.tanh((np.pi*(im_freq-cutoff_freq)/(2*filter_fall_off*cutoff_freq)))));
    return filter_coefficients;

def get_fsc_filter(input_map_1, input_map_2):
    from emmer.ndimage.fsc.calculate_fsc_curve import calculate_fsc_curve
    fsc_curve = calculate_fsc_curve(input_map_1, input_map_2)
    C_ref = 2*fsc_curve / (1+fsc_curve)
    
    return C_ref

def window3D(w):
    # Convert a 1D filtering kernel to 3D
    # eg, window3D(numpy.hanning(5))
    L=w.shape[0]
    m1=np.outer(np.ravel(w), np.ravel(w))
    win1=np.tile(m1,np.hstack([L,1,1]))
    m2=np.outer(np.ravel(w),np.ones([1,L]))
    win2=np.tile(m2,np.hstack([L,1,1]))
    win2=np.transpose(win2,np.hstack([1,2,0]))
    win=np.multiply(win1,win2)
    return win



      