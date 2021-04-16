class Piece:
    """"
    Represents a piece superclass that each piece inherits from. Each piece has the following functions:

    checkMove: Checks if a move ordered by the piece is valid.
    Piece Representation: the letter representing the piece.
    current position: where on the board is the piece right now
    nextLegalMove: List of legal moves the thing can make

    """


    def __init__(self):
        self.piece_representation = 'x'
        self.x,self.y, self.z = -1, -1, -1
        self.is_white = True

    def check_move():
        raise NotImplementedError("Subclass must implement abstract method")
    def __genNextMoves():
        raise NotImplementedError("Subclass must implement abstract method")

class Rook:
    def __init__(self, x=-1, y=-1, z=-1, is_white=True):
        super().__init__()
        self.piece_representation = 'R'
        self.x, self.y, self.z = x, y, z
        self.is_white = is_white

    def check_move(x, y, z):
        if !(isinstance(x, int) and isinstance(y, int) and isinstance(z, int) and x > 0 and y > 0 and z > 0 and x < 8 and y < 8 and z < 8):
            return False
        if(self.x == x and self.y == y and self.z != z):
            return True
        if(self.z == z and self.y == y and self.x != x):
            return True
        if(self.z == z and self.x == x and self.y != y):
            return True

        return False





