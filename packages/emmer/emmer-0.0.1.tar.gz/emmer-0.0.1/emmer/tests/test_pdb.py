# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 15:35:54 2021

@author: mjoosten1
"""

# test file for functions in the pdb section of emmer.

# global imports
import unittest
import gemmi
import numpy as np
import os

class test_pdb_functions(unittest.TestCase):
    def setUp(self):
        import emmer
        
        emmer_module_path = os.path.dirname(emmer.__file__)
        emmer_install_path = emmer_module_path
        self.emmer_install_path = emmer_install_path

        os.sys.path.insert(0, self.emmer_install_path)
        
        # locate data used in tests
        data_path = "/tests/pdb_unittest/data/"
        self.pdb_path = self.emmer_install_path+data_path+"testing_model.pdb"
        self.model_with_nucleotides = self.emmer_install_path+data_path+"6NY1.pdb"
        self.charged_model = self.emmer_install_path+data_path+"charged.pdb"
        self.no_cryst1_line = self.emmer_install_path+data_path+"no_cryst1_line.pdb"
        self.pdb_gemmi = gemmi.read_structure(self.pdb_path)
        
        # locate data for verification of test results
        verify_path = "/tests/pdb_unittest/verify/"
        self.verify_emmap_path = self.emmer_install_path+verify_path+"verify_map.mrc"
        self.verify_emmap_gemmi = gemmi.read_ccp4_map(self.verify_emmap_path)
        self.verify_cif = self.emmer_install_path+verify_path+"testing_model.cif"    
        self.verify_shifted = self.emmer_install_path+verify_path+"shifted_model.pdb"
        self.verify_ca_coords = self.emmer_install_path+verify_path+"ca_coords.npy"
        self.verify_all_coords = self.emmer_install_path+verify_path+"all_coords.npy"

    def test_convert_pdb_to_map(self):
        from emmer.pdb.convert.convert_pdb_to_map import convert_pdb_to_map

        temp_map_from_model, temp_grid = convert_pdb_to_map(input_pdb=self.pdb_path,
                                  size=(48,96,48),
                                  return_grid=True)
        
        map_equal_size = temp_map_from_model.shape == self.verify_emmap_gemmi.grid.shape
        m1, m2 = temp_map_from_model.mean(), np.array(self.verify_emmap_gemmi.grid).mean()
        s1, s2 = temp_map_from_model.std(), np.array(self.verify_emmap_gemmi.grid).std()
        CCC = ((np.rot90(np.flip(temp_map_from_model,axis=2), axes=(0,2)) - m1)*(np.array(self.verify_emmap_gemmi.grid) - m2)/(s1*s2)).sum() / temp_map_from_model.size
        
        self.assertTrue(map_equal_size)
        self.assertAlmostEqual(temp_map_from_model.mean(), np.array(self.verify_emmap_gemmi.grid).mean(), delta=1e-5)
        self.assertAlmostEqual(temp_map_from_model.min(), np.array(self.verify_emmap_gemmi.grid).min(), delta=1e-5)
        self.assertAlmostEqual(temp_map_from_model.max(), np.array(self.verify_emmap_gemmi.grid).max(), delta=1e-5)
        self.assertAlmostEqual(temp_map_from_model.std(), np.array(self.verify_emmap_gemmi.grid).std(), delta=1e-5)
        self.assertAlmostEqual(CCC, 1, delta=1e-3)

    def test_convert_pdb_to_mmcif(self):
        from emmer.pdb.convert import convert_pdb_to_mmcif
        
        convert_pdb_to_mmcif.convert_pdb_to_mmcif(self.pdb_path)
        test_cif = gemmi.read_structure(self.pdb_path[:-4]+".cif")
        verify_cif = gemmi.read_structure(self.verify_cif)
        
        tM = test_cif[0]
        vM = verify_cif[0]        
        tCoM = tM.calculate_center_of_mass()
        vCoM = vM.calculate_center_of_mass()
        
        self.assertEqual(tM.count_atom_sites(), vM.count_atom_sites())
        self.assertEqual(tCoM.x, vCoM.x)
        self.assertEqual(tCoM.y, vCoM.y)
        self.assertEqual(tCoM.z, vCoM.z)
                
        # remove generated file
        os.remove(self.pdb_path[:-4]+".cif")
        
    def test_check_if_gemmi_st_is_downloadable(self):
        from emmer.pdb.pdb_utils import check_if_gemmi_st_is_downloadable

        self.assertTrue(check_if_gemmi_st_is_downloadable('3j5p'))
        self.assertTrue(check_if_gemmi_st_is_downloadable('5vy5'))
        
    def test_get_gemmi_st_from_id(self):
        from emmer.pdb.pdb_utils import get_gemmi_st_from_id
        
        tmp_gemmi = get_gemmi_st_from_id('3j5p')
        self.assertEqual(tmp_gemmi[0].count_atom_sites(), 18636)
        
        tmp_gemmi = get_gemmi_st_from_id('5vy5')
        self.assertEqual(tmp_gemmi[0].count_atom_sites(), 10472)

    def test_shift_coordinates(self):
        from emmer.pdb.pdb_utils import shift_coordinates
        
        outfile = self.emmer_install_path+"/tests/pdb_unittest/data/tmp_shifted_model.pdb"
        st=shift_coordinates(input_pdb=self.pdb_path, trans_matrix=[3,3,3])
        st.write_pdb(outfile)
        ftest = open(outfile)
        lnstest = ftest.readlines()
        ftest.close()
        fverify = open(self.verify_shifted)
        lnsverify = fverify.readlines()
        fverify.close()
        shift_correct = True
        for ln in range(len(lnstest)):
            if 'ATOM' in lnstest[ln]:
                if lnstest[ln] != lnsverify[ln]:
                    shift_correct = False
                    
        self.assertTrue(shift_correct)

        os.remove(outfile)
        
    def test_split_model_based_on_nucleotides(self):
        from emmer.pdb.pdb_utils import split_model_based_on_nucleotides
        
        model_with_nucleotides = gemmi.read_structure(self.model_with_nucleotides)
        split_model = split_model_based_on_nucleotides(model_with_nucleotides)
        
        self.assertEqual(split_model[0][0].count_atom_sites(), 940)
        self.assertEqual(split_model[1][0].count_atom_sites(), 2300)

    def test_get_bfactors(self):
        from emmer.pdb.pdb_utils import get_bfactors
        
        B = get_bfactors(input_pdb=self.pdb_path)
        self.assertEqual(len(B), 125)
        
        bfac_correct = True
        for i in B:
            if i!=30:
                bfac_correct = False

        self.assertTrue(bfac_correct)
        
    def test_add_atomic_bfactors(self):
        from emmer.pdb.pdb_utils import add_atomic_bfactors
        
        outfile = self.emmer_install_path+"/tests/pdb_unittest/data/tmp_addBfac_model.pdb"
        st=add_atomic_bfactors(input_pdb=self.pdb_path, additional_biso=100)
        st.write_pdb(outfile)
        
        fid = open(outfile)
        lns = fid.readlines()
        fid.close()
        bfac_correct = True
        for ln in lns:
            if ln[:4] == "ATOM":
                if ln[60:66]!="130.00":
                    bfac_correct = False
        
        self.assertTrue(bfac_correct)
        
        os.remove(outfile)
        
    def test_set_atomic_bfactors(self):
        from emmer.pdb.pdb_utils import set_atomic_bfactors

        outfile = self.emmer_install_path+"/tests/pdb_unittest/data/tmp_setBfac_model.pdb"
        st=set_atomic_bfactors(input_pdb=self.pdb_path, b_iso=100)
        st.write_pdb(outfile)
        fid = open(outfile)
        lns = fid.readlines()
        fid.close()
        bfac_correct = True
        for ln in lns:
            if ln[:4] == "ATOM":
                if ln[60:66]!="100.00":
                    bfac_correct = False
       
        self.assertTrue(bfac_correct)

        os.remove(outfile)
    
    def test_get_residue_ca_coordinates(self):
        from emmer.pdb.pdb_utils import get_residue_ca_coordinates
        
        ca_coords = get_residue_ca_coordinates(self.pdb_path)
        verify_coords = np.load(self.verify_ca_coords, allow_pickle=True)
        coords_are_equal = (ca_coords!=verify_coords).sum() == 0

        self.assertTrue(coords_are_equal)
        
    def test_get_coordinates(self):
        from emmer.pdb.pdb_utils import get_coordinates
        
        coords = get_coordinates(self.pdb_path)
        verify_coords = np.load(self.verify_all_coords, allow_pickle=True)
        coords_are_equal = (coords!=verify_coords).sum() == 0
         
        self.assertTrue(coords_are_equal)

    def test_remove_atomic_charges(self):
        from emmer.pdb.pdb_utils import remove_charges
        
        outfile = self.emmer_install_path+"/tests/pdb_unittest/data/tmp_nocharge_model.pdb"
        st=remove_charges(self.charged_model)
        st.write_pdb(outfile)
        uncharged_gemmi = gemmi.read_structure(outfile)
        charge_removed_correct = True
        for mdl in uncharged_gemmi:
            for chn in mdl:
                for res in chn:
                    for atm in res:
                        if atm.charge != 0: charge_removed_correct = False
                        
        self.assertTrue(charge_removed_correct)      
        
        os.remove(outfile)
        
    def test_add_cryst1_line(self):
        from emmer.pdb.pdb_tools.add_cryst1_line import add_cryst1_line

        outfile = self.emmer_install_path+"/tests/pdb_unittest/data/tmp_addcryst1_model.pdb"
        add_cryst1_line(pdb_path=self.no_cryst1_line, unitcell=(12,12,12), new_pdb_path=outfile)
        fid = open(outfile)
        lns = fid.readlines()
        fid.close()
        cryst_line_present = False
        cryst_line_correct = False
        for ln in lns:
            if "CRYST1" in ln:
                cryst_line_present = True
                if ln[9:15]=='12.000' and ln[18:24]=='12.000' and ln[27:33]=='12.000':
                    cryst_line_correct = True
                
        self.assertTrue(cryst_line_present)
        self.assertTrue(cryst_line_correct)                
        
        os.remove(outfile)
        
    def test_set_to_center_of_unit_cell(self):
        from emmer.pdb.pdb_utils import set_to_center_of_unit_cell
        
        unit_cell = gemmi.UnitCell(100,100,100,90,90,90)
        centered_gemmi = set_to_center_of_unit_cell(self.pdb_gemmi, unit_cell)
        
        CoM = centered_gemmi[0].calculate_center_of_mass()
        
        self.assertAlmostEqual(CoM.x, 50, delta=1e-5)
        self.assertAlmostEqual(CoM.y, 50, delta=1e-5)        
        self.assertAlmostEqual(CoM.z, 50, delta=1e-5)
        
        num_total_atoms = 0
        for mdl in centered_gemmi:
            num_total_atoms += mdl.count_atom_sites()

        atmidx = 0
        pos = np.zeros((num_total_atoms,3))
        for mdl in centered_gemmi:
            for chn in mdl:
                for res in chn:
                    for atm in res:
                        pos[atmidx,:] = [atm.pos.x, atm.pos.y, atm.pos.z]
                        atmidx += 1
        
        self.assertAlmostEqual(pos.max(axis=0)[0], 54, delta=1)
        self.assertAlmostEqual(pos.max(axis=0)[1], 69, delta=1)
        self.assertAlmostEqual(pos.max(axis=0)[2], 54, delta=1)
        
# =============================================================================
#     def test_get_unit_cell_estimate(self):
#         from emmer.pdb.pdb_tools import get_unit_cell_estimate
#         
#         ucell_estimate = get_unit_cell_estimate(self.pdb_gemmi, 0.65)
#         self.assertTrue(ucell_estimate.a, 1.5556)
#         
# =============================================================================
    def test_find_radius_of_gyration(self):
        from emmer.pdb.pdb_utils import find_radius_of_gyration
        
        RoG = find_radius_of_gyration(self.pdb_path)
        
        self.assertEqual(RoG, 24.539793074376302)
        
if __name__ == '__main__':
    unittest.main()

