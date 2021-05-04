import utils

class Board:

        '''
        This initializes the board, all 256 entries
        '''

	def __init__(self):
            self.board = [[[0 for k in range(8)] for j in range(8)] for i in
                    range(8)]
        '''
        This populates the board with pieces to start the initial game
        '''
        def initialize():
            pass
        
        '''
        this checks whether the move is within the bounds of the game, and does
        not capture a piece that is the same color as it.
        '''
        def check_move(self, piece, x, y, z):
            if !(utils.check_if_valid_move(piece, x, y, z)):
                return False
            
        return False
