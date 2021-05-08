class Piece:

    def __init__():
        self.sym = ''

    def get_color(self):
        return self.sym.upper() == self.sym
    
    def get_next_moves(self, coords):
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
            return Dragon(x, y, z, is_white)


class Rook(Piece):
    def __init__(self, is_white=True):
        self.sym = 'R' if is_white else 'r'

    def get_next_moves(self, coords):
        assert len(coords) == 3

        next_moves = []

        for i in range(8):
            if(coords[0] == i):
                continue
            next_moves.append((i, coords[1], coords[2]))

        for i in range(8):
            if(coords[1] == i):
                continue
            next_moves.append((coords[0], i, coords[2]))

        for i in range(8):
            if(coords[2] == i):
                continue
            next_moves.append((coords[0], coords[1], i))

        return next_moves

class Bishop(Piece):
    def __init__(self, is_white=True):
        self.sym = 'B' if is_white else 'b'

    def get_next_moves(self, coords):
        assert len(coords) == 3

        next_moves = []
        
        # i cant think of an algorithm that makes me happy, so im going to do
        # an interesting one instead

        adders = []

        for i in range(8):
            adders.append((i, i, i))
            adders.append((-i, -i, -i))
            
            adders.append((-i, i, i))
            adders.append((i, -i, -i))

            adders.append((i, -i, i))
            adders.append((-i, i, -i))
           
            adders.append((i, i, -i))
            adders.append((-i, -i, i))


        for adder in adders:
            move = tuple(map(lambda i, j: i + j, adder, coords))

            if(8 > move[0] >= 0 and 8 > move[1] >= 0 and 8 > move[2] >= 0):
                next_moves.append(move)

        return next_moves

class Priest(Piece):
    def __init__(is_white=True):
        self.sym = 'T' if is_white else 't'

    def get_next_moves(self, coords):
        assert len(coords) == 3

        next_moves= []
        adders = []

        for i in range(1, 8):
            adders.append((0, i, i))
            adders.append((i, 0, i))
            adders.append((i, i, 0))

            adders.append((0, -i, -i))
            adders.append((-i, 0, -i))
            adders.append((-i, -i, 0))
            
            adders.append((0, -i, i))
            adders.append((-i, 0, i))
            adders.append((-i, i, 0))

            adders.append((0, i, -i))
            adders.append((i, 0, -i))
            adders.append((i, -i, 0))
            


        for adder in adders:
            move = tuple(map(lambda i, j: i + j, adder, coords))

            if(8 > move[0] >= 0 and 8 > move[1] >= 0 and 8 > move[2] >= 0):
                next_moves.append(move)

        return next_moves


class Knight(Piece):
    def __init__(is_white=True):
        self.sym = 'K' if is_white else 'k'

    def get_next_moves(self, coords):
        assert len(coords) == 3

        next_moves = []
        adders = []

        adders.append((2, 1, 1))
        adders.append((-2, -1, -1))
        
        adders.append((2, 1, 1))
        adders.append((-2, -1, -1))
        
        adders.append((2, 1, 1))
        adders.append((-2, -1, -1))
        
        adders.append((2, 1, 1))
        adders.append((-2, -1, -1))





        for adder in adders:
            move = tuple(map(lambda i, j: i + j, adder, coords))

            if(8 > move[0] >= 0 and 8 > move[1] >= 0 and 8 > move[2] >= 0):
                next_moves.append(move)








