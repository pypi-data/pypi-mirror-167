## Script to calculate the Real Space Cross Correlation (RSCC) between two maps, or any two ndarrays.


def compute_real_space_correlation(input_map_1,input_map_2):
    '''
    Function to calculate the Real Space Cross Correlation (RSCC) between two maps, or any two ndarrays. 
    
    RSCC is calculated by standardizing two arrays by subtracting their mean and dividing by their standard deviation

    Parameters
    ----------
    array1 : numpy.ndarray
        
    array2 : numpy.ndarray
        

    Returns
    -------
    RSCC : float
        Floating point number between 0 and 1 showing the RSCC between two arrays

    '''
    from emmer.ndimage.map_utils import parse_input
    array1 = parse_input(input_map_1)
    array2 = parse_input(input_map_2)
    
    (map1_mean,map1_std) = (array1.mean(),array1.std())
    (map2_mean,map2_std) = (array2.mean(),array2.std())
    
    n = array1.size
    
    RSCC = (((array1-map1_mean)*(array2-map2_mean))/(map1_std*map2_std)).sum() * (1/n)
    
    return RSCC