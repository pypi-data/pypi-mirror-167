## Function to return frequency array from a array of amplitudes and pixel size
import numpy as np
def frequency_array(amplitudes=None, apix=None, n=None):
    '''
    Function to return frequency array from a array of amplitudes and pixel size
    
    Parameters
    ----------
    amplitudes : ndarray
        Array of amplitudes
    apix : float
        Pixel size in Angstroms
    n : int
        Number of points in the frequency array
    Returns
    -------
    frequency_array : ndarray
        Array of frequencies
    '''
    ## Check inputs
    if amplitudes is None and n is None:
        raise ValueError("Must provide either amplitudes or n")
    if apix is None:
        raise ValueError("Must provide apix")
    if amplitudes is not None and n is not None:
        raise ValueError("Must provide either amplitudes or n")

    if amplitudes is not None:
        n = len(amplitudes)
    else:
        n = int(n)
    ## Calculate frequency array
    freq = np.linspace(1/(apix*n),1/(apix*2),n,endpoint=True)

    return freq

    