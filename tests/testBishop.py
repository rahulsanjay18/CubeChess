import unittest
from pieces.bishop import Bishop
from board import Board
import random

class testBishop(unittest.TestCase):
    def setUp(self) -> None:
        self.test_bishop = Bishop()

    def test_valid_move_xyz(self):
        start_coords = [4,4,4]
        end_coords = [7,7,7]

        self.assertTrue(self.test_bishop.is_valid_move(start_coords, end_coords))
    
    def test_valid_move__x_y_z(self):
        start_coords = [4,4,4]
        end_coords = [0,0,0]

        self.assertTrue(self.test_bishop.is_valid_move(start_coords, end_coords))
    
    def test_valid_move_xy_z(self):
        start_coords = [4,4,4]
        end_coords = [7,7,1]

        self.assertTrue(self.test_bishop.is_valid_move(start_coords, end_coords))
    
    def test_valid_move_x_yz(self):
        start_coords = [4,4,4]
        end_coords = [7,1,7]

        self.assertTrue(self.test_bishop.is_valid_move(start_coords, end_coords))

    def test_valid_move__xyz(self):
        start_coords = [4,4,4]
        end_coords = [1,7,7]

        self.assertTrue(self.test_bishop.is_valid_move(start_coords, end_coords))

    def test_valid_move__xy_z(self):
        start_coords = [4,4,4]
        end_coords = [1,7,1]

        self.assertTrue(self.test_bishop.is_valid_move(start_coords, end_coords))

    def test_valid_move_x_y_z(self):
        start_coords = [4,4,4]
        end_coords = [7,1,1]

        self.assertTrue(self.test_bishop.is_valid_move(start_coords, end_coords))
    
    def test_valid_move__x_yz(self):
        start_coords = [4,4,4]
        end_coords = [1,1,7]

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

    def test_gen_path_test_xyz(self):
        start_coords = [4,4,4]
        end_coords = [7,7,7]

        true_path = [[5,5,5],[6,6,6]]

        path = self.test_bishop.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    def test_gen_path_test__x_y_z(self):
        start_coords = [4,4,4]
        end_coords = [0,0,0]

        true_path = [[3,3,3],[2,2,2],[1,1,1]]

        path = self.test_bishop.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    def test_gen_path_test_xy_z(self):
        start_coords = [4,4,4]
        end_coords = [7,7,1]

        true_path = [[5,5,3],[6,6,2]]

        path = self.test_bishop.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    def test_gen_path_test_x_yz(self):
        start_coords = [4,4,4]
        end_coords = [7,1,7]

        true_path = [[5,3,5],[6,2,6]]

        path = self.test_bishop.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)

    def test_gen_path_test__xyz(self):
        start_coords = [4,4,4]
        end_coords = [1,7,7]

        true_path = [[3,5,5],[2,6,6]]

        path = self.test_bishop.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    def test_gen_path_test__xy_z(self):
        start_coords = [4,4,4]
        end_coords = [1,7,1]

        true_path = [[3,5,3],[2,6,2]]

        path = self.test_bishop.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)

    def test_gen_path_test_x_y_z(self):
        start_coords = [4,4,4]
        end_coords = [7,1,1]

        true_path = [[5,3,3],[6,2,2]]

        path = self.test_bishop.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    def test_gen_path_test__x_yz(self):
        start_coords = [4,4,4]
        end_coords = [1,1,7]

        true_path = [[3,3,5],[2,2,6]]

        path = self.test_bishop.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    def test_check_attack(self):
        start_coords = [0,0,0]
        end_coords = [7,7,7]

        self.assertTrue(self.test_bishop.is_valid_attack(start_coords, end_coords))

if __name__ == '__main__':
    unittest.main()