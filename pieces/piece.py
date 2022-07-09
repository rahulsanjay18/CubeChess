class Piece:

    def __init__(self):
        self.sym = ''

    def get_color(self):
        return self.sym.upper() == self.sym
    
    def is_valid_move(self, coords, new_coords):
        raise NotImplementedError

    def gen_path_step(self, coords, new_coords):
        raise NotImplementedError

    def is_valid_attack(self, coords, new_coords):
        return self.is_valid_move(self, coords, new_coords)
