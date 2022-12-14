from curses.ascii import islower
import yaml
from pieces import piece_factory
from board import Board
import pieces.piece as p
from pieces.utils import check_if_valid_pos
from pieces.piece_factory import PieceFactory
from move import Move

class Game:
    
    is_white_turn = True

    def __init__(self, config='default.yaml'):
        with open(config, "r") as stream:
            try:
                yaml_file = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        self.board = Board(yaml_file['board_str'])
        self.moves = []
        self.factory = PieceFactory()
        self.path_pieces = ['r', 'b', 't', 'q']


    def is_path_empty(self, path_pos):
        for pos in path_pos:
            if self.board.get(pos) != '0':
                return False
        
        return True

    def convert_coords_to_move(self, piece_char, start, end, is_capture):
        return Move(piece_char, start, end, is_capture)

    '''
    This is done in a few steps:
    
    1. Find the piece on the board
    2. Take that piece object and find if its a legal move
    3. If legal, move the piece, if not return False
    4. Find that piece's range of movement
    5. If Rook, Bishop, Priest, Pawn or Queen, we need to remove invalid moves
    6. Remove moves by just iterating, assign the leftover moves to the piece
    7. Log move
    7. Return True

    '''
    def make_move(self, x:int, y:int, z:int, x_p:int, y_p:int, z_p:int) -> bool:
        # check if coordinates are in bounds
        start = [x, y, z]
        end = [x_p, y_p, z_p]
        if not check_if_valid_pos(start) or not check_if_valid_pos(end):
            # invalid position, move cannot be made
            return False
        
        piece_char = self.board.get(start)
        piece_end = self.board.get(end)
        piece_char_l = piece_char.lower()

        if piece_char == 0:
            # the start position is blank, move cannot be made
            return False

        if piece_end.islower() == piece_char.islower():
            # start and end piece are the same color, so the move cannot be hit
            return False
        
        piece = self.factory.create_piece(piece_char, is_white=piece_char.islower())

        if not piece.is_valid_move(start, end):
            return False
        
        # The shape of the movement is valid, now we need to check if there is a path from one to the other
        if piece_char_l in self.path_pieces:
            path_pos = piece.gen_path_step(start, end)
            if self.is_path_empty(path_pos):
                return False
        
        is_capture = piece_end.islower() != piece_char.islower()

        move = self.convert_coords_to_move(piece_char, start, end, is_capture)

        self.moves.append(move)

        return True
