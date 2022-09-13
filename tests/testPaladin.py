import unittest
from pieces.paladin import Paladin
from board import Board
import random

class testPaladin(unittest.TestCase):
    def setUp(self) -> None:
        self.test_paladin = Paladin()

    # (1,1,2)
    def test_valid_move_112(self):
        start_coords = [4,4,4]
        end_coords = [5,5,6]

        self.assertTrue(self.test_paladin.is_valid_move(start_coords, end_coords))
    
    def test_gen_path_test(self):
        start_coords = [4,4,4]
        end_coords = [6,5,6]
        callable = self.test_dragon.gen_path_step
        self.assertRaises(Exception, callable, start_coords, end_coords)

    def test_check_attack(self):
        start_coords = [4,4,4]
        end_coords = [6,5,6]

        self.assertTrue(self.test_paladin.is_valid_attack(start_coords, end_coords))

if __name__ == '__main__':
    unittest.main()