## Script to compute resolution from an amplitude

def resolution_from_amplitude(freq, amplitudes, probe_amplitude):
    from emmer.include.emmer_utils import probe_value_from_y
    xdata = freq
    ydata = amplitudes
    if probe_amplitude <= 0:
        raise UserWarning("Enter probe amplitude > 0")
    y = probe_amplitude
    x = probe_value_from_y(y, xdata, ydata)
    probe_resolution = 1/x

    return probe_resolution