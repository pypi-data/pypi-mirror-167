
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

class test_pdb_shake(unittest.TestCase):
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
        
    def test_shake_pdb(self):
        from emmer.pdb.pdb_tools.perturb_within_mask import perturb_within_mask
        from emmer.pdb.pdb_tools.compute_rmsd_two_pdb import compute_rmsd_two_pdb
        from emmer.ndimage.mask.get_atomic_model_mask import get_atomic_model_mask
        from emmer.ndimage.map_utils import save_as_mrc

        pdb_path = self.pdb_path
        sample_emmap_path = self.emmap_path

        ## create temporary directory
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as tmpdir:
            copied_pdb_path = self.copy_files(pdb_path, tmpdir)
            copied_sample_emmap_path = self.copy_files(sample_emmap_path, tmpdir)

            ## get atomic model mask
            emmap = mrcfile.open(copied_sample_emmap_path)
            model_mask = get_atomic_model_mask(emmap=emmap.data, apix=emmap.voxel_size.x, pdb_path=copied_pdb_path, dilation_radius=3, softening_parameter=5)
            save_as_mrc(model_mask, os.path.join(tmpdir,'model_mask.mrc'),apix=1.2156)
            model_mask_path = os.path.join(tmpdir,'model_mask.mrc')
            ## shake pdb within mask
            for trial in range(5):
                rmsd_mag = np.random.uniform(low=5, high=25)
                shaken_pdb = perturb_within_mask(copied_pdb_path, model_mask_path, rmsd_magnitude=rmsd_mag)

                RMSD_shake = compute_rmsd_two_pdb(copied_pdb_path, shaken_pdb)

                percentage_rmsd_difference = abs(RMSD_shake-rmsd_mag)/rmsd_mag*100
                
                self.assertLess(percentage_rmsd_difference, 15)

        

        
        

       
        

      


      