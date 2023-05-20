from windowState import WindowState
from Commands.Command import Command
import Figures

class CuboidCommand(Command):
   def __init__(self, state: WindowState, *params):
      super().__init__(state)
      self.a = float(params[0])
      self.b = float(params[1])
      self.c = float(params[2])

   def execute(self):
      cuboid = Figures.Cuboid(self._state, self.a, self.b, self.c)
      self._state.figures[cuboid.id] = cuboid
      cuboid.setup()