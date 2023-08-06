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
