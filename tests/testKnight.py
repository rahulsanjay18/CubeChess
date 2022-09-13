import unittest
from pieces.knight import Knight
from board import Board
import random

class testKnight(unittest.TestCase):
    def setUp(self) -> None:
        self.test_knight = Knight()

    # (1,1,2)
    def test_valid_move_112(self):
        start_coords = [4,4,4]
        end_coords = [5,5,6]

        self.assertTrue(self.test_knight.is_valid_move(start_coords, end_coords))
    
    # (-1,1,2)
    def test_valid_move__112(self):
        start_coords = [4,4,4]
        end_coords = [3,5,6]

        self.assertTrue(self.test_knight.is_valid_move(start_coords, end_coords))
    
    # (-1,-1,2)
    def test_valid_move__1_12(self):
        start_coords = [4,4,4]
        end_coords = [3,3,6]

        self.assertTrue(self.test_knight.is_valid_move(start_coords, end_coords))

    # (1,-1,2)
    def test_valid_move_1_12(self):
        start_coords = [4,4,4]
        end_coords = [5,3,6]

        self.assertTrue(self.test_knight.is_valid_move(start_coords, end_coords))
###########
    # (1,1,-2)
    def test_valid_move_11_2(self):
        start_coords = [4,4,4]
        end_coords = [5,5,2]

        self.assertTrue(self.test_knight.is_valid_move(start_coords, end_coords))
    
    # (-1,1,-2)
    def test_valid_move__11_2(self):
        start_coords = [4,4,4]
        end_coords = [3,5,2]

        self.assertTrue(self.test_knight.is_valid_move(start_coords, end_coords))
    
    # (-1,-1,-2)
    def test_valid_move__1_1_2(self):
        start_coords = [4,4,4]
        end_coords = [3,3,2]

        self.assertTrue(self.test_knight.is_valid_move(start_coords, end_coords))

    # (1,-1,-2)
    def test_valid_move_1_1_2(self):
        start_coords = [4,4,4]
        end_coords = [5,3,2]

        self.assertTrue(self.test_knight.is_valid_move(start_coords, end_coords))
##########
    # (1,2,1)
    def test_valid_move_121(self):
        start_coords = [4,4,4]
        end_coords = [5,6,5]

        self.assertTrue(self.test_knight.is_valid_move(start_coords, end_coords))
    
    # (-1,2,1)
    def test_valid_move__121(self):
        start_coords = [4,4,4]
        end_coords = [3,6,5]

        self.assertTrue(self.test_knight.is_valid_move(start_coords, end_coords))
    
    # (-1,2,-1)
    def test_valid_move__12_1(self):
        start_coords = [4,4,4]
        end_coords = [3,6,3]

        self.assertTrue(self.test_knight.is_valid_move(start_coords, end_coords))

    # (1,2,-1)
    def test_valid_move_12_1(self):
        start_coords = [4,4,4]
        end_coords = [3,6,3]

        self.assertTrue(self.test_knight.is_valid_move(start_coords, end_coords))
##############
    # (1,-2,1)
    def test_valid_move_1_21(self):
        start_coords = [4,4,4]
        end_coords = [5,2,5]

        self.assertTrue(self.test_knight.is_valid_move(start_coords, end_coords))
    
    # (-1,-2,1)
    def test_valid_move__1_21(self):
        start_coords = [4,4,4]
        end_coords = [3,2,5]

        self.assertTrue(self.test_knight.is_valid_move(start_coords, end_coords))
    
    # (-1,-2,-1)
    def test_valid_move__1_2_1(self):
        start_coords = [4,4,4]
        end_coords = [3,2,3]

        self.assertTrue(self.test_knight.is_valid_move(start_coords, end_coords))

    # (1,-2,-1)
    def test_valid_move_1_2_1(self):
        start_coords = [4,4,4]
        end_coords = [5,2,3]

        self.assertTrue(self.test_knight.is_valid_move(start_coords, end_coords))
    
    ###################
    # (2,1,1)
    def test_valid_move_211(self):
        start_coords = [4,4,4]
        end_coords = [6,5,5]

        self.assertTrue(self.test_knight.is_valid_move(start_coords, end_coords))
    
    # (2,-1,1)
    def test_valid_move_2_11(self):
        start_coords = [4,4,4]
        end_coords = [6,3,5]

        self.assertTrue(self.test_knight.is_valid_move(start_coords, end_coords))
    
    # (2,-1,-1)
    def test_valid_move_2_1_1(self):
        start_coords = [4,4,4]
        end_coords = [6,3,3]

        self.assertTrue(self.test_knight.is_valid_move(start_coords, end_coords))

    # (2,1,-1)
    def test_valid_move_21_1(self):
        start_coords = [4,4,4]
        end_coords = [6,5,3]

        self.assertTrue(self.test_knight.is_valid_move(start_coords, end_coords))
    #############
    # (-2,1,1)
    def test_valid_move__211(self):
        start_coords = [4,4,4]
        end_coords = [2,5,5]

        self.assertTrue(self.test_knight.is_valid_move(start_coords, end_coords))
    
    # (-2,-1,1)
    def test_valid_move__2_11(self):
        start_coords = [4,4,4]
        end_coords = [2,3,5]

        self.assertTrue(self.test_knight.is_valid_move(start_coords, end_coords))
    
    # (-2,-1,-1)
    def test_valid_move__2_1_1(self):
        start_coords = [4,4,4]
        end_coords = [2,3,3]

        self.assertTrue(self.test_knight.is_valid_move(start_coords, end_coords))

    # (-2,1,-1)
    def test_valid_move__21_1(self):
        start_coords = [4,4,4]
        end_coords = [2,5,3]

        self.assertTrue(self.test_knight.is_valid_move(start_coords, end_coords))
    
    ###################
    
    def test_gen_path_test(self):
        start_coords = [4,4,4]
        end_coords = [2,5,3]
        callable = self.test_knight.gen_path_step
        self.assertRaises(Exception, callable, start_coords, end_coords)


    def test_check_attack(self):
        start_coords = [4,4,4]
        end_coords = [2,5,3]

        self.assertTrue(self.test_knight.is_valid_attack(start_coords, end_coords))

if __name__ == '__main__':
    unittest.main()