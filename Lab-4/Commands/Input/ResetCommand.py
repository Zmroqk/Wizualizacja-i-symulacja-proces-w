from windowState import WindowState
from Commands.Command import Command
import Figures

class ResetCommand(Command):
   def __init__(self, state: WindowState):
      super().__init__(state)

   def execute(self):
      self._state.currentFigure = None
      self._state.currentPosition = [0, 0, 0]
      self._state.currentRotation = [0, 0, 0]