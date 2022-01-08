import utils
from piece import Piece

class Board:

    '''
    This initializes the board, all 256 entries, which is only a character array
    '''

    def __init__(self):
        # keep board state as char
        self.board = [[['' for k in range(8)] for j in range(8)] for i in
                    range(8)]
       
    def get(self, coords):
        return self.board[coords[0]][coords[1]][coords[2]]

    def insert(self, coords, piece = Piece()):
        self.board[coords[0]][coords[1]][coords[2]] = piece.sym
    


