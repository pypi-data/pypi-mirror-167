def get_spherical_mask(input_emmap, radius_pixels):
    from emmer.ndimage.map_utils import parse_input

    emmap = parse_input(input_emmap)
    n = emmap.shape[0]
    z,y,x = np.ogrid[-n//2:n//2,-n//2:n//2,-n//2:n//2]
    mask = (x**2+y**2+z**2 <= radius_pixels**2).astype(np.int)
    return mask