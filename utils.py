def check_if_valid_move(piece, x, y, z):
    return isinstance(x, int) and isinstance(y, int) and isinstance(z,
                int) and 8 > x >= 0 and 8 > y >= 0 and 8 > z >= 0)
