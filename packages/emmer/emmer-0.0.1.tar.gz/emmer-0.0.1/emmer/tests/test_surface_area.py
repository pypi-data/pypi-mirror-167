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

class test_contour_tools(unittest.TestCase):
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
        


    def test_surface_area_threshold(self):
        ## shake pdb within mask at 2A resolution
        from emmer.ndimage.contour.surface_area_at_threshold import surface_area_at_threshold
        from emmer.ndimage.map_utils import load_map
        
        sample_emmap_path = self.emmap_path

        ## create temporary directory
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as tmpdir:
            copied_sample_emmap_path = self.copy_files(sample_emmap_path, tmpdir)
            emmap,_ = load_map(copied_sample_emmap_path)
            ref_threshold_1 = 0.005
            ref_threshold_2 = 0.01

            ref_area_1 = 134.4e3 ## from chimeraX  in A^2
            ref_area_2 = 72.44e3  ## from chimeraX in A^2

            ## get surface area threshold
            surface_area_1 = surface_area_at_threshold(emmap, apix=1.2156, reference_threshold=ref_threshold_1)
            surface_area_2 = surface_area_at_threshold(emmap, apix=1.2156, reference_threshold=ref_threshold_2)

            surface_area_relative_difference_1 = abs(surface_area_1 - ref_area_1)/ref_area_1
            surface_area_relative_difference_2 = abs(surface_area_2 - ref_area_2)/ref_area_2

            self.assertLess(surface_area_relative_difference_1, 0.15)
            self.assertLess(surface_area_relative_difference_2, 0.15) 
    
    def test_count_number_of_segments(self):
        from emmer.ndimage.contour.count_segments import count_segments
        from emmer.ndimage.map_utils import load_map
        
        sample_emmap_path = self.emmap_path

        ## create temporary directory
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as tmpdir:
            copied_sample_emmap_path = self.copy_files(sample_emmap_path, tmpdir)
            emmap,_ = load_map(copied_sample_emmap_path)
            ref_threshold = 0.01
            ref_num_regions = 5

            ## get number of segments
            num_regions = count_segments(emmap, reference_threshold=ref_threshold)

            self.assertEqual(num_regions, ref_num_regions)
    
    def test_volume_at_threshold(self):
        from emmer.ndimage.contour.volume_at_threshold import volume_at_threshold
        from emmer.ndimage.map_utils import load_map
        
        sample_emmap_path = self.emmap_path

        ## create temporary directory
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as tmpdir:
            copied_sample_emmap_path = self.copy_files(sample_emmap_path, tmpdir)
            emmap,apix = load_map(copied_sample_emmap_path)
            ref_threshold = 0.01
            ref_volume = 96.5e3 ## from chimeraX in A^3 (approx)

            ## get volume at threshold
            volume = volume_at_threshold(emmap, apix, reference_threshold=ref_threshold)

            error = abs(volume - ref_volume)/ref_volume

            self.assertLess(error, 0.05)
    
    def test_volume_matching_threshold(self):
        from emmer.ndimage.contour.volume_matching_threshold import volume_matching_threshold
        from emmer.ndimage.map_utils import load_map
        
        sample_emmap_path = self.emmap_path

        ## create temporary directory
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as tmpdir:
            copied_sample_emmap_path = self.copy_files(sample_emmap_path, tmpdir)
            emmap,apix = load_map(copied_sample_emmap_path)
            ref_threshold = 0.01210
            ref_volume = 70e3

            ## get volume at threshold
            threshold = volume_matching_threshold(emmap, apix, reference_volume=ref_volume, min_threshold=0.01, max_threshold=0.03, num_bins=20)

            self.assertAlmostEqual(threshold, ref_threshold, delta=0.01)





    
        

            
    

       

       











            

