
def get_atomic_point_map(input_pdb, map_shape, apix):
    import numpy as np

    from emmer.pdb.convert.convert_pdb_to_mrc_position import convert_pdb_to_mrc_position
    from emmer.pdb.pdb_utils import detect_pdb_input, get_all_atomic_positions
    
    structure = detect_pdb_input(input_pdb)
    mask = np.zeros(map_shape)
    pdb_positions = get_all_atomic_positions(structure)        
    mrc_position = convert_pdb_to_mrc_position(pdb_positions, apix)
    zz,yy,xx = zip(*mrc_position)
    mask[zz,yy,xx] = 1
    
    return mask

