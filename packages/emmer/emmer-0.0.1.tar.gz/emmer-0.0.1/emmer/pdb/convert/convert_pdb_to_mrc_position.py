def convert_pdb_to_mrc_position(pdb_position, apix):
    '''
    Convert the real units of positions into indices for the emmap. 
    Note: returns in (Z,Y,X) format
    

    Parameters
    ----------
    pdb_position : list
        list of xyz positions (Angstorm)
    apix : float
        Pixel size 

    Returns
    -------
    mrc_position : list
        List of ZYX positions (index positions)

    '''
    mrc_position = []
    
    for pos in pdb_position:
        [x,y,z] = pos
        int_x, int_y, int_z = int(round(x/apix)), int(round(y/apix)), int(round(z/apix))
        mrc_position.append([int_z, int_y, int_x])
        
    return mrc_position