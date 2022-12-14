
import unittest
from game import Game
import random

class testBoard(unittest.TestCase):
    def setUp(self)->None:
        self.test_game = Game()

    def testLayout(self):
        true_board = 'rd00r0dr/iiiiiiii/00000000/00000000/00000000/00000000/IIIIIIII/RD00R0DR\ndbpnnpbd/iiiiiiii/00000000/00000000/00000000/00000000/IIIIIIII/DBPNNPBD\n0pbttbp0/iiiiiiii/00000000/00000000/00000000/00000000/IIIIIIII/0PBTTBP0\nrntkqtn0/iiiiiiii/00000000/00000000/00000000/00000000/IIIIIIII/RNTKQTN0\n0ntqqtnr/iiiiiiii/00000000/00000000/00000000/00000000/IIIIIIII/0NTQQTNR\n0pbttbp0/iiiiiiii/00000000/00000000/00000000/00000000/IIIIIIII/0PBTTBP0\ndbpnnpbd/iiiiiiii/00000000/00000000/00000000/00000000/IIIIIIII/DBPNNPBD\nrd0r00dr/iiiiiiii/00000000/00000000/00000000/00000000/IIIIIIII/RD0R00DR'
        
        self.assertEquals(true_board, str(self.test_game.board))
        


if __name__ == '__main__':
    unittest.main()
