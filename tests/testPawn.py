import unittest
from board import Board
import random

class testPawn(unittest.TestCase):
    def setUp(self) -> None:
        self.test_board = Board()
        return super().setUp()