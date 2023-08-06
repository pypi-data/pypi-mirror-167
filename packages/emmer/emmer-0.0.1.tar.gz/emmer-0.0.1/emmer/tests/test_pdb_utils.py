
# -*- coding: utf-8 -*-
"""
Created on 25 April 2022

@author: alok
"""

import unittest
import gemmi
import mrcfile
import numpy as np
import os

class test_pdb_utils(unittest.TestCase):
    def setUp(self):
        import pickle
        import emmer
        
        emmer_module_path = os.path.dirname(emmer.__file__)
        emmer_install_path = emmer_module_path
        self.emmer_install_path = emmer_install_path
        os.sys.path.insert(0, self.emmer_install_path)
        
        self.data_folder = os.path.join(self.emmer_install_path, 'tests','ndimage_unittest','data') 
        self.emmap_path = os.path.join(self.data_folder,'emd5778_map.mrc')
        self.mask_path = os.path.join(self.data_folder,'emd5778_mask.mrc')
        self.pdb_path = os.path.join(self.data_folder,'pdb3j5p.pdb')
        self.modmap_path = os.path.join(self.data_folder,'pdb3j5p_map.mrc')
        
        verify_output_file = os.path.join(self.emmer_install_path, 'tests','ndimage_unittest','verify','ndimage_outputs.pickle') 
        with open(verify_output_file, "rb") as outfile:
            self.validate = pickle.load(outfile)
        
    def copy_files(self, file_path, tempDir):
        from subprocess import run
        run(["cp",file_path,tempDir])
        if os.path.exists(os.path.join(tempDir, os.path.basename(file_path))):               
            return os.path.join(tempDir, os.path.basename(file_path))
            
        else:
            raise UserWarning("Could not copy {} to {}".format(path,tempDir))
        
    def test_replace_pdb_column_with_array(self):
        from emmer.pdb.pdb_utils import replace_pdb_column_with_arrays, detect_pdb_input
        
        pdb_path = self.pdb_path
        ## create temporary directory
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as tmpdir:
            copied_pdb_path = self.copy_files(pdb_path, tmpdir)
            st = detect_pdb_input(copied_pdb_path)
            num_atoms = st[0].count_atom_sites()
            random_array = np.random.randint(0,999,num_atoms)
            pdb_replaced_bfactor = replace_pdb_column_with_arrays(input_pdb=st, replace_column="bfactor", replace_array=random_array)
            pdb_replaced_occupancy = replace_pdb_column_with_arrays(input_pdb=st, replace_column="occ", replace_array=random_array)

            replaced_bfactor_list = []
            for cra_obj in pdb_replaced_bfactor[0].all():
                atom = cra_obj.atom
                replaced_bfactor_list.append(atom.b_iso)
            
            replaced_bfactor_list = np.array(replaced_bfactor_list)

            replaced_occupancy_list = []
            for cra_obj in pdb_replaced_occupancy[0].all():
                atom = cra_obj.atom
                replaced_occupancy_list.append(atom.occ)
            
            replaced_occupancy_list = np.array(replaced_occupancy_list)

            self.assertTrue(np.allclose(replaced_bfactor_list, random_array))
            self.assertTrue(np.allclose(replaced_occupancy_list, random_array))

    def test_set_all_atomic_positions(self):
        from emmer.pdb.pdb_utils import set_all_atomic_positions, get_all_atomic_positions, detect_pdb_input

        pdb_path = self.pdb_path
        ## create temporary directory
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as tmpdir:
            copied_pdb_path = self.copy_files(pdb_path, tmpdir)
            st = detect_pdb_input(copied_pdb_path)
            num_atoms = st[0].count_atom_sites()
            random_positions = {}
            for i in range(num_atoms):
                random_positions[i] = np.random.randint(0,999, size=3)
            
            random_positions_array = np.array(list(random_positions.values()))
            pdb_changed_positions = set_all_atomic_positions(input_pdb=st, positions_dictionary=random_positions)

            pdb_test_changed_positions = get_all_atomic_positions(input_pdb=pdb_changed_positions, as_dictionary=False) 

            self.assertTrue(np.allclose(random_positions_array, pdb_test_changed_positions))
    
    def test_gemmi_neighbor_analysis(self):
        from emmer.pdb.pdb_utils import find_number_of_neighbors, get_atomic_bfactor_window, detect_pdb_input, get_all_atomic_positions, get_bfactors
        import random

        pdb_path = self.pdb_path
        ## create temporary directory
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as tmpdir:
            copied_pdb_path = self.copy_files(pdb_path, tmpdir)
            st = detect_pdb_input(copied_pdb_path)

            pdb_positions = get_all_atomic_positions(input_pdb=st, as_dictionary=False)
            pdb_bfactors = get_bfactors(input_pdb=st)

            random_position = random.choice(list(pdb_positions))

            num_neighbors = find_number_of_neighbors(input_pdb=st, atomic_position=random_position, window_size_A=5.0)
            bfactor_window = get_atomic_bfactor_window(input_pdb=st, atomic_position=random_position, window_size_A=5.0)

            self.assertTrue(num_neighbors > 0 and num_neighbors < len(pdb_positions))
            self.assertTrue(bfactor_window > min(pdb_bfactors) and bfactor_window < max(pdb_bfactors))




            



                
           
            


      