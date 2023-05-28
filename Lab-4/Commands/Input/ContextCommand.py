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
      if self._state.currentFigure is not None:
         self._state.currentFigure.figureColor = list(map(lambda x: x + 0.2, self._state.currentFigure.figureColor))
         self._state.currentFigure.setup()
      if self.figureId is None:
         self._state.currentFigure = None
      else:
         self._state.currentFigure = self._state.figures[self.figureId]
         self._state.currentFigure.figureColor = list(map(lambda x: x - 0.2, self._state.currentFigure.figureColor))
         self._state.currentFigure.setup()