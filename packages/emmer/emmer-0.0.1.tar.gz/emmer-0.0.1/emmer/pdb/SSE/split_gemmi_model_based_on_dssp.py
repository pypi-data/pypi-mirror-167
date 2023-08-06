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
from emmer.pdb.SSE.get_dssp import get_dssp
from emmer.pdb.SSE.get_secondary_structure_residues_content import get_secondary_structure_residues_content
#%% functions
  
def split_gemmi_model_based_on_dssp(pdbid,pdb_path):
     
     '''
     Returns two gemmi.Model() based on secondary structure
     '''
     #local imports
     import gemmi
     from emmer.pdb.SSE.link_gemmi_model_with_dssp import link_gemmi_model_with_dssp
     dssp = get_dssp(pdbid,pdb_path)
     secondary_structure_res_list,_ = get_secondary_structure_residues_content(pdbid,pdb_path)
     
     gemmi_model = gemmi.read_pdb(pdb_path)[0]
     helix_model = gemmi.Model('H')
     sheet_model = gemmi.Model('S')
     skipped_residues = 0
     
     linked_dictionary = link_gemmi_model_with_dssp(gemmi_model,dssp)
     print("Number of dssp keys >>> " + str(len(dssp.keys())))
     
     num_residue = 0
     for chain in gemmi_model:
          helix_model.add_chain(chain.name)
          sheet_model.add_chain(chain.name)

          for res in chain:
               #dssp_key = tuple([chain.name,tuple([' ',res.seqid.num,' '])])
               num_residue += 1
               try:
                    dssp_key = linked_dictionary[(chain.name,res.seqid.num)]
                    if dssp[dssp_key][2] in ['H','G','I']:
                         helix_model[chain.name].add_residue(res)
                    elif dssp[dssp_key][2] in ['B','E']:
                         sheet_model[chain.name].add_residue(res)
               except KeyError:
                    skipped_residues += 1
                    
     print("Number of residues in Gemmi Model  >>> " + str(num_residue))

     return helix_model, sheet_model,tuple([num_residue,skipped_residues])

