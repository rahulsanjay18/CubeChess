from pieces.piece import Piece
from pieces import utils

class Pawn(Piece):

    def __init__(self, is_white=True):
        self.sym = 'I' if is_white else 'i'

    def is_valid_move(self, coords, new_coords):
        diff = (new_coords[0] - coords[0],
                new_coords[1] - coords[1],
                new_coords[2] - coords[2])
        
        fwd_step = -1 if self.sym.islower() else 1
        
        if diff[0] == 0 and diff[2] == 0 and (diff[1] == fwd_step):
            return utils.check_if_valid_pos(new_coords)
        
        if diff[0] == 0 and diff[2] == 0 and \
            ((coords[1] == 1 and new_coords[1] == 3) \
                or (coords[1] == 6 and new_coords[1] == 4)):
            
            return utils.check_if_valid_pos(new_coords)

        if self.is_valid_attack(coords, new_coords):
            return utils.check_if_valid_pos(new_coords)

        return False
    
    def gen_next_path(self, coords, new_coords):
        return Exception("Pawn moves one step, we don't need to check the path")

    def is_valid_attack(self, coords, new_coords):
        diff = (new_coords[0] - coords[0],
                new_coords[1] - coords[1],
                new_coords[2] - coords[2])
        atk_diff = [1,0,-1]
        fwd_step = -1 if self.sym.islower() else 1

        if diff[1] == fwd_step and (diff[0] in atk_diff) and (diff[2] in atk_diff):
            return utils.check_if_valid_pos(new_coords)

        return False