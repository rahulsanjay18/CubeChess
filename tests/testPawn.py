import unittest
from pieces.pawn import Pawn
import random

class testPawn(unittest.TestCase):
    def setUp(self) -> None:
        self.wht_pawn = Pawn()
        self.blk_pawn = Pawn(is_white=False)
        return super().setUp()

    def atk_wht_pawn_l(self):
        st = [0, 1, 0]
        ed = [0, 2, 0]
        for i in range(0, 8):
            for j in range(0, 8):
                st[0] = i
                ed[0] = i

                st[2] = j
                ed[2] = j
                self.assertTrue(self.wht_pawn.is_valid_move(st, ed))
    
    def atk_wht_pawn_r(self):
        st = [0, 1, 0]
        ed = [0, 3, 0]
        for i in range(0, 8):
            for j in range(0, 8):
                st[0] = i
                ed[0] = i

                st[2] = j
                ed[2] = j
                self.assertTrue(self.wht_pawn.is_valid_move(st, ed))
    
    def atk_blk_pawn_l(self):
        st = [0, 7, 0]
        ed = [0, 6, 0]
        for i in range(0, 8):
            for j in range(0, 8):
                st[0] = i
                ed[0] = i

                st[2] = j
                ed[2] = j
                self.assertTrue(self.blk_pawn.is_valid_move(st, ed))
    
    def atk_blk_pawn_r(self):
        st = [0, 7, 0]
        ed = [0, 5, 0]
        for i in range(0, 8):
            for j in range(0, 8):
                st[0] = i
                ed[0] = i

                st[2] = j
                ed[2] = j
                self.assertTrue(self.blk_pawn.is_valid_move(st, ed))