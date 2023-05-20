from windowState import WindowState
from Commands.Command import Command

class ContextCommand(Command):
   def __init__(self, state: WindowState, *params):
      super().__init__(state)
      if len(params) == 1:
         self.figureId = int(params[0])
      else:
         self.figureId = None

   def execute(self):
      if self.figureId is None:
         self._state.currentFigure = None
      else:
         self._state.currentFigure = self._state.figures[self.figureId]