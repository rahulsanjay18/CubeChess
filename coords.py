class Coordinates:

    def __init__(self, c=None, x=None, y=None, z=None) -> None:
        self.x = c[0]
        self.y = c[1]
        self.z = c[2]

        if not c and (x and y and z):
            self.x = x
            self.y = y
            self.z = z

    
    def __eq__(self, __o: object) -> bool:
        return (self.x == __o.x) and (self.y == __o.y) and (self.z == __o.z)