from pieces.piece import Piece
from pieces import utils

class Rook(Piece):
    def __init__(self, is_white=True):
        self.sym = 'R' if is_white else 'r'

    def is_valid_move(self, coords, new_coords):
         
        diff = (new_coords[0] - coords[0],
                new_coords[1] - coords[1],
                new_coords[2] - coords[2])

        add = sum(diff)
        
        # need to prove that this works
        if add != 0 and (diff[0] == add or diff[1] == add or diff[2] == add):
            return utils.check_if_valid_pos(new_coords)
        return False
    
    def gen_path_step(self, coords, new_coords):
        
        assert self.is_valid_move(coords, new_coords)

        temp_coords = coords.copy()
        index = -1
        if(coords[0] != new_coords[0]):
            index = 0
        elif(coords[1] != coords[1]):
            index = 1
        elif(coords[2] != new_coords[2]):
            index = 2
        
        direction = 1 if coords[index] < new_coords[index] else -1
        
        path = []

        while(temp_coords[index] != new_coords[index]):
            temp_coords[index] += direction
            path.append(temp_coords)

        return path[:-1]