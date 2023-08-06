## Script to compute radial amplitude from resolution

def amplitude_from_resolution(freq, amplitudes, probe_resolution):
    from emmer.include.emmer_utils import probe_value_from_x
    xdata = freq
    ydata = amplitudes
    if probe_resolution <= 0:
        raise UserWarning("Enter probe resolution > 0A")
    x = 1/probe_resolution
    y = probe_value_from_x(x, xdata, ydata)
    probe_amplitude = y

    return probe_amplitude