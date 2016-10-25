# The gravitational cursor
class Cursor:

    mass_start = 0
    mass_boost = 50000

    rad = 0    # radius of cursor
    mass = 0   # weight of cursor

    # on instantiation
    def __init__(self, rad, mass):
        self.mass_start = mass
        self.rad = rad
        self.mass = mass
