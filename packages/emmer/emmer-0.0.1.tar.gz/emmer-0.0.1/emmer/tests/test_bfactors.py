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

class test_bfactor_tools(unittest.TestCase):
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
        


    def test_estimate_bfactor_map(self):
        ## shake pdb within mask at 2A resolution
        from emmer.ndimage.bfactors.estimate_bfactor_map import estimate_bfactor_map
        from emmer.ndimage.map_utils import load_map
        sample_emmap_path = self.emmap_path

        ## create temporary directory
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as tmpdir:
            copied_sample_emmap_path = self.copy_files(sample_emmap_path, tmpdir)

            bfactor, fit = estimate_bfactor_map(copied_sample_emmap_path, wilson_cutoff=10, fsc_cutoff=3.4, return_fit=True)

            self.assertAlmostEqual(bfactor, -215, delta=10)
            self.assertGreater(fit.r_squared(), 0.99)
                
           
    def test_estimate_local_bfactor_map(self):
        from emmer.ndimage.bfactors.estimate_local_bfactor import estimate_local_bfactor
        from emmer.ndimage.map_utils import load_map
        
        sample_emmap_path = self.emmap_path

        ## create temporary directory
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as tmpdir:
            copied_sample_emmap_path = self.copy_files(sample_emmap_path, tmpdir)

            bfactor, fit = estimate_local_bfactor(copied_sample_emmap_path, center=(180,179,120), wilson_cutoff=10, fsc_cutoff=3.4, boxsize=22, standard_notation=True, return_fit_quality=True)
            
            self.assertAlmostEqual(bfactor, 95, delta=5)
            self.assertAlmostEqual(fit, 0.89, delta=0.01)
    
    
    def test_bfactor_distribution(self):
        from emmer.ndimage.bfactors.estimate_bfactor_distribution import estimate_bfactor_distribution
        from emmer.ndimage.map_utils import load_map
        
        sample_emmap_path = self.emmap_path
        
        ## create temporary directory
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as tmpdir:
            copied_sample_emmap_path = self.copy_files(sample_emmap_path, tmpdir)
            
            emmap,_ = load_map(copied_sample_emmap_path)
            binarised_mask = (emmap >= 0.01).astype(int)

            bfactor_distribution = estimate_bfactor_distribution(copied_sample_emmap_path, binarised_mask, wilson_cutoff=10,fsc_cutoff=3.4, boxsize=22, standard_notation=True)

            bfactors = np.array([x[0] for x in bfactor_distribution.values()])
            qfit = np.array([x[1] for x in bfactor_distribution.values()])

            self.assertAlmostEqual(bfactors.mean(), 178 , delta=10)
            self.assertAlmostEqual(qfit.mean(), 0.95 , delta=0.01)


