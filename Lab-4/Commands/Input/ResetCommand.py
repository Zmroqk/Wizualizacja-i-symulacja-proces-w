from windowState import WindowState
from Commands.Command import Command
import Figures

class ResetCommand(Command):
   def __init__(self, state: WindowState):
      super().__init__(state)

   def execute(self):
      if self._state.currentFigure is not None:
         self._state.currentFigure.globalPosition = [0, 0, 0]
         self._state.currentFigure.rotation = [0, 0, 0]