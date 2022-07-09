from pieces.piece import Piece
from pieces import utils

class Paladin(Piece):
    
    def __init__(self, is_white = True):
        self.sym = 'P' if is_white else 'p'

    def is_valid_move(self, coords, new_coords):
        abs_diff = (abs(new_coords[0] - coords[0]), abs(new_coords[1] - coords[1]), abs(new_coords[2] - (coords[2])))
        if sum(abs_diff) == 3:
            if abs_diff[0] == 2 or abs_diff[1] == 2 or abs_diff[2] == 2:
                return utils.check_if_valid_move(new_coords)
        
        return False

    def gen_path_step(self, coords, new_coords):
        raise Exception('Paladin does not need to generate a path')