import pieces.utils as utils
from pieces.piece_factory import PieceFactory
import numpy as np

class Board:

    # Do not change, this is just to eliminate the magic number
    size = 8

    '''
    This initializes the board, all 256 entries, which is only a character array.
    '''
    def __init__(self, board_str=''):
        
        # keep board state as char
        if board_str != '':
            self.board = self.initialize(board_str)
        elif board_str == 'blank':
            self.board = [[['0' for _ in range(Board.size)] for __ in range(Board.size)] for ___ in
                    range(Board.size)]
        else:
            self.board = [[['' for _ in range(Board.size)] for __ in range(Board.size)] for ___ in
                    range(Board.size)]
        
        
    def display_board(self) -> str:
        board_str = ''
        for plane in self.board:
            for line in plane:
                board_str += ''.join(line) + '/'
            board_str = board_str[:-1] + '\n'

        return board_str

    def convert_to_numpy(self):
        array = [[[ord(c) for c in line] for line in self.board] for plane in
                    self.board]
        
        return np.asarray(array)

    '''
    Initializes the board with the starting pieces
    '''
    def initialize(self, board_str):
        data = board_str.split('~')
        
        board = []

        for line in data:
            rows = line.split('/')
            board.append([list(c) for c in rows])

        return board

    def get(self, coords):
        return self.board[coords[0]][coords[1]][coords[2]]

    def insert(self, coords, piece):
        replaced = self.board[coords[0]][coords[1]][coords[2]]
        self.board[coords[0]][coords[1]][coords[2]] = piece
        return replaced
    


