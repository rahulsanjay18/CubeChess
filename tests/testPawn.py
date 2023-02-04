import unittest
from pieces.pawn import Pawn
import random

class testPawn(unittest.TestCase):
    def setUp(self) -> None:
        self.wht_pawn = Pawn()
        self.blk_pawn = Pawn(is_white=False)
        return super().setUp()

    def test_wht_pawn_1(self):
        st = [0, 1, 0]
        ed = [0, 2, 0]

        around = [1, 0, -1]
        for i in range(0, 8):
            for j in range(0, 8):
                for x in around:
                    for z in around:
                        st[0] = i
                        ed[0] = i + x

                        st[2] = j
                        ed[2] = j + z
                        if 0 <= ed[0] < 8 and 0 <= ed[2] < 8:
                            self.assertTrue(self.wht_pawn.is_valid_move(st, ed))
    
    def test_wht_pawn_2(self):
        st = [0, 1, 0]
        ed = [0, 3, 0]
        for i in range(0, 8):
            for j in range(0, 8):
                st[0] = i
                ed[0] = i

                st[2] = j
                ed[2] = j
                self.assertTrue(self.wht_pawn.is_valid_move(st, ed))
    
    def test_blk_pawn_1(self):
        st = [0, 6, 0]
        ed = [0, 5, 0]
        around = [1, 0, -1]
        for i in range(0, 8):
            for j in range(0, 8):
                for x in around:
                    for z in around:
                        st[0] = i
                        ed[0] = i + x

                        st[2] = j
                        ed[2] = j + z
                        if 0 <= ed[0] < 8 and 0 <= ed[2] < 8:
                            self.assertTrue(self.blk_pawn.is_valid_move(st, ed))
    
    def test_blk_pawn_2(self):
        st = [0, 6, 0]
        ed = [0, 4, 0]
        for i in range(0, 8):
            for j in range(0, 8):
                st[0] = i
                ed[0] = i

                st[2] = j
                ed[2] = j
                self.assertTrue(self.blk_pawn.is_valid_move(st, ed))
    
    # probably make another set of tests where the pawn moves fail
    
if __name__ == '__main__':
    unittest.main()