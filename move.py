
from pieces import piece


class Move:
    
    def __init__(self, piece, start, end, is_capture) -> None:
        self.piece = piece
        self.start = start
        self.end = end
        self.is_capture = is_capture

    def __str__(self) -> str:
        start_str = str(self.start[0]) + str(self.start[1]) + str(self.start[2])
        end_str = str(self.end[0]) + str(self.end[1]) + str(self.end[2])
        return self.piece + start_str + ('x' if self.is_capture else ',') + end_str
