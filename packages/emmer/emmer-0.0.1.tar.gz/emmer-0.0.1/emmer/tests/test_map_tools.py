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

class test_map_tools(unittest.TestCase):
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
        


    def test_atomic_model_mask(self):
        ## shake pdb within mask at 2A resolution
        from emmer.pdb.pdb_tools.perturb_within_mask import perturb_within_mask
        from emmer.pdb.pdb_utils import get_all_atomic_positions
        from emmer.ndimage.mask.get_atomic_model_mask import get_atomic_model_mask
        from emmer.pdb.convert.convert_pdb_to_mrc_position import convert_pdb_to_mrc_position
        from emmer.ndimage.map_utils import load_map
        pdb_path = self.pdb_path
        sample_emmap_path = self.emmap_path

        ## create temporary directory
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as tmpdir:
            copied_pdb_path = self.copy_files(pdb_path, tmpdir)
            copied_sample_emmap_path = self.copy_files(sample_emmap_path, tmpdir)
            emmap, apix = load_map(copied_sample_emmap_path)

            ## get atomic model mask
            model_mask = get_atomic_model_mask(emmap=emmap, apix=1.2156,pdb_path=copied_pdb_path, dilation_radius=3, softening_parameter=5)
            binarised = (model_mask > 0.5).astype(np.int_)
            pdb_positions = get_all_atomic_positions(copied_pdb_path)
            mrc_positions = convert_pdb_to_mrc_position(pdb_positions, apix=1.2156)

            count = 0
            for mrc in mrc_positions:
                count += binarised[mrc[0],mrc[1],mrc[2]]
            
            num_atoms = len(pdb_positions)
            capture = count/num_atoms * 100
     
            self.assertTrue(capture > 99)


    def test_trim_map_between_residues(self):
        ## shake pdb within mask at 2A resolution
        from emmer.ndimage.trim_map_between_residues import trim_map_between_residues
        from emmer.ndimage.map_utils import load_map, save_as_mrc
        
        pdb_path = self.pdb_path
        sample_emmap_path = self.emmap_path


        ## create temporary directory
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as tmpdir:
            copied_pdb_path = self.copy_files(pdb_path, tmpdir)
            copied_sample_emmap_path = self.copy_files(sample_emmap_path, tmpdir)
            emmap, _ = load_map(copied_sample_emmap_path)

            ## crop map between residues 
            chain_name = "B"
            residue_range = [378,383]

            cropped_map = trim_map_between_residues(copied_sample_emmap_path, copied_pdb_path, chain_name, residue_range)

            cropped_map_target = self.validate['map_tools_output']['cropped_map']

            self.assertTrue(np.allclose(cropped_map, cropped_map_target))

    def test_confidence_map(self):
        from emmer.ndimage.map_tools import measure_mask_parameters
        from emmer.ndimage.mask.compute_confidence_map import compute_confidence_map
        from emmer.ndimage.map_utils import load_map
        from emmer.ndimage.compute_real_space_correlation import compute_real_space_correlation
        sample_emmap_path = self.emmap_path
        sample_mask_path = self.mask_path
        ## create temporary directory
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as tmpdir:
            copied_sample_emmap_path = self.copy_files(sample_emmap_path, tmpdir)
            copied_sample_mask_path = self.copy_files(sample_mask_path, tmpdir)
            emmap, _ = load_map(copied_sample_emmap_path)

            ## compute confidence map
            confidence_map = compute_confidence_map(emmap, apix=1.2156, window_size=25, fdr=0.01)
           
            confidence_map_target,_ = load_map(copied_sample_mask_path)
            rscc = compute_real_space_correlation(confidence_map, confidence_map_target)

            self.assertTrue(rscc > 0.8)            

            mask_parameters = measure_mask_parameters(mask=confidence_map, apix=1.2156, detailed_report=True)
            
            self.assertTrue(mask_parameters[2]==41926)

    def test_resample_map(self):
        from emmer.ndimage.map_tools import resample_map
        from emmer.ndimage.map_utils import load_map
        
        sample_emmap_path = self.emmap_path

        ## create temporary directory
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as tmpdir:
            copied_sample_emmap_path = self.copy_files(sample_emmap_path, tmpdir)
            emmap, apix = load_map(copied_sample_emmap_path)

            resampled_map = resample_map(emmap, apix=1.2156, apix_new=1.0)



            self.assertTrue(resampled_map.shape == (311,311,311))
            self.assertAlmostEqual(resampled_map.mean(),emmap.mean(), delta=1e-5)
            self.assertAlmostEqual(resampled_map.std(),emmap.std(), delta=1e-4)
    
    def test_resample_image(self):
        from emmer.ndimage.map_tools import resample_image
        from emmer.ndimage.map_utils import load_map
        
        sample_emmap_path = self.emmap_path

        ## create temporary directory
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as tmpdir:
            copied_sample_emmap_path = self.copy_files(sample_emmap_path, tmpdir)
            emmap, apix = load_map(copied_sample_emmap_path)

            resampled_map = resample_image(emmap, apix=1.2156, apix_new=1.0)



            self.assertTrue(resampled_map.shape == (311,311,311))
            self.assertAlmostEqual(resampled_map.mean(),emmap.mean(), delta=1e-4)
            self.assertAlmostEqual(resampled_map.std(),emmap.std(), delta=1e-3)
    
    def test_add_half_maps(self):
        from emmer.ndimage.average_half_maps import average_half_maps
        from emmer.ndimage.map_utils import load_map, save_as_mrc
        import os

        ## create temporary directory
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as tmpdir:
            
            random_map_1 = np.random.uniform(0,1,(256,256,256))
            random_map_2 = np.random.uniform(0,1,(256,256,256))

            save_as_mrc(random_map_1, os.path.join(tmpdir,'temp_1.mrc'), apix=1)
            save_as_mrc(random_map_2, os.path.join(tmpdir,'temp_2.mrc'), apix=1)

            full_map_path = average_half_maps(os.path.join(tmpdir,'temp_1.mrc'), os.path.join(tmpdir,'temp_2.mrc'), output_filename=os.path.join(tmpdir,'temp_full.mrc'))
            
            full_map, apix = load_map(full_map_path)
            self.assertTrue(os.path.exists(full_map_path))
            self.assertTrue(full_map.shape == random_map_1.shape)
            self.assertAlmostEqual(full_map.mean(),np.mean(np.array([random_map_1.mean(),random_map_2.mean()])), delta=1e-5)

            


            


        
        
