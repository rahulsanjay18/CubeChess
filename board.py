import utils

class Board:

        '''
        This initializes the board, all 256 entries
        '''

	def __init__(self):
            self.board = [[[None for k in range(8)] for j in range(8)] for i in
                    range(8)]
       
        def get(self, coords):
            return self.board[coords[0]][coords[1]][coords[2]]

        def insert(self, coords, piece = None):
            self.board[coords[0]][coords[1]][coords[2]] = piece


