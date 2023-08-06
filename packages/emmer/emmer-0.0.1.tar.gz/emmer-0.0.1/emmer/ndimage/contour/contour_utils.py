#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 17:10:49 2022

@author: alok
"""
import numpy as np

def mesh_surface_area(data, threshold, apix):
    from skimage import measure
    
    verts, faces,_,_ = measure.marching_cubes(data, threshold)
    surface_area = measure.mesh_surface_area(verts, faces) * apix**2
    return surface_area






