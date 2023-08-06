# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 10:16:11 2021

"""

# global imports
import gemmi
from emmer.pdb.pdb_tools import add_cryst1_line

def add_cryst1_line(pdb_path,unitcell=None,emmap_path=None,new_pdb_path=None):
    '''
    pdb_path -> Address of .pdb path
    
    Some PDB files developed for cryoEM maps do not have proper cryst1 record. Two options to modify:

    1. From an input tuple, or array. In this case, unitcell is a python tuple, which has unit cell dimensions in angstorm
    Ex: unitcell = (x,y,z)
    2. From a mrcfile. In this case, point to an associated EM map and the unit cell dimensions are taken from that
    emmap_path -> Address of associated .mrc file
    
    If you like to the pdb file with a different name, or address then change the 'new_pdb_path' 
    
    '''
    if emmap_path is not None:
        mrc = mrcfile.open(emmap_path)
        cella = mrc.header.cella
        x = cella.x
        y = cella.y
        z = cella.z
    elif unitcell is not None:
        x = unitcell[0]
        y = unitcell[1]
        z = unitcell[2]
    else:
        print("Please give either unit cell dimensions (in Ang) or point to an associated mrc file!")
        return
    
    unitcell = gemmi.UnitCell(x,y,z,90,90,90)
    
    gemmi_structure = gemmi.read_structure(pdb_path)
    gemmi_structure.cell = unitcell
    if new_pdb_path is None:
        gemmi_structure.write_pdb(pdb_path)
    else:
        gemmi_structure.write_pdb(new_pdb_path)
           


