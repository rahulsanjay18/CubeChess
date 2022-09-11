import unittest
from pieces.paladin import Paladin
from board import Board
import random

class testPaladin(unittest.TestCase):
    def setUp(self) -> None:
        self.test_paladin = Paladin()


if __name__ == '__main__':
    unittest.main()