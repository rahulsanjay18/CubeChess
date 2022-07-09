from pieces.piece import Piece
from pieces import utils

class Queen(Piece):
    
    def __init__(self, is_white = True):
        self.sym = 'Q' if is_white else 'q'
        self.dir = -1

    def is_valid_move(self, coords, new_coords):
        
        return self._is_face_move(self, coords, new_coords) or\
               self._is_edge_move(self, coords, new_coords) or\
               self._is_vertex_move(self, coords, new_coords)
    
    def _is_face_move(self, coords, new_coords):
       
        diff = (new_coords[0] - coords[0],
                new_coords[1] - coords[1],
                new_coords[2] - coords[2])
        add = sum(diff) 
        # need to prove that this works 
        if diff[0] == add or diff[1] == add or diff[2] == add:
            return utils.check_if_valid_move(new_coords)
        return False

    def _is_edge_move(self, coords, new_coords):
        abs_diff = (abs(new_coords[0] - coords[0]),
                    abs(new_coords[1] - coords[1]),
                    abs(new_coords[2] - coords[2]))

        if sum(abs_diff) == abs_diff[0] * 3:
            return utils.check_if_valid_move(new_coords)

        return False

    def _is_vertex_move(self, coords, new_coords):
        abs_diff = (abs(new_coords[0] - coords[0]),
                    abs(new_coords[1] - coords[1]),
                    abs(new_coords[2] - (coords[2])))
        
        if abs_diff[0] == 0 or abs_diff[1] == 0 or abs_diff[2] == 0:
            sum_d = sum(abs_diff)
            if sum_d == 2 * abs_diff[0] or sum_d == 2 * abs_diff[1]:
                return utils.check_if_valid_move(new_coords)

        return False


    def gen_next_path(self, coords, new_coords):
        
        if self._is_face_move(coords, new_coords):
            temp_coords = tuple(coords)
            index = -1
            if(coords[0] != new_coords[0]):
                index = 0
            elif(coords[1] != coords[1]):
                index = 1
            elif(coords[2] != new_coords[2]):
                index = 2
        
            direction = 1 if coords[index] < new_coords[index] else -1

            while(temp_coords[index] != temp_coords[index]):
                step = list(temp_coords)
                step[index] += direction
                yield tuple(step)
                temp_coords = tuple(step)
        elif self._is_edge_move(coords, new_coords):
            diff = (new_coords[0] - coords[0],
                    new_coords[1] - coords[1],
                    new_coords[2] - coords[2])

            temp_coords = list(coords)

            x_dir = 1 if diff[0] > 0 else -1
            y_dir = 1 if diff[1] > 0 else -1
            z_dir = 1 if diff[2] > 0 else -1

            while temp_coords != new_coords:
            
                if diff[0] != 0:
                    temp_coords[0] += x_dir
                if diff[1] != 0:
                    temp_coords[1] += y_dir
                if diff[2] != 0:
                    temp_coords[2] += z_dir

                yield tuple(temp_coords)
        elif self._is_vertex_move(coords, new_coords):
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
        else:
            raise Exception("Bad move input!")