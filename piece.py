import utils

class Piece:

    def __init__():
        self.sym = ''

    def get_color(self):
        return self.sym.upper() == self.sym
    
    def is_valid_move(self, coords, new_coords):
        raise NotImplementedError

    def gen_path_step(self, coords, new_coords):
        raise NotImplementedError

class PieceFactory:
    """"
    Represents a factory that creates a  piece superclass that each piece inherits from. Each piece has the following functions:

    checkMove: Checks if a move ordered by the piece is valid.
    Piece Representation: the letter representing the piece.
    current position: where on the board is the piece right now
    nextLegalMove: List of legal moves the thing can make

    """

    def create_piece(self, piece_name, is_white=True):
        

        if(piece_name.lower() == 'king' or piece_name.lower() == 'k'):
            return King(is_white)
        elif(piece_name.lower() == 'queen' or piece_name.lower() == 'q'):
            return Queen(is_white)
        elif(piece_name.lower() == 'bishop' or piece_name.lower() == 'b'):
            return Bishop(is_white)
        elif(piece_name.lower() == 'priest' or piece_name.lower() == 't'):
            return Priest(is_white)
        elif(piece_name.lower() == 'knight' or piece_name.lower() == 'n'):
            return Knight(is_white)
        elif(piece_name.lower() == 'paladin' or piece_name.lower() == 'p'):
            return Paladin(is_white)
        elif(piece_name.lower() == 'rook' or piece_name.lower() == 'r'):
            return Rook(is_white)
        elif(piece_name.lower() == 'pawn' or piece_name.lower() == 'i'):
            return Pawn(is_white)
        elif(piece_name.lower() == 'dragon' or piece_name.lower() == 'd'):
            return Dragon(is_white)


class Rook(Piece):
    def __init__(self, is_white=True):
        self.sym = 'R' if is_white else 'r'

    def is_valid_move(self, coords, new_coords):
         
        diff = (new_coords[0] - coords[0],
                new_coords[1] - coords[1],
                new_coords[2] - coords[2])

        add = sum(diff)

        # need to prove that this works
        if diff[0] == add or diff[1] == add or diff[2] == add:
            return utils.check_if_valid_move(new_coords)
        return False
    
    def gen_path_step(self, coords, new_coords):
        
        assert is_valid_move(self, coords, new_coords)

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
        assert is_valid_move(self, coords, new_coords)
        
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


class Priest(Piece):
    def __init__(is_white=True):
        self.sym = 'T' if is_white else 't'

    def is_valid_move(self, coords, new_coords):
        
        abs_diff = (abs(new_coords[0] - coords[0]),
                    abs(new_coords[1] - coords[1]),
                    abs(new_coords[2] - (coords[2]))
        
        if abs_diff[0] == 0 or abs_diff[1] == 0 or abs_diff[2] == 0:
            sum_d = sum(abs_diff)
            if sum_d == 2 * abs_diff[0] or sum_d == 2 * abs_diff[1]:
                return utils.check_if_valid_move(new_coords)

        return False

    def gen_path_step(self, coords, new_coords):
        assert is_valid_move(self, coords, new_coords)
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


class Knight(Piece):
    def __init__(is_white=True):
        self.sym = 'K' if is_white else 'k'

    def is_valid_move(self, coords, new_coords):
        abs_diff = (abs(new_coords[0] - coords[0]),
                    abs(new_coords[1] - coords[1]),
                    abs(new_coords[2] - (coords[2]))

        if sum(abs_diff) == 4:
            if (diff[0] == 1 and diff[1] == 1) or
               (diff[2] == 1 and diff[1] == 1) or
               (diff[0] == 1 and diff[2] == 1):

               return utils.check_if_valid_move(new_coords)
        
        return False

    def gen_path_step(self, coords, new_coords):
        raise Exception('Knight does not need to generate a path')


class Paladin(Piece):
    
    def __init__(is_white = True):
        self.sym = 'P' if is_white else 'p'

    def is_valid_move(self, coords, new_coords):
       abs_diff = (abs(new_coords[0] - coords[0]),
                    abs(new_coords[1] - coords[1]),
                    abs(new_coords[2] - (coords[2]))

 
        if sum(abs_diff) == 3:
            if diff[0] == 2 or diff[1] == 2 or diff[2] == 2:
               return utils.check_if_valid_move(new_coords)
        
        return False

    def gen_path_step(self, coords, new_coords):
        raise Exception('Paladin does not need to generate a path')
 
class Dragon(Piece):
    def __init__(is_white = True):
        self.sym = 'D' if is_white else 'd'

    def is_valid_move(self, coords, new_coords):
       abs_diff = (abs(new_coords[0] - coords[0]),
                    abs(new_coords[1] - coords[1]),
                    abs(new_coords[2] - (coords[2]))

 
        if sum(abs_diff) == 5:
            if (diff[0] == 2 and diff[1] == 2) or
               (diff[2] == 2 and diff[1] == 2) or
               (diff[0] == 2 and diff[2] == 2):
                
               return utils.check_if_valid_move(new_coords)


        
        return False

    def gen_path_step(self, coords, new_coords):
        raise Exception('Dragon does not need to generate a path')
 

class Queen(Piece):
    
    def __init__(is_white = True):
        self.sym = 'Q' if is_white else 'q'
        self.dir = -1

    def is_valid_move(self, coords, new_coords):
        
        return _is_face_move(self, coords, new_coords) or
               _is_edge_move(self, coords, new_coords) or
               _is_vertex_move(self, coords, new_coords)
    
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
                    abs(new_coords[2] - (coords[2]))
        
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


class King(Piece):
    def __init__(is_white = True):
        self.sym = 'K' if is_white else 'k'

    def is_valid_move(self, coords, new_coords):
        
        abs_diff = (abs(new_coords[0] - coords[0]),
                    abs(new_coords[1] - coords[1]),
                    abs(new_coords[2] - (coords[2]))

        if sum(abs_diff) == 0:
            return utils.check_if_valid_move(new_coords)

    def gen_next_path(self, coords, new_coords):
        
        raise Exception("King does not have path")




        



