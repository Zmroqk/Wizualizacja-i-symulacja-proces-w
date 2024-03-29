from windowState import WindowState
from Commands.Command import Command
import Figures

class PyramidCommand(Command):
   def __init__(self, state: WindowState, *params):
      super().__init__(state)
      self.d = float(params[0])
      self.h = float(params[1])

   def execute(self):
      pyramid = Figures.Pyramid(self._state, self.d, self.h)
      self._state.figures[pyramid.id] = pyramid
      pyramid.setup()