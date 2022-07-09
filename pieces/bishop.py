from pieces.piece import Piece
from pieces import utils

class Bishop(Piece):
    def __init__(self, is_white=True):
        self.sym = 'B' if is_white else 'b'
    
    def is_valid_move(self, coords, new_coords):
        
        abs_diff = (abs(new_coords[0] - coords[0]),
                    abs(new_coords[1] - coords[1]),
                    abs(new_coords[2] - coords[2]))

        if sum(abs_diff) == abs_diff[0] * 3:
            return utils.check_if_valid_move(new_coords)

        return False
    
    def gen_path_step(self, coords, new_coords):
        assert self.is_valid_move(coords, new_coords)
        
        diff = (new_coords[0] - coords[0],
                new_coords[1] - coords[1],
                new_coords[2] - coords[2])

        temp_coords = list(coords)

        x_dir = 1 if diff[0] > 0 else -1
        y_dir = 1 if diff[1] > 0 else -1
        z_dir = 1 if diff[2] > 0 else -1

        while temp_coords != new_coords:
            temp_coords[0] += x_dir
            temp_coords[1] += y_dir
            temp_coords[2] += z_dir

            yield tuple(temp_coords)