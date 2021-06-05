import board as b
import piece as p

class Game:
    
    is_white_turn = True

    def __init__():
        self.board = b.Board()
    
    '''
    Initializes the board with the starting pieces
    '''
    def initialize(self):
        king_w = p.King()
        king_b = p.King(False)

        queen_w = p.Queen()
        queen_b = p.Queen(False)

        bishop_w1 = p.Bishop()
        bishop_w2 = p.Bishop()
        bishop_b1 = p.Bishop(False)
        bishop_b2 = p.Bishop(False)

        priest_w1 = p.Priest()
        priest_w2 = p.Priest()
        priest_b1 = p.Priest(False)
        priest_b2 = p.Priest(False)

        paladin_w1 = p.Paladin()
        paladin_w2 = p.Paladin()
        paladin_b1 = p.Paladin(False)
        paladin_b2 = p.Paladin(False)

        rook_w1 = p.Rook()
        rook_w2 = p.Rook()
        rook_b1 = p.Rook(False)
        rook_b2 = p.Rook(False)

        pawns_w = []
        pawns_b = []

        for i in range(18):
            pawns_w.append(p.Pawn())

        for i in range(18):
            pawns_b.append(p.Pawn(False))

        self.board.insert((7, 0, 0), king_w)
        self.board.insert((6, 0, 0), king_w)
        self.board.insert((5, 0, 0), king_w)
        self.board.insert((4, 0, 0), king_w)
        self.board.insert((3, 0, 0), king_w)
        self.board.insert((2, 0, 0), king_w)
        self.board.insert((1, 0, 0), king_w)
        self.board.insert((0, 0, 0), king_w)
        
        for i in range(8):
            self.board.insert((i, 0, 1), pawns_w[i])

        for i in range(8):
            self.board.insert((i, 1, 0), pawns_w[i+8])

        self.board.insert((3, 1, 1), pawns_w[16])
        self.board.insert((4, 1, 1), pawns_w[17])


    '''
    This is done in a few steps:
    
    1. Find the piece on the board
    2. Take that piece object and find if its a legal move
    3. If legal, move the piece, if not return False
    4. Find that piece's range of movement
    5. If Rook, Bishop, Priest, Pawn or Queen, we need to remove invalid moves
    6. Remove moves by just iterating, assign the leftover moves to the piece
    7. Return True

    '''
    def make_move(x, y, z, x_p, y_p, z_p):
        pass
