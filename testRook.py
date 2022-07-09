import unittest
from pieces import Rook
from board import Board
import random

class testRook(unittest.TestCase):
    def setUp(self) -> None:
        self.test_rook = Rook()
    
    def test_x_valid_move(self):
        x = random.randint(0, 7)
        new_x = random.randint(0, 7)
        while(x == new_x):
            new_x = random.randint(0, 7)
        y = random.randint(0, 7)
        z = random.randint(0, 7)
        
        self.assertTrue(self.test_rook.is_valid_move((x, y, z), (new_x, y, z)))
    
    def test_y_valid_move(self):
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        new_y = random.randint(0, 7)
        while(y == new_y):
            new_y = random.randint(0, 7)
        z = random.randint(0, 7)
        
        self.assertTrue(self.test_rook.is_valid_move((x, y, z), (x, new_y, z)))

    def test_z_valid_move(self):
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        z = random.randint(0, 7)
        new_z = random.randint(0, 7)
        while(z == new_z):
            new_z = random.randint(0, 7)

        self.assertTrue(self.test_rook.is_valid_move((x, y, z), (x, y, new_z)))

    def test_did_not_move(self):
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        z = random.randint(0, 7)

        self.assertFalse(self.test_rook.is_valid_move((x, y, z), (x, y, z)))

    def test_invalid_move(self):
        x = random.randint(0, 7)
        new_x = random.randint(0, 7)
        while(x == new_x):
            new_x = random.randint(0, 7)
        y = random.randint(0, 7)
        z = random.randint(0, 7)

        self.assertFalse(self.test_rook.is_valid_move((x, y, z), (new_x, (y+1) % 8, z)))
    
    def test_out_of_bounds(self):
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        z = random.randint(0, 7)

        self.assertFalse(self.test_rook.is_valid_move((x, y, z), (9, y, z)))

    def test_gen_path_step(self):
        x = 0
        new_x = 4
        y = random.randint(0, 7)
        z = random.randint(0, 7)

        result_path = [(1, y, z), (2, y, z), (3, y, z), (4, y, z)]
        path = self.test_rook.gen_path_step((x, y, z), (new_x, y, z))

        self.assertEqual(result_path, path)

        

if __name__ == '__main__':
    unittest.main()