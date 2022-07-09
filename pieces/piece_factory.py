from pieces.king import King
from pieces.queen import Queen
from pieces.bishop import Bishop
from pieces.priest import Priest
from pieces.knight import Knight
from pieces.paladin import Paladin
from pieces.rook import Rook
from pieces.pawn import Pawn
from pieces.dragon import Dragon

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
