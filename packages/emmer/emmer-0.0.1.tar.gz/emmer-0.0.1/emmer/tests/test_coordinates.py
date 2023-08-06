
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

class test_coordinate_functions(unittest.TestCase):
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
        
    def test_coordinate_functions(self):
        from emmer.pdb.convert.convert_polar_to_cartesian import convert_polar_to_cartesian
        from emmer.pdb.convert.convert_mrc_to_pdb_position import convert_mrc_to_pdb_position
        from emmer.pdb.convert.convert_pdb_to_mrc_position import convert_pdb_to_mrc_position
        
        from scipy.spatial import distance

        rmsd_magnitude=15
        
        for trial in range(1000):
            pos = np.random.uniform(0,500,size=3)
            r = np.random.uniform(0, rmsd_magnitude*2)
            shake_thetas = np.random.uniform(0, 2*np.pi)
            shake_phis = np.random.uniform(0, np.pi)
            shake_vector = np.column_stack((r, shake_thetas, shake_phis))
            shake_v = shake_vector[0]
            new_pos = pos+convert_polar_to_cartesian(shake_v)
            d = distance.euclidean(new_pos, pos)
            self.assertTrue(abs(d-r)<0.01)

        
        for i in range(1000):
            apix = np.random.uniform(0.1,2)
            pos = np.random.uniform(0,500,size=3)
            mrcpos = convert_pdb_to_mrc_position([pos],apix)[0]
            pdbpos = convert_mrc_to_pdb_position([mrcpos],apix)[0]
            d = distance.euclidean(pdbpos, pos)
            self.assertTrue(abs(d)<apix)
            
              
        

        
        

       
        

      


      