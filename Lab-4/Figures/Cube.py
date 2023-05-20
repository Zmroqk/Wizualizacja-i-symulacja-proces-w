from Figures.Cuboid import Cuboid
from windowState import WindowState

class Cube(Cuboid):
    def __init__(self, state: WindowState, a: float):
        super(Cube, self).__init__(state, a, a, a)
        self.type = 'Cube'