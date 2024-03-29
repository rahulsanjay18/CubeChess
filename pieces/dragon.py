from pieces.piece import Piece
from pieces import utils
from coords import Coordinates

class Dragon(Piece):
    def __init__(self, is_white = True):
        self.sym = 'D' if is_white else 'd'

    def is_valid_move(self, coords, new_coords):
        abs_diff = (abs(new_coords[0] - coords[0]),
                    abs(new_coords[1] - coords[1]),
                    abs(new_coords[2] - coords[2]))
        
        if sum(abs_diff) == 5:
            c = Coordinates(abs_diff)
            if (c == Coordinates([2, 2, 1])) or\
               (c == Coordinates([2, 1, 2])) or\
               (c == Coordinates([1, 2, 2])):
                
               return utils.check_if_valid_pos(new_coords)
        
        return False

    def gen_path_step(self, coords, new_coords):
        raise Exception('Dragon does not need to generate a path')
 