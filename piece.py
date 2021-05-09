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
                    abs(new_coords[2] - (coords[2]))

        if sum(abs_diff) == 0:
            return utils.check_if_valid_move(new_coords)

        return False


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


class Knight(Piece):
    def __init__(is_white=True):
        self.sym = 'K' if is_white else 'k'

    def is_valid_move(self, coords, new_coords):
        abs_diff = (abs(new_coords[0] - coords[0]),
                    abs(new_coords[1] - coords[1]),
                    abs(new_coords[2] - (coords[2]))

        if sum(abs_diff) == 5:
            if (diff[0] == 1 and diff[1] == 1) or
               (diff[2] == 1 and diff[1] == 1) or
               (diff[0] == 1 and diff[2] == 1):

               return utils.check_if_valid_move(new_coords)
        
        return False


 







