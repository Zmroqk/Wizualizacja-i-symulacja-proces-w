from windowState import WindowState
from Commands.Command import Command
import Figures

class CircleCommand(Command):
   def __init__(self, state: WindowState, *params):
      super().__init__(state)
      self.psl = float(params[0])

   def execute(self):
      self._state.currentFigure = Figures.Circle(self._state, polygonSideLength=self.psl, is2d=True)
      self._state.currentFigure.setup()