def check_if_valid_pos(coords):
    valid_x = 8 > coords[0] >= 0 and isinstance(coords[0], int) 
    valid_y = 8 > coords[1] >= 0 and isinstance(coords[1], int)
    valid_z = 8 > coords[2] >= 0 and isinstance(coords[2], int)
    
    return valid_x and valid_y and valid_z
