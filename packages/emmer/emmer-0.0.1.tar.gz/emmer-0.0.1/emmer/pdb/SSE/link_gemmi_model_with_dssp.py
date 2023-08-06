# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 14:52:11 2021
"""

# get_dssp contains several functions to analyse secondary structure
# information in PDB structures using Biopython

# global imports
from Bio.PDB import PDBParser
from Bio.PDB.DSSP import DSSP
from Bio.PDB import PDBList
from emmer.pdb.pdb_utils import detect_pdb_input
#%% functions
  
def link_gemmi_model_with_dssp(gemmi_model,dssp):
     '''
     gemmi_model: gemmi.Model() 
     dssp: dictionary which is the output of Bio.PDB.DSSP.DSSP() function
     
     return:
     linked_dictionary[(chain_name,res_id)] = relevant_dssp_key
     '''
     linked_dictionary = {}
     for key in dssp.keys():
          chain_name = key[0]
          res_id = key[1][1]
          linked_dictionary[(chain_name,res_id)] = key
          
     return linked_dictionary
