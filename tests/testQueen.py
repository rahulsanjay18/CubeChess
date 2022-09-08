import unittest
from pieces.queen import Queen
from board import Board
import random

class testQueen(unittest.TestCase):
    def setUp(self) -> None:
        self.test_queen = Queen()
    
    def test_x_valid_move(self):
        x = random.randint(0, 7)
        new_x = random.randint(0, 7)
        while(x == new_x):
            new_x = random.randint(0, 7)
        y = random.randint(0, 7)
        z = random.randint(0, 7)
        
        self.assertTrue(self.test_queen.is_valid_move([x, y, z], [new_x, y, z]))
    
    def test_y_valid_move(self):
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        new_y = random.randint(0, 7)
        while(y == new_y):
            new_y = random.randint(0, 7)
        z = random.randint(0, 7)
        
        self.assertTrue(self.test_queen.is_valid_move([x, y, z], [x, new_y, z]))

    def test_z_valid_move(self):
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        z = random.randint(0, 7)
        new_z = random.randint(0, 7)
        while(z == new_z):
            new_z = random.randint(0, 7)

        self.assertTrue(self.test_queen.is_valid_move([x, y, z], [x, y, new_z]))

    def test_did_not_move(self):
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        z = random.randint(0, 7)

        self.assertFalse(self.test_queen.is_valid_move([x, y, z], [x, y, z]))

    def test_invalid_move_straight(self):
        x = random.randint(0, 7)
        new_x = random.randint(0, 7)
        while(x == new_x):
            new_x = random.randint(0, 7)
        y = random.randint(0, 7)
        z = random.randint(0, 7)

        self.assertFalse(self.test_queen.is_valid_move([x, y, z], [new_x, (y+1) % 8, z]))
    
    def test_out_of_bounds(self):
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        z = random.randint(0, 7)

        self.assertFalse(self.test_queen.is_valid_move([x, y, z], [9, y, z]))

    def test_gen_path_step(self):
        x = 0
        new_x = 4
        y = random.randint(0, 7)
        z = random.randint(0, 7)

        result_path = [[1, y, z], [2, y, z], [3, y, z]]
        path = self.test_queen.gen_path_step([x, y, z], [new_x, y, z])

        self.assertEqual(result_path, path)

    def test_check_attack_straight(self):
        x = random.randint(0, 7)
        new_x = random.randint(0, 7)
        while(x == new_x):
            new_x = random.randint(0, 7)
        y = random.randint(0, 7)
        z = random.randint(0, 7)
        
        self.assertTrue(self.test_queen.is_valid_attack([x, y, z], [new_x, y, z]))

    # (1,1,0)
    def test_valid_move_xy(self):
        start_coords = [4,4,4]
        end_coords = [7,7,4]

        self.assertTrue(self.test_queen.is_valid_move(start_coords, end_coords))
    
    # (1,0,1)
    def test_valid_move_xz(self):
        start_coords = [4,4,4]
        end_coords = [7,4,7]

        self.assertTrue(self.test_queen.is_valid_move(start_coords, end_coords))
    
    # (0,1,1)
    def test_valid_move_yz(self):
        start_coords = [4,4,4]
        end_coords = [4,7,7]

        self.assertTrue(self.test_queen.is_valid_move(start_coords, end_coords))
    
    # (-1,1,0)
    def test_valid_move__xy(self):
        start_coords = [4,4,4]
        end_coords = [1,7,4]

        self.assertTrue(self.test_queen.is_valid_move(start_coords, end_coords))
    
    # (-1,0,1)
    def test_valid_move__xz(self):
        start_coords = [4,4,4]
        end_coords = [1,4,7]

        self.assertTrue(self.test_queen.is_valid_move(start_coords, end_coords))
    
    # (0,-1,1)
    def test_valid_move__yz(self):
        start_coords = [4,4,4]
        end_coords = [4,1,7]

        self.assertTrue(self.test_queen.is_valid_move(start_coords, end_coords))
    
    # (1,-1,0)
    def test_valid_move_x_y(self):
        start_coords = [4,4,4]
        end_coords = [7,1,4]

        self.assertTrue(self.test_queen.is_valid_move(start_coords, end_coords))
    
    # (1,0,-1)
    def test_valid_move_x_z(self):
        start_coords = [4,4,4]
        end_coords = [7,4,1]

        self.assertTrue(self.test_queen.is_valid_move(start_coords, end_coords))
    
    # (0,1,-1)
    def test_valid_move_y_z(self):
        start_coords = [4,4,4]
        end_coords = [4,7,1]

        self.assertTrue(self.test_queen.is_valid_move(start_coords, end_coords))
    
    # (-1,-1,0)
    def test_valid_move_xy(self):
        start_coords = [4,4,4]
        end_coords = [1,1,4]

        self.assertTrue(self.test_queen.is_valid_move(start_coords, end_coords))
    
    # (-1,0,-1)
    def test_valid_move_xz(self):
        start_coords = [4,4,4]
        end_coords = [1,4,1]

        self.assertTrue(self.test_queen.is_valid_move(start_coords, end_coords))
    
    # (0,-1,-1)
    def test_valid_move_yz(self):
        start_coords = [4,4,4]
        end_coords = [4,1,1]

        self.assertTrue(self.test_queen.is_valid_move(start_coords, end_coords))
    
    def test_invalid_move_edge(self):
        start_coords = [0, 0, 0]
        end_coords = [0, 1, 2]

        self.assertFalse(self.test_queen.is_valid_move(start_coords, end_coords))

    # (1,1,0)
    def test_gen_path_test_xy(self):
        start_coords = [4,4,4]
        end_coords = [7,7,4]

        true_path = [[5,5,4],[6,6,4]]

        path = self.test_queen.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)

    # (1,0,1)
    def test_gen_path_test_xz(self):
        start_coords = [4,4,4]
        end_coords = [7,4,7]

        true_path = [[5,4,5],[6,4,6]]

        path = self.test_queen.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    # (0,1,1)
    def test_gen_path_test_yz(self):
        start_coords = [4,4,4]
        end_coords = [4,7,7]

        true_path = [[4,5,5],[4,6,6]]

        path = self.test_queen.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    # (-1,1,0)
    def test_gen_path_test__xy(self):
        start_coords = [4,4,4]
        end_coords = [1,7,4]

        true_path = [[3,5,4],[2,6,4]]

        path = self.test_queen.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)

    # (-1,0,1)
    def test_gen_path_test__xz(self):
        start_coords = [4,4,4]
        end_coords = [1,4,7]

        true_path = [[3,4,5],[2,4,6]]

        path = self.test_queen.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    # (0,-1,1)
    def test_gen_path_test__yz(self):
        start_coords = [4,4,4]
        end_coords = [4,1,7]

        true_path = [[4,3,5],[4,2,6]]

        path = self.test_queen.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    # (1,-1,0)
    def test_gen_path_test_x_y(self):
        start_coords = [4,4,4]
        end_coords = [7,1,4]

        true_path = [[5,3,4],[6,2,4]]

        path = self.test_queen.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)

    # (1,0,-1)
    def test_gen_path_test_x_z(self):
        start_coords = [4,4,4]
        end_coords = [7,4,1]

        true_path = [[5,4,3],[6,4,2]]

        path = self.test_queen.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    # (0,1,-1)
    def test_gen_path_test_y_z(self):
        start_coords = [4,4,4]
        end_coords = [4,7,1]

        true_path = [[4,5,3],[4,6,2]]

        path = self.test_queen.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    # (-1,-1,0)
    def test_gen_path_test__x_y(self):
        start_coords = [4,4,4]
        end_coords = [1,1,4]

        true_path = [[3,3,4],[2,2,4]]

        path = self.test_queen.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)

    # (-1,0,-1)
    def test_gen_path_test__x_z(self):
        start_coords = [4,4,4]
        end_coords = [1,4,1]

        true_path = [[3,4,3],[2,4,2]]

        path = self.test_queen.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    # (0,-1,-1)
    def test_gen_path_test__y_z(self):
        start_coords = [4,4,4]
        end_coords = [4,1,1]

        true_path = [[4,3,3],[4,2,2]]

        path = self.test_queen.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    def test_check_attack_edge(self):
        start_coords = [0,0,0]
        end_coords = [7,7,0]

        self.assertTrue(self.test_queen.is_valid_attack(start_coords, end_coords))

    def test_valid_move_xyz(self):
        start_coords = [4,4,4]
        end_coords = [7,7,7]

        self.assertTrue(self.test_queen.is_valid_move(start_coords, end_coords))
    
    def test_valid_move__x_y_z(self):
        start_coords = [4,4,4]
        end_coords = [0,0,0]

        self.assertTrue(self.test_queen.is_valid_move(start_coords, end_coords))
    
    def test_valid_move_xy_z(self):
        start_coords = [4,4,4]
        end_coords = [7,7,1]

        self.assertTrue(self.test_queen.is_valid_move(start_coords, end_coords))
    
    def test_valid_move_x_yz(self):
        start_coords = [4,4,4]
        end_coords = [7,1,7]

        self.assertTrue(self.test_queen.is_valid_move(start_coords, end_coords))

    def test_valid_move__xyz(self):
        start_coords = [4,4,4]
        end_coords = [1,7,7]

        self.assertTrue(self.test_queen.is_valid_move(start_coords, end_coords))

    def test_valid_move__xy_z(self):
        start_coords = [4,4,4]
        end_coords = [1,7,1]

        self.assertTrue(self.test_queen.is_valid_move(start_coords, end_coords))

    def test_valid_move_x_y_z(self):
        start_coords = [4,4,4]
        end_coords = [7,1,1]

        self.assertTrue(self.test_queen.is_valid_move(start_coords, end_coords))
    
    def test_valid_move__x_yz(self):
        start_coords = [4,4,4]
        end_coords = [1,1,7]

        self.assertTrue(self.test_queen.is_valid_move(start_coords, end_coords))

    def test_invalid_move_vert(self):
        start_coords = [0, 0, 0]
        end_coords = [3, 4, 2]

        self.assertFalse(self.test_queen.is_valid_move(start_coords, end_coords))
    
    def test_gen_path_test_xyz(self):
        start_coords = [4,4,4]
        end_coords = [7,7,7]

        true_path = [[5,5,5],[6,6,6]]

        path = self.test_queen.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    def test_gen_path_test__x_y_z(self):
        start_coords = [4,4,4]
        end_coords = [0,0,0]

        true_path = [[3,3,3],[2,2,2],[1,1,1]]

        path = self.test_queen.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    def test_gen_path_test_xy_z(self):
        start_coords = [4,4,4]
        end_coords = [7,7,1]

        true_path = [[5,5,3],[6,6,2]]

        path = self.test_queen.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    def test_gen_path_test_x_yz(self):
        start_coords = [4,4,4]
        end_coords = [7,1,7]

        true_path = [[5,3,5],[6,2,6]]

        path = self.test_queen.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)

    def test_gen_path_test__xyz(self):
        start_coords = [4,4,4]
        end_coords = [1,7,7]

        true_path = [[3,5,5],[2,6,6]]

        path = self.test_queen.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    def test_gen_path_test__xy_z(self):
        start_coords = [4,4,4]
        end_coords = [1,7,1]

        true_path = [[3,5,3],[2,6,2]]

        path = self.test_queen.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)

    def test_gen_path_test_x_y_z(self):
        start_coords = [4,4,4]
        end_coords = [7,1,1]

        true_path = [[5,3,3],[6,2,2]]

        path = self.test_queen.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    def test_gen_path_test__x_yz(self):
        start_coords = [4,4,4]
        end_coords = [1,1,7]

        true_path = [[3,3,5],[2,2,6]]

        path = self.test_queen.gen_path_step(start_coords, end_coords)

        self.assertEqual(true_path, path)
    
    def test_check_attack_vert(self):
        start_coords = [0,0,0]
        end_coords = [7,7,7]

        self.assertTrue(self.test_queen.is_valid_attack(start_coords, end_coords))

if __name__ == '__main__':
    unittest.main()