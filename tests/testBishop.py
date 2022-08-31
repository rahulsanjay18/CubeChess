import unittest
from pieces.bishop import Bishop
from board import Board
import random

class testRook(unittest.TestCase):
    def setUp(self) -> None:
        self.test_bishop = Bishop()

    def test_valid_move(self):
        start_coords = [0,0,0]
        end_coords = [7,7,7]

        self.assertTrue(self.test_bishop.is_valid_move(start_coords, end_coords))
    
    def test_invalid_move(self):
        start_coords = [0, 0, 0]
        end_coords = [3, 4, 2]

        self.assertFalse(self.test_bishop.is_valid_move(start_coords, end_coords))
    
    def test_gen_path_test(self):
        start_coords = [0,0,0]
        end_coords = [7,7,7]

        true_path = [[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5],[6,6,6]]

        path = self.test_bishop.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    def test_check_attack(self):
        start_coords = [0,0,0]
        end_coords = [7,7,7]

        self.assertTrue(self.test_bishop.is_valid_attack(start_coords, end_coords))

if __name__ == '__main__':
    unittest.main()