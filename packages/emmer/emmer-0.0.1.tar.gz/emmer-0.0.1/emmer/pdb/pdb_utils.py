# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 14:08:55 2021
"""

# pdb_util contains helper functions used in other applications in the emmer
# toolbox. pdb_util functions are classified as such if there is little need
# to manually call these functions and/or when their output is used in
# many different applications.

# global imports
import gemmi
import numpy as np
#%% functions

def get_gemmi_st_from_id(pdb_id):
    '''
    Returns a gemmi.Structure() containing the PDB coordinate information and headers for a given PDB-ID. 

    Parameters
    ----------
    pdb_id : string
        PDB ID: "3j5p"

    Returns
    -------
    gemmi_st : gemmi.Structure()

    '''          
    import pypdb
    
    try: 
        pdb_file = pypdb.get_pdb_file(pdb_id,filetype='pdb',compression=False)
        pdb_struc = gemmi.read_pdb_string(pdb_file)
        print("- Successfully downloaded PDBgemmi {} from database".format(pdb_id))
        return pdb_struc
    except AttributeError:
        cif_file = pypdb.get_pdb_file(pdb_id, filetype='cif',\
                                          compression=False)
        cif_struc = gemmi.read_pdb_string(cif_file)
        return cif_struc
    
def check_if_gemmi_st_is_downloadable(pdb_id):
    """[summary]

    Args:
        pdb_id (str): PDB ID, like: "3j5p"

    Returns:
        Bool: indicating whether the gemmi structure is downloadable (True) or not (False)
    """    
    import pypdb
    
    try: 
        pdb_file = pypdb.get_pdb_file(pdb_id, filetype='pdb',compression=False)
        return True
    except AttributeError:
        try:
            cif_file = pypdb.get_pdb_file(pdb_id, filetype='cif', compression=False)
            return True
        except Exception as e:
            print("- Exception: {}".format(e))
            return False
        
def detect_pdb_input(input_pdb):
    '''
    Function to detect the type of input the user has passed and return gemmi.Structure as output

    Parameters
    ----------
    input_pdb : str or gemmi.Structure
        Input can be either 
        a) string: either (i) pdb path, for ex: "path/to/pdb.pdb" or 
                          (ii)pdb_id "3j5p"
        b) gemmi.Structure()

    Returns
    -------
    pdb_structure : gemmi.Structure()
        Parsed input of type gemmi.Structure()
        Returns nothing if input cannot be parsed properly.

    '''
    from emmer.pdb.pdb_utils import get_gemmi_st_from_id
    
    if isinstance(input_pdb, str):
        if input_pdb.split(sep='.')[-1] in ['pdb','cif']:  # Then input is a file path
            pdb_structure = gemmi.read_structure(input_pdb)
            return pdb_structure
        elif ("/" not in input_pdb) or ("\\" not in input_pdb) or ("." not in input_pdb): # Then input is not file path but pdb_id
            pdb_structure = get_gemmi_st_from_id(input_pdb)
            return pdb_structure
        else:
            print("Input cannot be parsed. Please pass a pdb_id (as string) or pdb_path (as string)")
    elif isinstance(input_pdb, gemmi.Structure):
        pdb_structure = input_pdb.clone()
        return pdb_structure
    else:
        print("Unknown datatype for input. Please pass either a gemmi.Structure() or a\
              string (pointing to pdb_path or pdb_id")
    
def set_to_center_of_unit_cell(input_pdb, unitcell):
    '''
    Function to set the center of mass of a PDB structure to the center of a unitcell

    Parameters
    ----------
    pdb_structure : gemmi.Structure
        Input structure 
    unitcell : gemmi.UnitCell
        Input unitcell

    Returns
    -------
    centered_pdb : gemmi.Structure

    '''
    from emmer.pdb.pdb_utils import shift_coordinates
    
    pdb_structure_local = detect_pdb_input(input_pdb)
    center_of_mass_old = np.array(pdb_structure_local[0].calculate_center_of_mass().tolist())
    center_of_mass_new = np.array([unitcell.a/2, unitcell.b/2, unitcell.c/2])
    
    translation_matrix = center_of_mass_new - center_of_mass_old
    shifted_structure = shift_coordinates(trans_matrix=translation_matrix, input_pdb=pdb_structure_local)
    
    return shifted_structure

def get_atomic_positions_between_residues(input_pdb, chain_name, res_range = None, model_index=0):
    '''
    Extract atom positions between residue range

    Parameters
    ----------
    gemmi_structure : gemmi.Structure()
        input gemmi structure
    chain_name : str
        
    res_range : list
        res_range = [start_res, end_res] (both incl)

    Returns
    -------
    pdb_positions : list
    
    pdb_positions = [[x1, y1, z1], [x2, y2, z3]...] (values in Angstorm)
    '''
    structure = detect_pdb_input(input_pdb)
    gemmi_model = structure[model_index]
    pdb_positions = []
    for chain in gemmi_model:
        if chain.name == chain_name:
            if res_range is not None:
                for res in chain:
                    if res.seqid.num >= res_range[0] and res.seqid.num <= res_range[1] :
                        for atom in res:
                            pdb_positions.append(atom.pos.tolist())
            else:
                for res in chain:
                    for atom in res:
                        pdb_positions.append(atom.pos.tolist())
                        
    
    return pdb_positions

def get_unit_cell_estimate(pdb_struct,vsize):
          
    '''
    Find an estimated size of unit cell in A based on nunber of atoms and apix

    As reference: PDB3J5P had ~18000 atoms and a box size of 256^3
          
    '''

    number_of_atoms = pdb_struct[0].count_atom_sites()
    estimated_box_size = number_of_atoms * 256 / 18000
    unit_cell_dim =  estimated_box_size * vsize
    unitcell = gemmi.UnitCell(unit_cell_dim,unit_cell_dim,unit_cell_dim,90,90,90)
          
    return unitcell

def replace_pdb_column_with_arrays(input_pdb, replace_column, replace_array):
    '''
    Replace a column in the PDB (either bfactor or occupancy) with values from an array where the \ 
        array index position correspods to atom location in the cra generator

    Parameters
    ----------
    input_pdb : str to gemmi structure
        path to pdb file or a gemmi structure.
    replace_column : str
        string to specify which PDB column to replace values with
    replace_array : numpy.ndarray (1d)
        replace values of column with these values

    Returns
    -------
    st: gemmi.Structure
    

    '''
    
    st = detect_pdb_input(input_pdb)
    
    replace_array = np.clip(replace_array, 0, 999)  ## PDB array only allows a maximum of three digits
    for i,cra_gen in enumerate(st[0].all()):
        if replace_column=="bfactor":
            cra_gen.atom.b_iso = replace_array[i]
        elif replace_column=="occ":
            cra_gen.atom.occ = replace_array[i]
        else:
            raise UserWarning("Please input either bfactor or occ for the replace_column variable")
        
    
    return st

def remove_charges(input_pdb):
    structure = detect_pdb_input(input_pdb)
    
    for model in structure:
        for chain in model:
            for residue in chain:
                for atom in residue:
                    atom.charge = 0
    
    return structure

def shift_coordinates(input_pdb, trans_matrix=[0,0,0]):
    """
    Shift atomic coordinates based on a translation matrix
    """
    structure = detect_pdb_input(input_pdb)
            
    for model in structure:
        for chain in model:
            for residue in chain:
                for atom in residue:
                    atom.pos = gemmi.Position(atom.pos.x+trans_matrix[0],
                                              atom.pos.y+trans_matrix[1],
                                              atom.pos.z+trans_matrix[2])
        
    return structure
  
def split_model_based_on_nucleotides(input_pdb):
    structure = detect_pdb_input(input_pdb)
    dna_model = gemmi.Model('D')
    rna_model = gemmi.Model('R')
    
    for model in structure:
        for chain in model:
            dna_model.add_chain(chain.name)
            rna_model.add_chain(chain.name)
            for res in chain:
                if res.name in ['C','G','A','U','I']:
                    rna_model[chain.name].add_residue(res)
                elif res.name in ['DC','DG','DA','DU','DI','DT']:
                    dna_model[chain.name].add_residue(res)
    
    dna_st = gemmi.Structure()
    dna_st.add_model(dna_model)
    
    rna_st = gemmi.Structure()
    rna_st.add_model(rna_model)

    return dna_st, rna_st    

def get_all_atomic_positions(input_pdb, as_dictionary=False):
    '''
    Extract atom positions

    Parameters
    ----------
    gemmi_structure : gemmi.Structure()
        input gemmi structure
    chain_name : str
        
    res_range : list
        res_range = [start_res, end_res] (both incl)

    Returns
    -------
    pdb_positions : list
    
    pdb_positions = [[x1, y1, z1], [x2, y2, z3]...] (values in Angstorm)
    '''
    
    st = detect_pdb_input(input_pdb)
    
    if as_dictionary:
        pdb_positions = {}
        for i,cra_obj in enumerate(st[0].all()):
            pdb_positions[i] = np.array(cra_obj.atom.pos.tolist())
        
        return pdb_positions
                        
    
    else:
        pdb_positions = []
        for chain in st[0]:
            for res in chain:
                for atom in res:
                    pdb_positions.append(atom.pos.tolist())
                            
        
        return np.array(pdb_positions)

def set_all_atomic_positions(input_pdb, positions_dictionary):
    '''
    Input a dictionary where keys are atomic "access IDs " generated by the function get_all_atomic_positions

    Parameters
    ----------
    gemmi_structure : TYPE
        DESCRIPTION.
    positions_dictionary : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    
    st = detect_pdb_input(input_pdb)
    for i, cra_obj in enumerate(st[0].all()):
        new_position = gemmi.Position(positions_dictionary[i][0],positions_dictionary[i][1],positions_dictionary[i][2])
        cra_obj.atom.pos = new_position
    
    return st
    

def get_bfactors(input_pdb, model_index=None, return_type="list"):
    """
    Get B-factors of atoms
    """
    dict_chain = {}
    if model_index is not None:
        input_structure = detect_pdb_input(input_pdb)
        probe_model = input_structure[model_index]
        structure = gemmi.Structure()
        structure.add_model(probe_model)
    else:
        structure = detect_pdb_input(input_pdb)
    
    
        
    list_bfact = []
    for model in structure:
        for chain in model:
            if not chain.name in dict_chain:
                dict_chain[chain.name] = {}
            for residue in chain:
                residue_id = str(residue.seqid.num)+'_'+residue.name
                for atom in residue:
                    list_bfact.append(atom.b_iso)
                avg_bfact = sum(list_bfact)/float(len(list_bfact))
                dict_chain[chain.name][residue_id] = round(avg_bfact,3)
    
    if return_type=="list":
        return list_bfact
    elif return_type=="dictionary":
        return dict_chain
    else:
        raise UserWarning("Enter return_type as either list or dictionary")
        

def add_atomic_bfactors(input_pdb, additional_biso):
    '''
    Function to modify atomic bfactors uniformly by adding or subtracting b factors to each atom present in the PDB.
    

    Parameters
    ----------
    input_pdb : string or gemmi.Structure
        Path to a PDB file or gemmi structure
    
    additional_biso : float, 
        Parameter to specify how the bfactors of the atomic model be modified

    Returns
    -------
     st : gemmi.Structure 

    '''
    
    structure = detect_pdb_input(input_pdb)
    
    for model in structure:
        for chain in model:
            for res in chain:
                for atom in res:
                    atom.b_iso += additional_biso
    
    
    return structure
    
def set_atomic_bfactors(input_pdb, b_iso=None):
    '''
    Function to modify atomic bfactors uniformly by adding or subtracting b factors to each atom present in the PDB.
    

    Parameters
    ----------
    in_model_path : str, optional
        Path to a PDB file. 
    gemmi_st : gemmi.Structure()
        Pass a gemmi.Structure() instead of a path to perform computation online
    b_iso : float, 
        Parameter to specify the bfactors of the atomic model

    Returns
    -------
    If in_model_path is passed, returns the output model path.. Else returns the gemmi.Structure()

    '''
    structure = detect_pdb_input(input_pdb)

    for model in structure:
        for chain in model:
            for res in chain:
                for atom in res:
                    atom.b_iso = b_iso

    return structure

def get_residue_ca_coordinates(input_pdb):
    
    structure = detect_pdb_input(input_pdb)
    
    dict_coord = {}
    for model in structure:
        if not model.name in dict_coord: dict_coord[model.name] = {}
        for chain in model:
            polymer = chain.get_polymer()
            #skip non polymers
            #if not polymer: continue
            
            if not chain.name in dict_coord[model.name]: 
                dict_coord[model.name][chain.name] = {}
            for residue in chain:
                residue_id = str(residue.seqid.num)+'_'+residue.name
                residue_centre = ()
                if residue.name in ['A','T','C','G','U']:#nuc acid
                    for atom in residue:
                        if atom.name in ["P","C3'","C1'"]:
                            residue_centre = (atom.pos.x,atom.pos.y,atom.pos.z)
                else:
                    for atom in residue:
                        if atom.name == 'CA':#prot
                            residue_centre = (atom.pos.x,atom.pos.y,atom.pos.z)
                if len(residue_centre) == 0:#non nuc acid / prot
                    try: 
                        center_index = len(residue)/2
                        atom = residue[center_index]
                        residue_centre = (atom.pos.x,atom.pos.y,atom.pos.z)
                    except: 
                        for atom in residue:
                            residue_centre = (atom.pos.x,atom.pos.y,atom.pos.z)
                            break #first atom
                if len(residue_centre) > 0:
                    dict_coord[model.name][str(chain.name)][str(residue.seqid.num)] = \
                                            [residue_centre, residue.name]

    return dict_coord

def get_coordinates(input_pdb):
    list_coord = []
    structure = detect_pdb_input(input_pdb)
    for model in structure:
        for chain in model:
            for residue in chain:
                for atom in residue:
                    coord = atom.pos #gemmi Position
                    list_coord.append([coord.x,coord.y,coord.z])
    return list_coord

def find_number_of_neighbors(input_pdb, atomic_position, window_size_A):    
    gemmi_structure = detect_pdb_input(input_pdb)
    
    # Neighbor Search initialize
    
    ns = gemmi.NeighborSearch(gemmi_structure[0], gemmi_structure.cell, window_size_A).populate()
    
    gemmi_position = gemmi.Position(atomic_position[0], atomic_position[1], atomic_position[2])
    
    neighbors = ns.find_atoms(gemmi_position, '\0', radius=window_size_A)
    atoms = [gemmi_structure[0][x.chain_idx][x.residue_idx][x.atom_idx] for x in neighbors]
    number_of_neighbors = len(atoms)
    
    
    return number_of_neighbors

def get_atomic_bfactor_window(input_pdb, atomic_position, window_size_A):
    gemmi_structure = detect_pdb_input(input_pdb)
    
    # Neighbor Search initialize
    
    ns = gemmi.NeighborSearch(gemmi_structure[0], gemmi_structure.cell, window_size_A).populate()
    
    gemmi_position = gemmi.Position(atomic_position[0], atomic_position[1], atomic_position[2])
    
    neighbors = ns.find_atoms(gemmi_position, '\0', radius=window_size_A)
    atoms = [gemmi_structure[0][x.chain_idx][x.residue_idx][x.atom_idx] for x in neighbors]
    atomic_bfactor_list = np.array([x.b_iso for x in atoms])
    
    average_atomic_bfactor = atomic_bfactor_list.mean()
    
    return average_atomic_bfactor

def find_radius_of_gyration(input_pdb):
    
    structure = detect_pdb_input(input_pdb)
    
    num_atoms = structure[0].count_atom_sites()
    com = structure[0].calculate_center_of_mass()
    distances = []
    for model in structure:
        for chain in model:
            for res in chain:
                ca = res.get_ca()
                if ca is not None:
                    distances.append(com.dist(ca.pos))
    
    np_distance = np.array(distances)
    
    Rg = np.sum(np_distance**2)/num_atoms
    
    return Rg