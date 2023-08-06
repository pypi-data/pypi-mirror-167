## Script to compute FSC at a given resolution for two maps


def compute_fsc_resolution(input_map_1, input_map_2, threshold, apix):
    '''
    Function to calculate the FSC curve from two given input
    input_map_1 : either numpy.ndarray or path to mrc file
    input_map_2 : either numpy.ndarray or path to mrc file
    resolution : float
        resolution at which FSC is to be calculated
    '''
    from emmer.ndimage.fsc import calculate_fsc_curve
    from emmer.include.emmer_utils import probe_value_from_y
    from emmer.ndimage.radial_profile.frequency_array import frequency_array

    fsc_curve = calculate_fsc_curve(input_map_1, input_map_2)
    fsc_curve = np.array(fsc_curve)
    freq = frequency_array(fsc_curve, apix)

    fsc_resolution = probe_value_from_y(y=threshold, xdata=freq, ydata=fsc_curve)

    return fsc_resolution
    