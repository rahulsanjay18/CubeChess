class PieceFactory:
    """"
    Represents a factory that creates a  piece superclass that each piece inherits from. Each piece has the following functions:

    checkMove: Checks if a move ordered by the piece is valid.
    Piece Representation: the letter representing the piece.
    current position: where on the board is the piece right now
    nextLegalMove: List of legal moves the thing can make

    """

    def create_piece(self, piece_name, x=-1, y=-1, z=-1, is_white=True):
        if(piece_name.lower() == 'king' or piece_name.lower() == 'k'):
            return King(x, y, z, is_white)
        elif(piece_name.lower() == 'queen' or piece_name.lower() == 'q'):
            return Queen(x, y, z, is_white)
        elif(piece_name.lower() == 'bishop' or piece_name.lower() == 'b'):
            return Bishop(x, y, z, is_white)
        elif(piece_name.lower() == 'priest' or piece_name.lower() == 'p'):
            return Priest(x, y, z, is_white)
        elif(piece_name.lower() == 'knight' or piece_name.lower() == 'n'):
            return Knight(x, y, z, is_white)
        elif(piece_name.lower() == 'paladin' or piece_name.lower() == 'l'):
            return Paladin(x, y, z, is_white)
        elif(piece_name.lower() == 'rook' or piece_name.lower() == 'r'):
            return Rook(x, y, z, is_white)
        elif(piece_name.lower() == 'pawn' or piece_name.lower() == 'i'):
            return Pawn(x, y, z, is_white)
        elif(piece_name.lower() == 'dragon' or piece_name.lower() == 'd'):
            return Dragon(x, y, z, is_white)


class Rook:
    def __init__(self, x=-1, y=-1, z=-1, is_white=True):
        self.piece_representation = 'R' if is_white else 'r'
        self.x, self.y, self.z = x, y, z
        self.is_white = is_white
        

    def next_legal_move(self):
        next_moves = []

        for i in range(8):
            if(self.x == i):
                continue
            next_moves.append(i, y, z)

        for i in range(8):
            if(self.y == i):
                continue
            next_moves.append(x, i, z)

        for i in range(8):
            if(self.z == i):
                continue
            next_moves.append(x, y, i)

        self.next_moves = next_moves





