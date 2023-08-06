# -*- coding: utf-8 -*-
"""

"""
import numpy as np
import gemmi
import mrcfile
import matplotlib.pyplot as plt

#%%


def plot_mapContour_model(threshold=0, modelfile="", gemmi_strct="", mapfile="", mrcfile_map="", projection_orientation='z'):
    """
    Function for plotting density map as contour plot with model overlay.
    

    Parameters
    ----------
    threshold : float, optional
        threshold value for plotting. The default is 0.
    modelfile : str, optional
        pdb file to use as model structure. Either modelfile or gemmi_strct must be specified.
    gemmi_strct : gemmi.Structure, optional
        Gemmi structure object containing at least 1 model. Either modelfile or gemmi_strct must be specified.
    mapfile : str, optional
        filename of the target map to be plotted. Either mapfile or mrcfile_map must be specified.
    mrcfile_map : MrcFile, optional
        mrcFile object of the target map.  Either mapfile or mrcfile_map must be specified.
    projection_orientation : str, optional
        axis along which to project the target map, can be 'x', 'y' or 'z'. The default is 'z'.


    Returns
    -------
    None.

    """
    
    if mapfile!="":
        target_map = mrcfile.open(mapfile)
    elif mrcfile_map!="":
        target_map = mrcfile_map
    else:
        print("must specify target map as either path to .mrc file or as mrcfile object")
        return 0
    voxelsize = target_map.header.cella.x / target_map.header.nx
    
    if projection_orientation=='x':
        projection_axis = 0
        plot_axes = [1,2]
    elif projection_orientation=='y':
        projection_axis = 1
        plot_axes = [0,2]
    elif projection_orientation=='z':
        projection_axis = 2
        plot_axes = [0,1]
    else:
        print("please specify valid projection orientation ('x','y','z')")
        return 0
    
    if modelfile!="":
        gemmi_strct = gemmi.read_structure(modelfile)
    elif gemmi_strct=="":
        print("must specify either path to .pdb file or a gemmi.Structure object")
        return 0
        
    T = np.copy(target_map.data) # mrcfile.data object is read only
    T[T<threshold] = np.nan
    
    x = np.linspace(0, target_map.header.cella.x, target_map.header.nx)
    XX,YY = np.meshgrid(x,x)
    
    # prepare plot figure
    projection = np.nanmean(T, axis=projection_axis)
    # projection = np.mean(target_map.data,axis=2)
    fig, ax = plt.subplots()
    # im = ax.imshow(projection, interpolation='spline16')
    cntr = ax.contourf(XX,YY,projection, levels = 32, alpha=0.8)
    cbar = fig.colorbar(im)
    ax.axis('off')
    ax.set_aspect('equal')
    
    # get number of backbone atoms
    numAtoms = 0
    for chn in gemmi_strct[0]:
        for res in chn:
            for atm in res:
                if atm.name == 'C' or atm.name=='N' or atm.name=='CA':
                    numAtoms += 1
    
    # find positions of all backbone atoms
    plot_pos = np.zeros((numAtoms, 3))
    atmidx = 0
    for chn in gemmi_strct[0]:
        for res in chn:
            for atm in res:
                if atm.name == 'C' or atm.name=='N' or atm.name=='CA':
                    if projection_orientation=='x':
                        plot_pos[atmidx,:] = np.array([atm.pos.z, atm.pos.x, atm.pos.y])
                    if projection_orientation=='z':
                        plot_pos[atmidx,:] = np.array([atm.pos.y, atm.pos.z, atm.pos.x])
                    if projection_orientation=='y':
                        plot_pos[atmidx,:] = np.array([atm.pos.x, atm.pos.y, atm.pos.z])      
                    atmidx+=1

    ax.plot(plot_pos[:,plot_axes[0]], plot_pos[:,plot_axes[1]],
            marker='o',
            markerfacecolor='red',
            markeredgecolor='black',
            markersize=3,
            linewidth=1.5,
            color='red')    
    
        