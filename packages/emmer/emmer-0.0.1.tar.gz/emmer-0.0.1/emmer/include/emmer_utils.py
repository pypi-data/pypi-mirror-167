import numpy as np
import math


def round_up_to_even(x):
    ceil_x = math.ceil(x)
    if ceil_x % 2 == 0:   ## check if it's even, if not return one higher
        return ceil_x
    else:
        return ceil_x+1

def round_up_to_odd(x):
    ceil_x = math.ceil(x)
    if ceil_x % 2 == 0:   ## check if it's even, if so return one higher
        return ceil_x+1
    else:
        return ceil_x

def true_percent_probability(n):
    x = np.random.uniform(low=0, high=100)
    if x <= n:
        return True
    else:
        return False

def copy_file_to_folder(full_path_to_file, new_folder):
    import shutil
    import os
    
    source = full_path_to_file
    file_name = os.path.basename(source)
    destination = os.path.join(new_folder, file_name)
    shutil.copyfile(source, destination)
    
    return destination

def linear(x,a,b):
    return a * x + b

def general_quadratic(x,a,b,c):
    return a * x**2 + b*x + c
    

def round_up_proper(x):
    epsilon = 1e-15  ## To round up in case of rounding to odd
    return np.round(x+epsilon).astype(int)


## Function to probe the value of Y from a given X value
def probe_value_from_x(x, xdata, ydata):
    from scipy.interpolate import interp1d
    ## Make sure x is between the min and max of xdata
    x = np.clip(x, xdata.min(), xdata.max())

    f = interp1d(xdata, ydata)
    y_probe = f(x)
    return y_probe

## Function to probe the value of X from a given Y value
def probe_value_from_y(y, xdata, ydata):
    from scipy.interpolate import interp1d
    ## Make sure y is between the min and max of ydata
    y = np.clip(y, ydata.min(), ydata.max())

    f = interp1d(ydata, xdata)
    x_probe = f(y)
    return x_probe
