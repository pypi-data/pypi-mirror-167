import numpy as np
import mrcfile

def load_map(map_path, return_apix = True):
    from emmer.ndimage.map_utils import average_voxel_size
    
    emmap = mrcfile.open(map_path).data
    apix = average_voxel_size(mrcfile.open(map_path).voxel_size)
    
    if return_apix:
        return emmap, apix
    else:
        return emmap

def parse_input(input_map):
    '''
    Function to detect type of input and return a emmap numpy array

    Parameters
    ----------
    input_map : str or numpy array or Mrc object
    string type input should be path/to/emmap.mrc    

    Returns
    -------
    emmap : numpy.ndarray

    '''
    import os
    
    if isinstance(input_map, np.ndarray):
        if len(input_map.shape) == 3:
            return input_map
        else:
            print("You have not input a 3-D numpy array, which cannot be a EM-map")
            return None
    elif isinstance(input_map, str):
        if os.path.exists(input_map):
            emmap = mrcfile.open(input_map).data
            return emmap
        else:
            print("You have not entered a proper path, or the requested file does not exist!")
            return None
    
    
def read_gemmi_map(map_path, return_grid=False):
    '''
    Function to read a map file and return a numpy.ndarray using gemmi.read_ccp4() map

    Parameters
    ----------
    map_path : str
        path/to/emmap.mrc

    Returns
    -------
    emmap : numpy.ndarray
        
    '''
    import gemmi

    gemmi_ccp4Map = gemmi.read_ccp4_map(map_path)
    emmap = np.array(gemmi_ccp4Map.grid, copy=False)
    
    if return_grid:
        return emmap, gemmi_ccp4Map.grid
    else:
        return emmap
    
    
def save_as_mrc(map_data, output_filename, apix=None,origin=None, verbose=False, header=None):
    '''
    Function to save a numpy array containing volume, as a MRC file with proper header

    Parameters
    ----------
    map_data : numpy.ndarray
        Volume data showing the intensities of the EM Map at different points

    apix : float or any iterable
        In case voxelsize in x,y,z are all equal you can also just pass one parameter. 
    output_filename : str
        Path to save the MRC file. Example: 'path/to/map.mrc'
    origin: float or any iterable, optional
        In case origin index in x,y,z are all equal you can also just pass one parameter. 

    Returns
    -------
    Saves MRC .

    '''
    import mrcfile

    with mrcfile.new(output_filename,overwrite=True) as mrc:
        mrc.set_data(np.float32(map_data))
        
        if header is not None:
            mrc.set_extended_header(header)
        
        else:
            if apix is not None:
                #apix_list = [apix['x'], apix['y'], apix['z']]
                ## apix can be either a float or a list. If it's a single number, then the function convert_to_tuple will use it three times
                apix_tuple = convert_to_tuple(apix, num_dims=3)
                rec_array_apix = np.rec.array(apix_tuple, dtype=[('x','<f4'),('y','<f4'),('z','<f4')])
                mrc.voxel_size = rec_array_apix
            else:
                print("Please pass a voxelsize value either as a float or an iterable")
                return 0
            
            if origin is not None:    
                origin_tuple = convert_to_tuple(origin,num_dims=3)
            else:
                origin_tuple = convert_to_tuple(input_variable=0,num_dims=3)
            rec_array_origin = np.rec.array(origin_tuple, dtype=[('x','<f4'),('y','<f4'),('z','<f4')])
            mrc.header.origin = origin_tuple
            
        if verbose:
            print("Saving as MRC file format with following properties: ")
            print("Voxel size", mrc.voxel_size)
            print("Origin", mrc.header.origin)
        
    mrc.close()


def compare_gemmi_grids(grid_1, grid_2, verbose=False):
    '''
    Function to test similarity of two gemmi grids. Test include: 
        (a) Axis order
        (b) Voxelsize
        (c) UnitCell
        (d) Shape
        

    Parameters
    ----------
    grid_1 : gemmi.FloatGrid
        
    grid_2 : gemmi.FloatGrid

    Returns
    -------
    report : pandas.DataFrame
    

    '''
    import pandas as pd
    report = pd.DataFrame()
    report['axis_order'] = [grid_1.axis_order.name,grid_2.axis_order.name]
    report['spacing'] = [grid_1.spacing,grid_2.spacing]
    report['unitcell'] = [grid_1.unit_cell,grid_2.unit_cell]
    report['shape'] = [grid_1.shape, grid_2.shape]
    
    report = report.T
    report['final'] = report[0] == report[1] 
    if verbose:
        if report['final'].all():
            print("The two input grids are same")
        else:
            print("Two input grids are not the same")
            print(report['final'])
    return report
    
def extract_window(im, center, size):
    '''
    Extract a square window at a given location. 
    The center position of the window should be provided.

    Parameters
    ----------
    im : numpy.ndarray
        3D numpy array
    center : tuple, or list, or numpy.array (size=3)
        Position of the center of the window
    size : int, even
        Total window size (edge to edge) as an even number
        (In future could be modified to include different sized window 
        in different directions)
        

    Returns
    -------
    window : numpy.ndarray
        3D numpy array of shape (size x size x size)

    '''
    z,y,x = center
    window = im[z-size//2:z+size//2, y-size//2:y+size//2, x-size//2:x+size//2]
    return window

def binarizeMap(emmap, threshold):
	binarised = (emmap>=threshold).astype(np.int_)
	return binarised

def average_voxel_size(voxel_size_record):
    apix_x = voxel_size_record.x
    apix_y = voxel_size_record.y
    apix_z = voxel_size_record.z
    
    average_apix = (apix_x+apix_y+apix_z)/3
    
    return average_apix

   
def get_sphere(radius):
    '''
    Function to return a window, with a spherical mask. Size of the window defined by the radius.
    Parameters
    ----------
    radius : int
        Radius of sphere, in pixels

    Returns
    -------
    sphere : numpy.ndarray
        Shape: (rad+1) x (rad+1)

    '''
    z,y,x = np.ogrid[-radius: radius+1, -radius: radius+1, -radius: radius+1]
    sphere = (x**2+y**2+z**2 <= radius**2).astype(int)
    return sphere


def moving_average(array,window=5):
    return np.convolve(array,np.ones(window), 'same')/window

def normalise(x):
    if isinstance(x,np.ndarray):
        return x/x.max()
    else:
        x = np.array(x)
        return x/x.max()

def dilate_mask(mask, radius, iterations=1):
    '''
    Dilate mask with spherical structures

    Parameters
    ----------
    mask : numpy.ndarray
        Skeleton structure of a set of atoms
    radius : int
        Cutoff radius used for binary dilation
    iterations : int, optional
        Number of iterations for binary dilation The default is 1.

    Returns
    -------
    dilated : numpy.ndarray
        Dilated mask

    '''
    from scipy.ndimage import binary_dilation
    from emmer.ndimage.map_utils import get_sphere
    
    dilated = binary_dilation(mask, structure=get_sphere(radius), iterations=iterations).astype(int)
        
    return dilated

def convert_to_tuple(input_variable, num_dims=3):
    '''
    Convert any variable, or iterable into a tuple. If a scalar is input then a tuple is generated with same variable
    based on number of dimensions mentioned in num_dims

    Parameters
    ----------
    input_variable : any
        scalar, or any iterable
    num_dims : int, optional
        Length of tuple. The default is 3.
        
    Returns
    -------
    output_tuple : tuple

    '''
    
    if hasattr(input_variable, '__iter__'):
        if len(input_variable) == num_dims:
            output_tuple = tuple(input_variable)
            return output_tuple
        else:
            print("Input variable dimension {} doesn't match expected output dimension {}".format(len(input_variable), num_dims))
    else:
        output_list = [input_variable for temporary_index in range(num_dims)]
        output_tuple = tuple(output_list)
        return output_tuple
    
def get_all_voxels_inside_mask(binarised_mask, mask_threshold=1):
    all_inside_mask = np.asarray(np.where(binarised_mask>=mask_threshold)).T.tolist()
    return all_inside_mask





    
    
    
    
################################### CODE HELL ######################################

# =============================================================================
# def convert_to_tuple_2(input_variable, num_dims=3):
#     '''
#     Convert any variable, or iterable into a tuple. If a scalar is input then a tuple is generated with same variable
#     based on number of dimensions mentioned in num_dims
# 
#     Parameters
#     ----------
#     input_variable : any
#         scalar, or any iterable
#     num_dims : int, optional
#         Length of tuple. The default is 3.
#         
#     Returns
#     -------
#     output_tuple : tuple
# 
#     '''
#     
#     if hasattr(input_variable, '__iter__'):
#         if isinstance(input_variable, np.recarray):
#             input_variable = [input_variable['x'], input_variable['y'], input_variable['z']]
#         
#         if len(input_variable) == num_dims:
#             output_tuple = tuple(input_variable)
#             return output_tuple
#         else:
#             print("Input variable dimension {} doesn't match expected output dimension {}".format(len(input_variable), num_dims))
#     else:
#         output_list = [input_variable for temporary_index in range(num_dims)]
#         output_tuple = tuple(output_list)
#         return output_tuple  
#     
#     
# =============================================================================
