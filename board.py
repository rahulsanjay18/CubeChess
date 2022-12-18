import pieces.utils as utils
from pieces.piece_factory import PieceFactory

class Board:

    '''
    This initializes the board, all 256 entries, which is only a character array.
    '''

    def __init__(self, board_str=''):
        # keep board state as char
        if board_str != '':
            self.board = self.initialize(board_str)
        else:
            self.board = [[['' for _ in range(8)] for __ in range(8)] for ___ in
                    range(8)]
        
        
    def display_board(self) -> str:
        board_str = ''
        for plane in self.board:
            for line in plane:
                board_str += ''.join(line) + '/'
            board_str = board_str[:-1] + '\n'

        return board_str[:-1]
         

    # def __repr__(self) -> str:
    #     return self.__str__()

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
    


