## Script to compute radial profile of a given volume

def compute_radial_profile(vol, return_indices=False):
    '''
    Computes the radial profile of a given volume

    Parameters
    ----------
    vol : numpy.ndarray
        Input array
    center : list, optional
        DESCRIPTION. The default is [0,0,0].
    return_indices : bool, optional
        

    Returns
    -------
    radial_profile : numpy.ndarray (1D)
        Radial profile
        

    '''
    import numpy as np

    dim = vol.shape
    m = np.mod(vol.shape,2)

    ps = np.abs( np.fft.rfftn(vol) )
    if not return_indices:
        x, y, z = np.indices(ps.shape)
        radii = np.sqrt(x**2 + y**2 + z**2)
        radii = radii.astype(int)
    else:
        [x, y, z] = np.mgrid[-dim[0]//2+m[0]:(dim[0]-1)//2+1, -dim[1]//2+m[1]:(dim[1]-1)//2+1, 0:dim[2]//2+1]
        x = np.fft.ifftshift(x)
        y = np.fft.ifftshift(y)
        radii = np.sqrt(x**2 + y**2 + z**2)
        radii = radii.astype(int)
    
    radial_profile = np.bincount(radii.ravel(), ps.ravel()) / np.bincount(radii.ravel())
    # exclude corner frequencies
    radial_profile = radial_profile[0:int(ps.shape[0]/2)]
    if not return_indices:
        return radial_profile
    else:
        return radial_profile, radii