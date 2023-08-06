#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 11:30:49 2021

@author: alok
"""

import unittest
import gemmi
import mrcfile
import numpy as np
import os

class test_profile_tools_functions(unittest.TestCase):
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
        
    
    def test_frequency_array(self):
        from emmer.ndimage.radial_profile.frequency_array import frequency_array
        apix_test = np.random.uniform(low=0.5,high=2.5)
        length = np.random.randint(low=100, high=1000)
        
        
        ## Tests based on saved dataset
        
        freq_test = frequency_array(n=length, apix=apix_test)
        
        self.assertAlmostEqual(freq_test[0], 1/(apix_test*length), delta=1e-6)
        self.assertAlmostEqual(freq_test[-1], 1/(apix_test*2), delta=1e-6)
    
    def test_compute_radial_profile(self):
        from emmer.ndimage.radial_profile.frequency_array import frequency_array
        from emmer.ndimage.radial_profile.compute_radial_profile import compute_radial_profile
        
        emmap= mrcfile.open(self.emmap_path).data
        modmap = mrcfile.open(self.modmap_path).data
        
        rp_emmap_test = compute_radial_profile(emmap)
        rp_modmap_test = compute_radial_profile(modmap)
        
        freq = frequency_array(rp_emmap_test, 1.2156)
        
        rp_emmap_target = self.validate['profile_tools_output']['rp_emmap']
        rp_modmap_target = self.validate['profile_tools_output']['rp_modmap']
        
        self.assertTrue((rp_emmap_test==rp_emmap_target).any())
        self.assertTrue((rp_modmap_test==rp_modmap_target).any())
    
    def test_match_bfactors(self):
        from emmer.ndimage.radial_profile.frequency_array import frequency_array
        from emmer.ndimage.radial_profile.compute_radial_profile import compute_radial_profile
        from emmer.ndimage.radial_profile.scale_profiles import scale_profiles

        emmap= mrcfile.open(self.emmap_path).data
        modmap = mrcfile.open(self.modmap_path).data
        
        rp_emmap_test = compute_radial_profile(emmap)
        rp_modmap_test = compute_radial_profile(modmap)
        freq = frequency_array(rp_emmap_test, 1.2156)

        freq_match, scaled_amplitude = scale_profiles((freq, rp_emmap_test), 
                                                    (freq, rp_modmap_test), 
                                                    wilson_cutoff=4.7, fsc_cutoff=3.4)
        
        amp_match_target = self.validate['profile_tools_output']['amp_matched']
        sr=abs(scaled_amplitude/amp_match_target)
        
        self.assertTrue(np.allclose(sr, np.ones(len(sr)), atol=0.2))
        self.assertTrue(np.allclose(freq_match, freq))
       
    
   
    def test_bfactor_and_resample(self):
        from emmer.ndimage.radial_profile.compute_radial_profile import compute_radial_profile
        from emmer.ndimage.radial_profile.frequency_array import frequency_array
        from emmer.ndimage.radial_profile.estimate_bfactor_standard import estimate_bfactor_standard
        from emmer.ndimage.radial_profile.estimate_bfactor_pwlf import estimate_bfactor_pwlf
        emmap= mrcfile.open(self.emmap_path).data
        rp_emmap_test = compute_radial_profile(emmap)
        freq = frequency_array(rp_emmap_test, 1.2156)
        bfactor_std_test = estimate_bfactor_standard(freq, rp_emmap_test, wilson_cutoff=4.7, fsc_cutoff=3.4)
        bfactor_pwlf_test, dc_amp, (fit, z, slope) = estimate_bfactor_pwlf(freq, rp_emmap_test, wilson_cutoff=9,fsc_cutoff=3.4, num_segments=3) 
                                                                      
        
        from emmer.ndimage.radial_profile.profile_tools import resample_1d
        resampled_rp_test = resample_1d(freq, rp_emmap_test, num=1000, xlims=[1/9,1/3.4])
        
      
        self.assertTrue((resampled_rp_test[1]==self.validate['profile_tools_output']['resampled_profile'][1]).any())
        self.assertAlmostEqual(bfactor_std_test,self.validate['profile_tools_output']['bfactor_std'],delta=10)
        self.assertAlmostEqual(bfactor_pwlf_test,self.validate['profile_tools_output']['bfactor_pwlf'], delta=10)
    
    def test_crop_profile_between_resolution(self):
        from emmer.ndimage.radial_profile.profile_tools import crop_profile_between_resolution
        from emmer.ndimage.radial_profile.frequency_array import frequency_array
        from emmer.ndimage.radial_profile.compute_radial_profile import compute_radial_profile

        emmap= mrcfile.open(self.emmap_path).data
        rp_emmap_test = compute_radial_profile(emmap)
        freq_test = frequency_array(rp_emmap_test, 1.2156)

        cropped_rp_test = crop_profile_between_resolution(freq_test, rp_emmap_test, 9, 3.4)
        cropped_freq, cropped_amp = cropped_rp_test

        self.assertAlmostEqual(cropped_freq[-1], 1/3.4, delta=1e-2)
        self.assertAlmostEqual(cropped_freq[0], 1/9, delta=1e-2)
    
    def test_get_index_at_resolution(self):
        from emmer.ndimage.radial_profile.profile_tools import get_index_at_resolution
        from emmer.ndimage.radial_profile.frequency_array import frequency_array
        from emmer.ndimage.radial_profile.compute_radial_profile import compute_radial_profile
        emmap= mrcfile.open(self.emmap_path).data
        rp_emmap_test = compute_radial_profile(emmap)
        freq_test = frequency_array(rp_emmap_test, 1.2156)
        index_test = get_index_at_resolution(freq_test, 3.4)
        self.assertEqual(index_test, 90)

    def test_measure_debye(self):
        from emmer.ndimage.radial_profile.measure_debye_effect_magnitude import measure_debye_effect_magnitude
        from emmer.ndimage.radial_profile.frequency_array import frequency_array
        from emmer.ndimage.radial_profile.compute_radial_profile import compute_radial_profile

        emmap= mrcfile.open(self.emmap_path).data
        rp_emmap_test = compute_radial_profile(emmap)
        freq_test = frequency_array(rp_emmap_test, 1.2156)
        debye_magnitude = measure_debye_effect_magnitude(freq_test, rp_emmap_test, wilson_cutoff=10, fsc_cutoff=3.4)
        self.assertAlmostEqual(debye_magnitude,107.3984, delta=2)
    

    


        
    
            
            
        
        
    
        
