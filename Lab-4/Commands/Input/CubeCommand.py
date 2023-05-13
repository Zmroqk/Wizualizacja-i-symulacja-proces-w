from windowState import WindowState
from Commands.Command import Command
import Figures

class CubeCommand(Command):
   def __init__(self, state: WindowState, *params):
      super().__init__(state)
      self.a = float(params[0])

   def execute(self):
      self._state.currentFigure = Figures.Cube(self._state, self.a)
      self._state.currentFigure.setup()