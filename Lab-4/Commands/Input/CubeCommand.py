from windowState import WindowState
from Commands.Command import Command
import Figures

class CubeCommand(Command):
   def __init__(self, state: WindowState, *params):
      super().__init__(state)
      self.a = float(params[0])

   def execute(self):
      cube = Figures.Cube(self._state, self.a)
      self._state.figures[cube.id] = cube
      print(cube.id, self._state.figures)
      cube.setup()