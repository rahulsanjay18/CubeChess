from pieces.piece import Piece
from pieces import utils

class Pawn(Piece):

    def __init__(self, is_white=True):
        self.sym = 'I' if is_white else 'i'

    def is_valid_move(self, coords, new_coords):
        diff = (new_coords[0] - coords[0],
                new_coords[1] - coords[1],
                new_coords[2] - coords[2])
        
        fwd_step = 1 if self.sym.islower() else -1

        if diff == [0, fwd_step, 0]:
            return utils.check_if_valid_move(new_coords)
        
        return False
    
    def gen_next_path(self, coords, new_coords):
        return Exception("Pawn moves one step, we don't need to check the path")

    def is_valid_attack(self, coords, new_coords):
        diff = (new_coords[0] - coords[0],
                new_coords[1] - coords[1],
                new_coords[2] - coords[2])
        
        fwd_step = 1 if self.sym.islower() else -1

        if diff[1] == fwd_step and (diff[0] == 1 or diff[0] == -1) and (diff[2] == 1 or diff[2] == -1):
            return utils.check_if_valid_move(new_coords)

        return False