import unittest
from game import Game
import random

class testGame(unittest.TestCase):
    def setUp(self) -> None:
        self.test_game = Game()
        return super().setUp()
    
    '''
    test make_move (happy case), move pawn, then another piece.
    Check result.
    '''
    def test_make_move(self):
        
        pass

    '''
    test make_move (invalid position at start)
    '''
    def test_invalid_start(self):
        pass

    '''
    test make_move (invalid position at end)
    '''
    def test_invalid_end(self):
        pass

    '''
    test make_move (move coordinates valid but no piece in space)
    '''
    def test_no_piece(self):
        pass

    '''
    test make_move (move piece to capture piece of same color)
    '''
    def test_same_color(self):
        pass

    '''
    test make_move (piece move is invalid). We don't need to test all pieces, just one piece.
    '''
    def test_piece_move_invalid(self):
        pass

    '''
    test make_move (block path for a piece that needs a clear path)
    '''
    def test_blocked_movement(self):
        pass
