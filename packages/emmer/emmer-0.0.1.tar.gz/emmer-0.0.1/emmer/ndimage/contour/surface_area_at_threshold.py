## Script to measure surface area of an EM-map at a given threshold

def surface_area_at_threshold(emmap, apix, reference_threshold):
    import numpy as np

    from emmer.ndimage.contour.contour_utils import mesh_surface_area
    
    binarised_emmap = (emmap>=reference_threshold).astype(np.int_)
    surface_area = mesh_surface_area(binarised_emmap, 0.9999999, apix)
    return surface_area
