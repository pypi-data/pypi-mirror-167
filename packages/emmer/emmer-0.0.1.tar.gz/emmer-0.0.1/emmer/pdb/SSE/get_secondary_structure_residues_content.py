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
#%% functions

def get_secondary_structure_residues_content(pdbid,pdb_path):
     '''
     Input: pdbid: string '3j5p' 
     pdb_path: string - gives the full path of the PDB file
     '''
     # local imports
     import os

     
     dssp = get_dssp(pdbid,pdb_path)    
     secondary_structures = [dssp[key][2] for key in dssp.keys()]
     helix_residues = secondary_structures.count('H') + secondary_structures.count('G') + secondary_structures.count('I')
     sheet_residues = secondary_structures.count('B') + secondary_structures.count('E')
     loop_residues = secondary_structures.count('T') + secondary_structures.count('S')
     total_residues = len(secondary_structures)
     
     secondary_structure_distribution = {}
     secondary_structure_distribution['helix'] = helix_residues/total_residues
     secondary_structure_distribution['sheet'] = sheet_residues/total_residues
     secondary_structure_distribution['loop'] = loop_residues/total_residues
     secondary_structure_distribution['total'] = total_residues
     

     return secondary_structures,secondary_structure_distribution
    
