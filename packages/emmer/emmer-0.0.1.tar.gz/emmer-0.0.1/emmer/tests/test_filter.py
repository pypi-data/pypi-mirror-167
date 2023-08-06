#!/usr/bin/env python3
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

class test_filter(unittest.TestCase):
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
        


    def test_low_pass_filter(self):
        from emmer.ndimage.filter.low_pass_filter import low_pass_filter
        from emmer.ndimage.map_utils import load_map
        from emmer.ndimage.radial_profile.compute_radial_profile import compute_radial_profile
        from emmer.ndimage.radial_profile.frequency_array import frequency_array
        from emmer.ndimage.radial_profile.profile_tools import get_index_at_resolution
        
        sample_emmap_path = self.emmap_path
        
        ## create temporary directory
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as tmpdir:
            copied_sample_emmap_path = self.copy_files(sample_emmap_path, tmpdir)
            
            filter_cutoff = np.random.uniform(5,20,1)
            output_map_path = os.path.join(tmpdir,'emd5778_map_filtered.mrc')
            emmap, apix = load_map(copied_sample_emmap_path)
            filtered_emmap = low_pass_filter(emmap, apix=apix, cutoff=filter_cutoff)
            
            
            ## test that the filtered map amplitude smaller than the original map

            rp_emmap = compute_radial_profile(emmap)
            rp_filtered_emmap = compute_radial_profile(filtered_emmap)

            freq = frequency_array(rp_emmap, apix=1.2156)
            filter_index = get_index_at_resolution(freq, filter_cutoff/2)

            rp_emmap_0 = rp_emmap[0]
            rp_filtered_emmap_0 = rp_filtered_emmap[0]

            rp_emmap_filtered_index = rp_emmap[filter_index]
            rp_filtered_emmap_filtered_index = rp_filtered_emmap[filter_index]

            self.assertTrue(rp_emmap_filtered_index > rp_filtered_emmap_filtered_index)
            self.assertAlmostEqual(rp_emmap_0, rp_filtered_emmap_0, delta=0.01)
    
    def test_high_pass_filter(self):
        from emmer.ndimage.filter.high_pass_filter import high_pass_filter
        from emmer.ndimage.map_utils import load_map
        from emmer.ndimage.radial_profile.compute_radial_profile import compute_radial_profile
        from emmer.ndimage.radial_profile.frequency_array import frequency_array
        from emmer.ndimage.radial_profile.profile_tools import get_index_at_resolution
        
        sample_emmap_path = self.emmap_path
        
        ## create temporary directory
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as tmpdir:
            copied_sample_emmap_path = self.copy_files(sample_emmap_path, tmpdir)
            
            filter_cutoff = np.random.uniform(5,20,1)
            output_map_path = os.path.join(tmpdir,'emd5778_map_filtered.mrc')
            emmap, apix = load_map(copied_sample_emmap_path)
            filtered_emmap = high_pass_filter(emmap, apix=apix, cutoff=filter_cutoff)
            
            
            ## test that the filtered map amplitude smaller than the original map

            rp_emmap = compute_radial_profile(emmap)
            rp_filtered_emmap = compute_radial_profile(filtered_emmap)

            freq = frequency_array(rp_emmap, apix=1.2156)
            filter_index = get_index_at_resolution(freq, filter_cutoff/2)

            rp_emmap_0 = rp_emmap[0]
            rp_filtered_emmap_0 = rp_filtered_emmap[0]

            rp_emmap_filtered_index = rp_emmap[filter_index]
            rp_filtered_emmap_filtered_index = rp_filtered_emmap[filter_index]

            self.assertTrue(rp_emmap_0 > rp_filtered_emmap_0)
            self.assertAlmostEqual(rp_emmap_filtered_index, rp_filtered_emmap_filtered_index, delta=0.01)
    
    def test_get_cosine_mask(self):
        from emmer.ndimage.filter.smoothen_mask import smoothen_mask
        import random
        from scipy.ndimage import binary_dilation
        ## get sphere at a random location in a map
        zeros = np.zeros((100,100,100))

        center = (random.randint(30,70),random.randint(30,70),random.randint(30,70))

        zeros[center[0],center[1],center[2]] = 1
        dilated_mask = binary_dilation(zeros, iterations=1, structure=np.ones((10,10,10)))

        ## get cosine mask
        cosine_mask = smoothen_mask(dilated_mask, cosine_falloff_length=3)

        ## test that the cosine mask is the same size as the original mask
        self.assertEqual(cosine_mask.shape, zeros.shape)
        unique_vals_cosine = np.unique(cosine_mask.flatten())
        self.assertTrue(len(unique_vals_cosine) > 2)

if __name__ == '__main__':
    unittest.main()
       

       











            

