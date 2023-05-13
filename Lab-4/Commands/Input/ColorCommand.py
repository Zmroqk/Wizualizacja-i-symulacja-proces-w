from windowState import WindowState
from Commands.Command import Command

class ColorCommand(Command):
   def __init__(self, state: WindowState, *params):
      super().__init__(state)
      self.r = float(params[0])
      self.g = float(params[1])
      self.b = float(params[2])

   def execute(self):
      self._state.currentColor = [self.r, self.g, self.b]
      if self._state.currentFigure is not None:
         self._state.currentFigure.setup()