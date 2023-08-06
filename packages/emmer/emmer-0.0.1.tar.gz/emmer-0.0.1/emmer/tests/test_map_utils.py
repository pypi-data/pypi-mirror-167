
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

class test_map_utils(unittest.TestCase):
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
        


    def test_load_map(self):
        
        from emmer.ndimage.map_utils import load_map
        
        sample_emmap_path = self.emmap_path

        ## create temporary directory
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as tmpdir:
            copied_sample_emmap_path = self.copy_files(sample_emmap_path, tmpdir)
            emmap, apix = load_map(copied_sample_emmap_path)

            self.assertTrue(emmap.shape == (256,256,256))
            self.assertAlmostEqual(apix, 1.2156, delta=0.1)
        
    def test_parse_input(self):
        from emmer.ndimage.map_utils import parse_input
        from emmer.ndimage.map_utils import load_map
        
        sample_emmap_path = self.emmap_path

        ## create temporary directory
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as tmpdir:
            copied_sample_emmap_path = self.copy_files(sample_emmap_path, tmpdir)
            emmap, apix = load_map(copied_sample_emmap_path)

            emmap_from_path = parse_input(copied_sample_emmap_path)
            emmap_from_array = parse_input(emmap)
            emmap_from_nonsense = parse_input("this_is_a_nonsense_path")

            self.assertTrue(np.array_equal(emmap_from_path, emmap))
            self.assertTrue(np.array_equal(emmap_from_array, emmap))
            self.assertTrue(emmap_from_nonsense is None)
    
    def test_read_gemmi_path(self):
        from emmer.ndimage.map_utils import read_gemmi_map
        import gemmi
        sample_emmap_path = self.emmap_path

        ## create temporary directory
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as tmpdir:
            copied_sample_emmap_path = self.copy_files(sample_emmap_path, tmpdir)
            emmap, grid = read_gemmi_map(copied_sample_emmap_path, return_grid=True)

            self.assertTrue(emmap.shape == (256,256,256))
            xyz_axis_order = grid.axis_order.value
                       
            self.assertTrue(xyz_axis_order == 1)
    
    def test_save_as_mrc(self):
        from emmer.ndimage.map_utils import save_as_mrc
        import os
        ## create temporary directory
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as tmpdir:
            temp_mrc_path = os.path.join(tmpdir,'temp.mrc')
            zeros = np.zeros((256,256,256))
            save_as_mrc(zeros, temp_mrc_path, apix=3)
            
            self.assertTrue(os.path.exists(temp_mrc_path))
    
    def test_compare_grid(self):
        from emmer.ndimage.map_utils import compare_gemmi_grids, save_as_mrc, read_gemmi_map
        sample_emmap_path = self.emmap_path

        ## create temporary directory
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as tmpdir:
            random_map_1 = np.random.uniform(0,1,(256,256,256))       
            random_map_2 = np.random.uniform(0,1,(256,256,256))
            random_map_3 = np.random.uniform(0,1,(256,256,256))

            temp_mrc_path_1 = os.path.join(tmpdir,'temp_1.mrc')
            temp_mrc_path_2 = os.path.join(tmpdir,'temp_2.mrc')
            temp_mrc_path_3 = os.path.join(tmpdir,'temp_3.mrc')

            save_as_mrc(random_map_1, temp_mrc_path_1, apix=3)
            save_as_mrc(random_map_2, temp_mrc_path_2, apix=3)
            save_as_mrc(random_map_3, temp_mrc_path_3, apix=2)

            emmap_1, grid_1 = read_gemmi_map(temp_mrc_path_1, return_grid=True)
            emmap_2, grid_2 = read_gemmi_map(temp_mrc_path_2, return_grid=True)
            emmap_3, grid_3 = read_gemmi_map(temp_mrc_path_3, return_grid=True)
            

            self.assertTrue(compare_gemmi_grids(grid_1, grid_2)['final'].all())
            self.assertFalse(compare_gemmi_grids(grid_1, grid_3)['final'].all())
    

    
            
