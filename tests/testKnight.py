import unittest
from pieces.knight import Knight
from board import Board
import random

class testKnight(unittest.TestCase):
    def setUp(self) -> None:
        self.test_knight = Knight()


if __name__ == '__main__':
    unittest.main()