#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 13:32:59 2022

@author: alok
"""
import numpy as np

def convert_polar_to_cartesian(polar_vector, multiple=False):
    '''
    Convert polar to cartesian.. Blindly following the formula mentioned here: 
        https://math.libretexts.org/Bookshelves/Calculus/Book%3A_Calculus_(OpenStax)/12%3A_Vectors_in_Space/12.7%3A_Cylindrical_and_Spherical_Coordinates#:~:text=To%20convert%20a%20point%20from,and%20z%3D%CF%81cos%CF%86.
        (accessed: 23-2-2022) 
    
    
    polar_vector: (r, theta, phi) !!
    Theta is the angle in the XY plane

    Parameters
    ----------
    r : float
        
    phi : float 
        first angle in radians
    theta : float
        second angle in radians

    Returns
    -------
    cartesian : numpy.ndarray [1x3]
        (x,y,z)

    '''
    if multiple:
        cartesians = []
        for vector in polar_vector:
            r, theta, phi = vector
            x = r * np.sin(phi) * np.cos(theta)
            y = r * np.sin(phi) * np.sin(theta)
            z = r * np.cos(phi)
            cartesians.append(np.array([x,y,z]))
        return np.array(cartesians)
    else:
        r, theta, phi = polar_vector
        x = r * np.sin(phi) * np.cos(theta)
        y = r * np.sin(phi) * np.sin(theta)
        z = r * np.cos(phi)
    
        cartesian = np.array([x,y,z])
    
        return cartesian

def convert_cartesian_to_polar(cartesian):
    '''
    Same as above

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.
    y : TYPE
        DESCRIPTION.
    z : TYPE
        DESCRIPTION.

    Returns
    -------
    Polar : numpy.ndarray

    '''
    x, y, z = cartesian
    r = np.sqrt(np.power(x,2)+np.power(y,2)+np.power(z,2))
    theta = np.arctan(y/x)
    phi = np.arccos(z / r)
    
    polar = np.array([r, theta, phi])
    
    return polar

def get_random_polar_vector(rmsd_magnitude, randomisation="uniform", mean=None):
    if randomisation == "normal":
        if mean is not None:
            r = abs(np.random.normal(loc=mean, scale=rmsd_magnitude))  ## r will be a normally distributed, positive definite variable
            theta = np.random.uniform(0, 2*np.pi)
            phi = np.random.uniform(0, np.pi)
        else:
            r = abs(np.random.normal(loc=0, scale=rmsd_magnitude))  ## r will be a normally distributed, positive definite variable
            theta = np.random.uniform(0, 2*np.pi)
            phi = np.random.uniform(0, np.pi)
                                        
    elif randomisation == "uniform":
        r = np.random.uniform(low=0, high=rmsd_magnitude*2)
        theta = np.random.uniform(0, 2*np.pi)
        phi = np.random.uniform(0, np.pi)
    else:
        raise ValueError("The variable randomisation has only two inputs: normal or uniform")
    
    return np.array([r, theta, phi])

def convert_pdb_to_mrc_position(pdb_position, apix):
    '''
    Convert the real units of positions into indices for the emmap. 
    Note: returns in (Z,Y,X) format
    

    Parameters
    ----------
    pdb_position : list
        list of xyz positions (Angstorm)
    apix : float
        Pixel size 

    Returns
    -------
    mrc_position : list
        List of ZYX positions (index positions)

    '''
    mrc_position = []
    
    for pos in pdb_position:
        [x,y,z] = pos
        int_x, int_y, int_z = int(round(x/apix)), int(round(y/apix)), int(round(z/apix))
        mrc_position.append([int_z, int_y, int_x])
        
    return mrc_position

def convert_mrc_to_pdb_position(mrc_position_list, apix):
    '''
    Convert the real units of positions into indices for the emmap. 
    Note: returns in (Z,Y,X) format
    
    Parameters
    ----------
    mrc_position_list : list
        list of xyz positions (Angstorm)
    apix : float
        Pixel size 

    Returns
    -------
    pdb_position_list : list
        List of XYZ positions (index positions)

    '''
    pdb_position_list = []
    
    for pos in mrc_position_list:
        [nz,ny,nx] = pos
        z, y, x  = nz*apix, ny*apix, nx*apix
        pdb_position_list.append([x, y, z])
        
    return pdb_position_list
