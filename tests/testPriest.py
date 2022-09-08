import unittest
from pieces.priest import Priest
from board import Board
import random

class testPriest(unittest.TestCase):
    def setUp(self) -> None:
        self.test_priest = Priest()

    # (1,1,0)
    def test_valid_move_xy(self):
        start_coords = [4,4,4]
        end_coords = [7,7,4]

        self.assertTrue(self.test_priest.is_valid_move(start_coords, end_coords))
    
    # (1,0,1)
    def test_valid_move_xz(self):
        start_coords = [4,4,4]
        end_coords = [7,4,7]

        self.assertTrue(self.test_priest.is_valid_move(start_coords, end_coords))
    
    # (0,1,1)
    def test_valid_move_yz(self):
        start_coords = [4,4,4]
        end_coords = [4,7,7]

        self.assertTrue(self.test_priest.is_valid_move(start_coords, end_coords))
    
    # (-1,1,0)
    def test_valid_move__xy(self):
        start_coords = [4,4,4]
        end_coords = [1,7,4]

        self.assertTrue(self.test_priest.is_valid_move(start_coords, end_coords))
    
    # (-1,0,1)
    def test_valid_move__xz(self):
        start_coords = [4,4,4]
        end_coords = [1,4,7]

        self.assertTrue(self.test_priest.is_valid_move(start_coords, end_coords))
    
    # (0,-1,1)
    def test_valid_move__yz(self):
        start_coords = [4,4,4]
        end_coords = [4,1,7]

        self.assertTrue(self.test_priest.is_valid_move(start_coords, end_coords))
    
    # (1,-1,0)
    def test_valid_move_x_y(self):
        start_coords = [4,4,4]
        end_coords = [7,1,4]

        self.assertTrue(self.test_priest.is_valid_move(start_coords, end_coords))
    
    # (1,0,-1)
    def test_valid_move_x_z(self):
        start_coords = [4,4,4]
        end_coords = [7,4,1]

        self.assertTrue(self.test_priest.is_valid_move(start_coords, end_coords))
    
    # (0,1,-1)
    def test_valid_move_y_z(self):
        start_coords = [4,4,4]
        end_coords = [4,7,1]

        self.assertTrue(self.test_priest.is_valid_move(start_coords, end_coords))
    
    # (-1,-1,0)
    def test_valid_move_xy(self):
        start_coords = [4,4,4]
        end_coords = [1,1,4]

        self.assertTrue(self.test_priest.is_valid_move(start_coords, end_coords))
    
    # (-1,0,-1)
    def test_valid_move_xz(self):
        start_coords = [4,4,4]
        end_coords = [1,4,1]

        self.assertTrue(self.test_priest.is_valid_move(start_coords, end_coords))
    
    # (0,-1,-1)
    def test_valid_move_yz(self):
        start_coords = [4,4,4]
        end_coords = [4,1,1]

        self.assertTrue(self.test_priest.is_valid_move(start_coords, end_coords))
    
    def test_invalid_move(self):
        start_coords = [0, 0, 0]
        end_coords = [3, 3, 3]

        self.assertFalse(self.test_priest.is_valid_move(start_coords, end_coords))

    # (1,1,0)
    def test_gen_path_test_xy(self):
        start_coords = [4,4,4]
        end_coords = [7,7,4]

        true_path = [[5,5,4],[6,6,4]]

        path = self.test_priest.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)

    # (1,0,1)
    def test_gen_path_test_xz(self):
        start_coords = [4,4,4]
        end_coords = [7,4,7]

        true_path = [[5,4,5],[6,4,6]]

        path = self.test_priest.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    # (0,1,1)
    def test_gen_path_test_yz(self):
        start_coords = [4,4,4]
        end_coords = [4,7,7]

        true_path = [[4,5,5],[4,6,6]]

        path = self.test_priest.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    # (-1,1,0)
    def test_gen_path_test__xy(self):
        start_coords = [4,4,4]
        end_coords = [1,7,4]

        true_path = [[3,5,4],[2,6,4]]

        path = self.test_priest.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)

    # (-1,0,1)
    def test_gen_path_test__xz(self):
        start_coords = [4,4,4]
        end_coords = [1,4,7]

        true_path = [[3,4,5],[2,4,6]]

        path = self.test_priest.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    # (0,-1,1)
    def test_gen_path_test__yz(self):
        start_coords = [4,4,4]
        end_coords = [4,1,7]

        true_path = [[4,3,5],[4,2,6]]

        path = self.test_priest.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    # (1,-1,0)
    def test_gen_path_test_x_y(self):
        start_coords = [4,4,4]
        end_coords = [7,1,4]

        true_path = [[5,3,4],[6,2,4]]

        path = self.test_priest.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)

    # (1,0,-1)
    def test_gen_path_test_x_z(self):
        start_coords = [4,4,4]
        end_coords = [7,4,1]

        true_path = [[5,4,3],[6,4,2]]

        path = self.test_priest.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    # (0,1,-1)
    def test_gen_path_test_y_z(self):
        start_coords = [4,4,4]
        end_coords = [4,7,1]

        true_path = [[4,5,3],[4,6,2]]

        path = self.test_priest.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    # (-1,-1,0)
    def test_gen_path_test__x_y(self):
        start_coords = [4,4,4]
        end_coords = [1,1,4]

        true_path = [[3,3,4],[2,2,4]]

        path = self.test_priest.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)

    # (-1,0,-1)
    def test_gen_path_test__x_z(self):
        start_coords = [4,4,4]
        end_coords = [1,4,1]

        true_path = [[3,4,3],[2,4,2]]

        path = self.test_priest.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    # (0,-1,-1)
    def test_gen_path_test__y_z(self):
        start_coords = [4,4,4]
        end_coords = [4,1,1]

        true_path = [[4,3,3],[4,2,2]]

        path = self.test_priest.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    def test_check_attack(self):
        start_coords = [0,0,0]
        end_coords = [7,7,0]

        self.assertTrue(self.test_priest.is_valid_attack(start_coords, end_coords))

if __name__ == '__main__':
    unittest.main()