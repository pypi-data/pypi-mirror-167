
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

class test_dssp(unittest.TestCase):
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
        
    def test_secondary_structure_distribution(self):
        from emmer.pdb.pdb_utils import replace_pdb_column_with_arrays, detect_pdb_input
        from emmer.pdb.SSE.get_secondary_structure_residues_content import get_secondary_structure_residues_content

        pdb_path = self.pdb_path
        pdbid="3j5p"

        secondary_structures,secondary_structure_distribution = get_secondary_structure_residues_content(pdbid, pdb_path)

        self.assertAlmostEqual(secondary_structure_distribution['helix'], 0.62, delta=1e-2)
        self.assertAlmostEqual(secondary_structure_distribution['sheet'], 0.03, delta=1e-2)
        self.assertAlmostEqual(secondary_structure_distribution['loop'], 0.16, delta=1e-2)
        self.assertTrue(secondary_structure_distribution['total']==1008)

    def test_split_gemmi_model_based_on_dssp(self):
        from emmer.pdb.pdb_utils import detect_pdb_input
        from emmer.pdb.SSE.split_gemmi_model_based_on_dssp import split_gemmi_model_based_on_dssp

        pdb_path = self.pdb_path
        pdbid="3j5p"

        helix_model, sheet_model, RESIDUE_SKIPPED_STAT = split_gemmi_model_based_on_dssp(pdbid, pdb_path)

        self.assertAlmostEqual(helix_model.count_atom_sites(), 5068, delta=3)
        self.assertAlmostEqual(sheet_model.count_atom_sites(), 227, delta=3)
        self.assertTrue(RESIDUE_SKIPPED_STAT[1]==1008)
        

      


      