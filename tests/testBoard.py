
import unittest
from game import Game
import random

class testBoard(unittest.TestCase):
    def setUp(self)->None:
        self.test_game = Game()

    def testLayout(self):
        true_board = 'rd00r0dr/iiiiiiii/00000000/00000000/00000000/00000000/IIIIIIII/RD00R0DR\ndbpnnpbd/iiiiiiii/00000000/00000000/00000000/00000000/IIIIIIII/DBPNNPBD\n0pbttbp0/iiiiiiii/00000000/00000000/00000000/00000000/IIIIIIII/0PBTTBP0\nrntkqtn0/iiiiiiii/00000000/00000000/00000000/00000000/IIIIIIII/RNTKQTN0\n0ntqqtnr/iiiiiiii/00000000/00000000/00000000/00000000/IIIIIIII/0NTQQTNR\n0pbttbp0/iiiiiiii/00000000/00000000/00000000/00000000/IIIIIIII/0PBTTBP0\ndbpnnpbd/iiiiiiii/00000000/00000000/00000000/00000000/IIIIIIII/DBPNNPBD\nrd0r00dr/iiiiiiii/00000000/00000000/00000000/00000000/IIIIIIII/RD0R00DR\n'
        
        self.assertEqual(true_board, self.test_game.board.display_board())

    '''
    makes a move and tests if the board reflects that change
    ''' 
    def testBoardMovement(self):
        true_board = 'rd00r0dr/0iiiiiii/i0000000/00000000/00000000/00000000/IIIIIIII/RD00R0DR\ndbpnnpbd/iiiiiiii/00000000/00000000/00000000/00000000/IIIIIIII/DBPNNPBD\n0pbttbp0/iiiiiiii/00000000/00000000/00000000/00000000/IIIIIIII/0PBTTBP0\nrntkqtn0/iiiiiiii/00000000/00000000/00000000/00000000/IIIIIIII/RNTKQTN0\n0ntqqtnr/iiiiiiii/00000000/00000000/00000000/00000000/IIIIIIII/0NTQQTNR\n0pbttbp0/iiiiiiii/00000000/00000000/00000000/00000000/IIIIIIII/0PBTTBP0\ndbpnnpbd/iiiiiiii/00000000/00000000/00000000/00000000/IIIIIIII/DBPNNPBD\nrd0r00dr/iiiiiiii/00000000/00000000/00000000/00000000/IIIIIIII/RD0R00DR\n'

        st = (0,1,0)
        ed = (0,2,0)
        self.test_game.make_move_t(st, ed)

        self.assertEqual(true_board, self.test_game.board.display_board())

    
    '''
    tests insert function and see if board makes that change
    '''
    def test_insert(self):
        st = (0,1,0)

        ch = self.test_game.board.insert(st, 'k')
        self.assertEqual('k', self.test_game.board.get(st))
        self.assertEqual('i', ch)
    
    '''
    get piece from board, make sure it is the right piece
    '''
    def test_get(self):
        st = (0,1,0)
        self.assertEqual('i', self.test_game.board.get(st))


if __name__ == '__main__':
    unittest.main()
