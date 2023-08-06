## Script to compute radial amplitude variance

def compute_radial_amplitude_variance(vol):
    import numpy as np
    
    ps = np.abs( np.fft.rfftn(vol) )
    x, y, z = np.indices(ps.shape)
    radii = np.sqrt(x**2 + y**2 + z**2)
    radii = radii.astype(int)
    shell_variance = []
    for r in np.unique(radii)[0:vol.shape[0]//2]:
        idx = radii == r
        shell = ps[idx]
        variance = shell.var()
        shell_variance.append(variance)
    return np.array(shell_variance)
    