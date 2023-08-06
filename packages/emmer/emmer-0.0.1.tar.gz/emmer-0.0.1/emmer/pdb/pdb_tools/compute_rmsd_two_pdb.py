#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:11:29 2020

@author: Alok, Arjen, Maarten, Stefan, Reinier 
"""

# pdb_tools contains several useful fucntions for common manipulations with
# pdb structures, making use of the gemmi package. functions are classified 
# into pdb_tools when they can be considered an application on their own
# but do not have so many distinct features that they warrent their own script.

# global imports
import mrcfile
import gemmi
import numpy as np

#%% functions

def compute_rmsd_two_pdb(input_pdb_1, input_pdb_2, use_gemmi_structure=True, return_array=False):
    from emmer.pdb.pdb_utils import detect_pdb_input, get_all_atomic_positions
    from scipy.spatial import distance
    
    
    if use_gemmi_structure:
        st_1 = detect_pdb_input(input_pdb_1)
        st_2 = detect_pdb_input(input_pdb_2)
        
        num_atoms_1 = st_1[0].count_atom_sites()
        num_atoms_2 = st_2[0].count_atom_sites()
        
        positions_1 = get_all_atomic_positions(st_1)
        positions_2 = get_all_atomic_positions(st_2)
        
        assert num_atoms_1 == num_atoms_2
    
    else:
        positions_1 = input_pdb_1
        positions_2 = input_pdb_2
        
        assert len(positions_1) == len(positions_2)
        
    
    atomic_distance = []
    for index in range(len(positions_1)):
        dist = distance.euclidean(positions_1[index], positions_2[index])
        atomic_distance.append(dist)
    
    atomic_distance = np.array(atomic_distance)
    
    if return_array:
        return atomic_distance
    else:
        return np.mean(atomic_distance)
