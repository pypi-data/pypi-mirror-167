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

def shake_pdb_within_mask(pdb_path, mask_path, rmsd_magnitude,mask_threshold=0.5, verbose=False):
    from emmer.pdb.pdb_utils import detect_pdb_input
    from emmer.ndimage.map_utils import load_map
    from emmer.pdb.pdb_utils import get_all_atomic_positions, set_all_atomic_positions
    from emmer.pdb.convert.convert_polar_to_cartesian import convert_polar_to_cartesian
    from emmer.pdb.convert.convert_mrc_to_pdb_position import convert_mrc_to_pdb_position
    from emmer.pdb.convert.convert_pdb_to_mrc_position import convert_pdb_to_mrc_position
    from emmer.pdb.pdb_tools.compute_rmsd_two_pdb import compute_rmsd_two_pdb
    from emmer.ndimage.map_utils import get_all_voxels_inside_mask
    from tqdm import tqdm
    import random   
    
    ## Inputs
    st = detect_pdb_input(pdb_path)
    
    mask,apix = load_map(mask_path)
    
    outside_mask = np.logical_not(mask>=mask_threshold)
    
    voxel_positions_mask = get_all_voxels_inside_mask(mask, mask_threshold=0.5)
    pdb_positions_mask = np.array(convert_mrc_to_pdb_position(voxel_positions_mask, apix))
    
       
    ## Get all atomic positions, in real units (XYZ)
    atomic_positions_values = get_all_atomic_positions(st)  ## XYZ
    # Get shake vector     
    if verbose:
        print("Shaking the input structure with input RMSD of {}...".format(rmsd_magnitude))
    shake_radii = np.random.uniform(0, rmsd_magnitude*2, size=len(atomic_positions_values))
    shake_thetas = np.random.uniform(0, 2*np.pi, size=len(atomic_positions_values))
    shake_phis = np.random.uniform(0, np.pi, size=len(atomic_positions_values))
    
    shake_vectors_polar = np.column_stack((shake_radii, shake_thetas, shake_phis))
    if verbose:
        print("Checking for atoms outside the mask...")
    
    shaken_atomic_position_native = list(atomic_positions_values + convert_polar_to_cartesian(shake_vectors_polar, multiple=True))
    rmsd_native = compute_rmsd_two_pdb(shaken_atomic_position_native, atomic_positions_values, use_gemmi_structure=False)
    
    shaken_atomic_position= shaken_atomic_position_native.copy()
    
    shaken_mrc_position_list = [tuple(x) for x in convert_pdb_to_mrc_position(shaken_atomic_position, apix)]  ## ZYX
       
    
    
    
    num_atoms_outside = 0
    
    from sklearn.neighbors import KDTree
    tree = KDTree(pdb_positions_mask)
    
    for i,mrc_pos in enumerate(tqdm(shaken_mrc_position_list, "Validating positions")):
        if outside_mask[mrc_pos[0],mrc_pos[1],mrc_pos[2]]:
            neighborhood_indices_list = tree.query_radius(shaken_atomic_position[i:i+1], r=rmsd_magnitude*2) 
            random_index = random.choice(list(neighborhood_indices_list)[0])
            random_position = pdb_positions_mask[random_index] + np.random.uniform(0,apix/2,3)
                
            shaken_atomic_position[i] = random_position
            num_atoms_outside += 1

    if verbose:
        print("{} atoms found outside the mask! Randomly placed them inside the mask within its sphere of influence.".format(num_atoms_outside))
        print("Done... Now converting into PDB")
    
    shaken_atomic_positions_dictionary = {}
    for i,atomic_position in enumerate(shaken_atomic_position):
        shaken_atomic_positions_dictionary[i] = atomic_position
    
    shaken_structure = set_all_atomic_positions(st, shaken_atomic_positions_dictionary)


    if verbose:    
        rmsd = compute_rmsd_two_pdb(st, shaken_structure)
        print("RMSD between input structure and native shaken structure: {} A".format(round(rmsd_native,2)))
        print("RMSD between the input and output structure is: {} A".format(round(rmsd,2)))
        
    return shaken_structure      
