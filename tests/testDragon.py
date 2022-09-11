import unittest
from pieces.dragon import Dragon
from board import Board
import random

class testDragon(unittest.TestCase):
    def setUp(self) -> None:
        self.test_dragon = Dragon()

    # (2,2,1)
    def test_valid_move_221(self):
        start_coords = [4,4,4]
        end_coords = [6,6,5]

        self.assertTrue(self.test_dragon.is_valid_move(start_coords, end_coords))
    
    # (1,2,2)
    def test_valid_move_112(self):
        start_coords = [4,4,4]
        end_coords = [5,6,6]

        self.assertTrue(self.test_dragon.is_valid_move(start_coords, end_coords))

    # (2,1,2)
    def test_valid_move_212(self):
        start_coords = [4,4,4]
        end_coords = [6,5,6]

        self.assertTrue(self.test_dragon.is_valid_move(start_coords, end_coords))
#########
    # (-2,-2,-1)
    def test_valid_move__2_2_1(self):
        start_coords = [4,4,4]
        end_coords = [2,2,3]

        self.assertTrue(self.test_dragon.is_valid_move(start_coords, end_coords))
    
    # (-1,-2,-2)
    def test_valid_move__1_2_2(self):
        start_coords = [4,4,4]
        end_coords = [3,2,2]

        self.assertTrue(self.test_dragon.is_valid_move(start_coords, end_coords))

    # (-2,-1,-2)
    def test_valid_move__2_1_2(self):
        start_coords = [4,4,4]
        end_coords = [2,3,2]

        self.assertTrue(self.test_dragon.is_valid_move(start_coords, end_coords))
#########    
    # (-2,2,1)
    def test_valid_move__221(self):
        start_coords = [4,4,4]
        end_coords = [2,6,5]

        self.assertTrue(self.test_dragon.is_valid_move(start_coords, end_coords))
    
    # (1,-2,2)
    def test_valid_move_1_22(self):
        start_coords = [4,4,4]
        end_coords = [5,2,6]

        self.assertTrue(self.test_dragon.is_valid_move(start_coords, end_coords))

    # (-2,1,2)
    def test_valid_move__212(self):
        start_coords = [4,4,4]
        end_coords = [2,5,6]

        self.assertTrue(self.test_dragon.is_valid_move(start_coords, end_coords))
#########    
    # (2,-2,-1)
    def test_valid_move_2_2_1(self):
        start_coords = [4,4,4]
        end_coords = [2,6,5]

        self.assertTrue(self.test_dragon.is_valid_move(start_coords, end_coords))
    
    # (-1,2,-2)
    def test_valid_move__12_2(self):
        start_coords = [4,4,4]
        end_coords = [3,6,2]

        self.assertTrue(self.test_dragon.is_valid_move(start_coords, end_coords))

    # (2,-1,-2)
    def test_valid_move_2_1_2(self):
        start_coords = [4,4,4]
        end_coords = [6,3,2]

        self.assertTrue(self.test_dragon.is_valid_move(start_coords, end_coords))
#########    
    # (2,-2,1)
    def test_valid_move_2_21(self):
        start_coords = [4,4,4]
        end_coords = [6,2,5]

        self.assertTrue(self.test_dragon.is_valid_move(start_coords, end_coords))
    
    # (1,2,-2)
    def test_valid_move_12_2(self):
        start_coords = [4,4,4]
        end_coords = [5,6,2]

        self.assertTrue(self.test_dragon.is_valid_move(start_coords, end_coords))

    # (2,1,-2)
    def test_valid_move_21_2(self):
        start_coords = [4,4,4]
        end_coords = [6,5,2]

        self.assertTrue(self.test_dragon.is_valid_move(start_coords, end_coords))
#########
    # (-2,2,-1)
    def test_valid_move__22_1(self):
        start_coords = [4,4,4]
        end_coords = [2,6,3]

        self.assertTrue(self.test_dragon.is_valid_move(start_coords, end_coords))
    
    # (-1,-2,2)
    def test_valid_move__1_22(self):
        start_coords = [4,4,4]
        end_coords = [3,2,6]

        self.assertTrue(self.test_dragon.is_valid_move(start_coords, end_coords))

    # (-2,-1,2)
    def test_valid_move__2_12(self):
        start_coords = [4,4,4]
        end_coords = [2,3,6]

        self.assertTrue(self.test_dragon.is_valid_move(start_coords, end_coords))
#########
    # (2,2,-1)
    def test_valid_move_22_1(self):
        start_coords = [4,4,4]
        end_coords = [6,6,3]

        self.assertTrue(self.test_dragon.is_valid_move(start_coords, end_coords))
    
    # (-1,2,2)
    def test_valid_move__122(self):
        start_coords = [4,4,4]
        end_coords = [3,6,6]

        self.assertTrue(self.test_dragon.is_valid_move(start_coords, end_coords))

    # (2,-1,2)
    def test_valid_move_2_12(self):
        start_coords = [4,4,4]
        end_coords = [6,3,6]

        self.assertTrue(self.test_dragon.is_valid_move(start_coords, end_coords))
#########
    # (-2,-2,1)
    def test_valid_move__2_21(self):
        start_coords = [4,4,4]
        end_coords = [2,2,5]

        self.assertTrue(self.test_dragon.is_valid_move(start_coords, end_coords))
    
    # (1,-2,-2)
    def test_valid_move_1_2_2(self):
        start_coords = [4,4,4]
        end_coords = [5,2,2]

        self.assertTrue(self.test_dragon.is_valid_move(start_coords, end_coords))

    # (-2,1,-2)
    def test_valid_move__21_2(self):
        start_coords = [4,4,4]
        end_coords = [2,5,2]

        self.assertTrue(self.test_dragon.is_valid_move(start_coords, end_coords))
#########
    def test_gen_path_test(self):
        start_coords = [4,4,4]
        end_coords = [6,5,6]
        callable = self.test_dragon.gen_path_step
        self.assertRaises(Exception, callable, start_coords, end_coords)


    def test_check_attack(self):
        start_coords = [4,4,4]
        end_coords = [6,5,6]

        self.assertTrue(self.test_dragon.is_valid_attack(start_coords, end_coords))

if __name__ == '__main__':
    unittest.main()