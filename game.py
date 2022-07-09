from board import Board
import pieces.piece as p

class Game:
    
    is_white_turn = True

    def __init__(self):
        self.board = Board()
    
    '''
    Initializes the board with the starting pieces
    '''
    def initialize(self):
        pass

    '''
    This is done in a few steps:
    
    1. Find the piece on the board
    2. Take that piece object and find if its a legal move
    3. If legal, move the piece, if not return False
    4. Find that piece's range of movement
    5. If Rook, Bishop, Priest, Pawn or Queen, we need to remove invalid moves
    6. Remove moves by just iterating, assign the leftover moves to the piece
    7. Return True

    '''
    def make_move(x, y, z, x_p, y_p, z_p):
        pass
