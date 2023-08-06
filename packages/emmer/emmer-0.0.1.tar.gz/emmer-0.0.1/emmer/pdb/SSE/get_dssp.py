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

def get_dssp(pdbid,pdb_path):  
    parser = PDBParser()
    structure = parser.get_structure(pdbid,pdb_path)
    model = structure[0]
    try:
        dssp = DSSP(model,pdb_path)
        print("Successfully performed DSSP! \n")
    except Exception as e:
        print("Problem with DSSP")
        print(e)
        raise
    
    return dssp
