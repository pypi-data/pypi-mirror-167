#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 00:40:10 2021

@author: alok
"""
import numpy as np

       
## Script to add new functions to the ndimage branch

def measure_mask_parameters(mask_path=None, mask=None,apix=None,mask_threshold=0.99,protein_density=1.35,average_atomic_weight=13.14,verbose=True,detailed_report=False):
    
    from emmer.ndimage.map_utils import load_map
    from scipy.constants import Avogadro
    '''
    Function to calculated parameters of a EM Mask map

    Parameters
    ----------
    mask_path : string 
        Path to mask file
    edge_threshold : float 
        The threshold to strictly binarize the FDR map at the edges
    protein_density : float, optional
        Average protein density to calculate number of atoms. The default is 1.35.
    average_atomic_weight : float, optional
        Atomic weight of an "average atom present in protein". 
        Found using 54% carbon, 20% oxygen and 16% nitrogen. The default is 12.066.
    verbose : bool, optional
        Print statistics if True. The default is True.

    Returns
    -------
    num_atoms : int
        Estimated number of atoms based on mask volume, protein density and average atomic weight
    

    '''
    if mask_path is not None:
        mask, apix = load_map(mask_path)
    
    assert mask is not None
    assert apix is not None
    
    
    ang_to_cm = 1e-8
    
    binarise_mask = (mask>=mask_threshold).astype(np.int_)
    
    mask_vol = binarise_mask.sum()*(apix*ang_to_cm)**3
    mask_vol_A3 = binarise_mask.sum()*apix**3
    
    protein_mass = protein_density * mask_vol
    num_moles = protein_mass / average_atomic_weight
    num_atoms = int((num_moles * Avogadro).round())
    maskshape = mask.shape
    mask_dims = [maskshape[0]*apix,maskshape[1]*apix,maskshape[2]*apix]
    
    
    if verbose:
        print("Mask parameters calculated are: \n"+
              "Mask sum voxels: "+str(round(mask.sum(),3))+"\n"+
              "Mask volume: "+str(round(mask_vol_A3,3))+" A^3 \n"+
              "Protein mass: "+str(round(1e21*protein_mass))+" zg\n"+
              "Num atoms: "+str(num_atoms)+"\n") 
        
    if not detailed_report:
        return num_atoms,mask_dims
    else:
        return mask_vol_A3, protein_mass, num_atoms, mask_dims,maskshape
    

def resample_map(emmap, emmap_size_new=None, apix=None, apix_new=None, order=1):
    '''
    Function to resample an emmap in real space using linear interpolation 

    Parameters
    ----------
    emmap : numpy.ndimage
        
    emmap_size_new : tuple 
        
    apix : float
        
    apix_new : float
        

    Returns
    -------
    resampled_emmap

    '''
    from scipy.ndimage import zoom
    if emmap_size_new is None:
        if apix is not None and apix_new is not None:
            resample_factor = apix/apix_new
        else:
            raise UserWarning("Provide either (1) current pixel size and new pixel size or (2) new emmap size")
    
    else:
        try:
            resample_factor = emmap_size_new[0] / emmap.shape[0]
        except:
            raise UserWarning("Please provide proper input: emmap_size_new must be a tuple")
    
    resampled_image = zoom(emmap, resample_factor, order=order)
    
    return resampled_image

      
def resample_image(im, imsize_new=None, apix=1.0, apix_new=None):
    """Returns a real image or volume resampled by cropping/padding its Fourier Transform
    """
    import numpy as np
    
    imsize = np.array(im.shape)
    if np.any(imsize_new == None) and apix_new == None:
        return im
    elif apix_new != None:
        imsize_new = np.round(imsize * apix / apix_new).astype('int')
        pad_factor = imsize_new/imsize
    elif imsize_new != None:
        imsize_new = np.array(imsize_new)
        pad_factor = imsize_new/imsize

    ft = np.fft.fftn(im)
    ft = np.fft.fftshift(ft)
    ft = pad_or_crop_image(ft, pad_factor)
    ft = np.fft.ifftshift(ft)
    return np.fft.ifftn(ft).real  

def pad_or_crop_image(im, pad_factor=None, pad_value = None, crop_image=False):
    """Returns the original image cropped or padded by pad_factor and pad_value; pad_factor being a fraction/multiple of original image size.
       Default behaviour is zero padding.
    """
    if np.any(pad_factor == None):
        return im
    else:
        pad_factor = np.round(np.multiply(pad_factor,np.array(im.shape))).astype('int')

        if pad_value == None:
            pad_value = 0

        if len(im.shape) == 2:       
            if (pad_factor[0] <= im.shape[0] or pad_factor[1] <= im.shape[1]):
                crop_image = True    
            
            if crop_image:
                crop_im = im[im.shape[0]//2-pad_factor[0]//2:im.shape[0]//2+pad_factor[0]//2+pad_factor[0]%2, :]
                crop_im = crop_im[:, im.shape[1]//2-pad_factor[1]//2:im.shape[1]//2+pad_factor[1]//2+pad_factor[1]%2]
                return crop_im
            else:
                pad_im = np.pad(im, ((pad_factor[0]//2-im.shape[0]//2, pad_factor[0]//2-im.shape[0]//2+pad_factor[0]%2), (0,0)), 'constant', constant_values=(pad_value,))
                pad_im = np.pad(pad_im, ((0,0),(pad_factor[1]//2-im.shape[1]//2, pad_factor[1]//2-im.shape[1]//2+pad_factor[1]%2 )), 'constant', constant_values=(pad_value,))
                return pad_im         
            
        elif len(im.shape) == 3:
            if (pad_factor[0] <= im.shape[0] or pad_factor[1] <= im.shape[1] or pad_factor[2] <= im.shape[2]):
                crop_image = True

            if crop_image:
                crop_im = im[im.shape[0]//2-pad_factor[0]//2:im.shape[0]//2+pad_factor[0]//2+pad_factor[0]%2, :, :]
                crop_im = crop_im[:, im.shape[1]//2-pad_factor[1]//2:im.shape[1]//2+pad_factor[1]//2+pad_factor[1]%2, :]
                crop_im = crop_im[:, :, im.shape[2]//2-pad_factor[2]//2:im.shape[2]//2+pad_factor[2]//2+pad_factor[2]%2]
                return crop_im

            else:
                pad_im = np.pad(im, ((pad_factor[0]//2-im.shape[0]//2, pad_factor[0]//2-im.shape[0]//2+pad_factor[0]%2), (0,0), (0,0) ), 'constant', constant_values=(pad_value,))
                pad_im = np.pad(pad_im, ((0,0), (pad_factor[1]//2-im.shape[1]//2, pad_factor[1]//2-im.shape[1]//2+pad_factor[1]%2 ), (0,0)), 'constant', constant_values=(pad_value,))
                pad_im = np.pad(pad_im, ((0,0), (0,0), (pad_factor[2]//2-im.shape[2]//2, pad_factor[2]//2-im.shape[2]//2+pad_factor[2]%2)), 'constant', constant_values=(pad_value,))
                return pad_im