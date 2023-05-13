from windowState import WindowState
from Commands.Command import Command

class CircleQualityCommand(Command):
   def __init__(self, state: WindowState, *params):
      super().__init__(state)
      self.quality = int(params[0])

   def execute(self):
      self._state.circleQuality = self.quality
      if self._state.currentFigure is not None:
         self._state.currentFigure.setup()