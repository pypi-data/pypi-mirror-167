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

class test_fsc_tools(unittest.TestCase):
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
        


    def test_compute_fsc(self):
        ## shake pdb within mask at 2A resolution
        from emmer.pdb.pdb_tools.perturb_within_mask import perturb_within_mask
        from emmer.ndimage.fsc.calculate_fsc_curve import calculate_fsc_curve
        from emmer.ndimage.mask.get_atomic_model_mask import get_atomic_model_mask
        from emmer.ndimage.map_utils import load_map, save_as_mrc
        from emmer.ndimage.radial_profile.frequency_array import frequency_array
        from emmer.ndimage.radial_profile.profile_tools import get_index_at_resolution
        from emmer.pdb.convert.convert_pdb_to_map import convert_pdb_to_map
        import matplotlib.pyplot as plt
        
        pdb_path = self.pdb_path
        sample_emmap_path = self.emmap_path

        ## create temporary directory
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as tmpdir:
            copied_pdb_path = self.copy_files(pdb_path, tmpdir)
            copied_sample_emmap_path = self.copy_files(sample_emmap_path, tmpdir)

            ## get atomic model mask
            emmap, apix = load_map(copied_sample_emmap_path)
            model_mask = get_atomic_model_mask(emmap=emmap, apix=apix,pdb_path=copied_pdb_path, dilation_radius=3, softening_parameter=5)
            save_as_mrc(model_mask, os.path.join(tmpdir,'model_mask.mrc'),apix=1.2156)
            model_mask_path = os.path.join(tmpdir,'model_mask.mrc')
            ## shake pdb within mask

            rmsd_mag = np.random.uniform(low=2, high=5)
            shaken_pdb_path_1 = perturb_within_mask(copied_pdb_path, model_mask_path, rmsd_magnitude=rmsd_mag)
            shaken_pdb_path_2 = perturb_within_mask(copied_pdb_path, model_mask_path, rmsd_magnitude=rmsd_mag)

            ## simulate model map
            model_map_1 = convert_pdb_to_map(input_pdb=shaken_pdb_path_1, apix=1.2156, size=(256,256,256))
            model_map_2 = convert_pdb_to_map(input_pdb=shaken_pdb_path_2, apix=1.2156, size=(256,256,256))

            ## calculate fsc maps
            fsc_maps = calculate_fsc_curve(model_map_1, model_map_2)
            freq = frequency_array(fsc_maps, apix=1.2156)
            
            fsc_index = get_index_at_resolution(freq, rmsd_mag)

            fsc_0 = fsc_maps[0]
            fsc_rmsd = fsc_maps[fsc_index]

            self.assertTrue(fsc_0 > fsc_rmsd)
            self.assertAlmostEqual(fsc_0, 1, delta=0.01)

    def test_apply_fsc_filter(self):
        ## shake pdb within mask at 2A resolution
        from emmer.pdb.pdb_tools.perturb_within_mask import perturb_within_mask
        from emmer.ndimage.fsc.calculate_fsc_curve import calculate_fsc_curve
        from emmer.ndimage.filter.apply_fsc_filter import apply_fsc_filter
        from emmer.ndimage.mask.get_atomic_model_mask import get_atomic_model_mask
        from emmer.ndimage.map_utils import load_map, save_as_mrc
        from emmer.ndimage.radial_profile.frequency_array import frequency_array
        from emmer.ndimage.radial_profile.profile_tools import get_index_at_resolution
        from emmer.ndimage.radial_profile.compute_radial_profile import compute_radial_profile
        from emmer.pdb.convert.convert_pdb_to_map import convert_pdb_to_map
        import matplotlib.pyplot as plt
        
        pdb_path = self.pdb_path
        sample_emmap_path = self.emmap_path

        ## create temporary directory
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as tmpdir:
            copied_pdb_path = self.copy_files(pdb_path, tmpdir)
            copied_sample_emmap_path = self.copy_files(sample_emmap_path, tmpdir)
            emmap, apix = load_map(copied_sample_emmap_path)

            ## get atomic model mask
            model_mask = get_atomic_model_mask(emmap=emmap, apix=apix,pdb_path=copied_pdb_path, dilation_radius=3, softening_parameter=5)
            save_as_mrc(model_mask, os.path.join(tmpdir,'model_mask.mrc'),apix=1.2156)
            model_mask_path = os.path.join(tmpdir,'model_mask.mrc')
            ## shake pdb within mask

            rmsd_mag = np.random.uniform(low=2, high=5)
            shaken_pdb_path_1 = perturb_within_mask(copied_pdb_path, model_mask_path, rmsd_magnitude=rmsd_mag)
            shaken_pdb_path_2 = perturb_within_mask(copied_pdb_path, model_mask_path, rmsd_magnitude=rmsd_mag)

            ## simulate model map
            model_map_1 = convert_pdb_to_map(input_pdb=shaken_pdb_path_1, apix=1.2156, size=(256,256,256))
            model_map_2 = convert_pdb_to_map(input_pdb=shaken_pdb_path_2, apix=1.2156, size=(256,256,256))

            fsc_filtered_emmap = apply_fsc_filter(emmap, apix=1.2156, halfmap_1=model_map_1, halfmap_2=model_map_2)

            rp_emmap = compute_radial_profile(emmap)
            rp_fsc_filtered_emmap = compute_radial_profile(fsc_filtered_emmap)
            freq = frequency_array(rp_emmap, apix=1.2156)

            rmsd_index = get_index_at_resolution(freq, rmsd_mag)

            rp_emmap_0 = rp_emmap[0]
            rp_fsc_filtered_emmap_0 = rp_fsc_filtered_emmap[0]

            rp_emmap_rmsd = rp_emmap[rmsd_index]
            rp_fsc_filtered_emmap_rmsd = rp_fsc_filtered_emmap[rmsd_index]

            self.assertTrue(rp_emmap_rmsd > rp_fsc_filtered_emmap_rmsd)
            self.assertAlmostEqual(rp_emmap_0, rp_fsc_filtered_emmap_0, delta=0.001)
       





            


        
        
