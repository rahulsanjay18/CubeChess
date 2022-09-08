from pieces.piece import Piece
from pieces import utils

class Priest(Piece):
    def __init__(self,is_white=True):
        self.sym = 'T' if is_white else 't'

    def is_valid_move(self, coords, new_coords):
        
        abs_diff = (abs(new_coords[0] - coords[0]),
                    abs(new_coords[1] - coords[1]),
                    abs(new_coords[2] - coords[2]))
        
        if abs_diff[0] == 0 or abs_diff[1] == 0 or abs_diff[2] == 0:
            sum_d = sum(abs_diff)
            if sum_d == 2 * abs_diff[0] or sum_d == 2 * abs_diff[1]:
                return utils.check_if_valid_pos(new_coords)

        return False

    def gen_path_step(self, coords, new_coords):
        assert self.is_valid_move(coords, new_coords)
        diff = (new_coords[0] - coords[0],
                new_coords[1] - coords[1],
                new_coords[2] - coords[2])

        temp_coords = coords.copy()

        x_dir = 1 if diff[0] > 0 else -1
        y_dir = 1 if diff[1] > 0 else -1
        z_dir = 1 if diff[2] > 0 else -1

        path = []

        while temp_coords[0] + x_dir != new_coords[0] and \
              temp_coords[1] + y_dir != new_coords[1] and \
              temp_coords[2] + z_dir != new_coords[2]:
            
            if diff[0] != 0:
                temp_coords[0] += x_dir
            if diff[1] != 0:
                temp_coords[1] += y_dir
            if diff[2] != 0:
                temp_coords[2] += z_dir

            path.append(temp_coords.copy())
        
        return path