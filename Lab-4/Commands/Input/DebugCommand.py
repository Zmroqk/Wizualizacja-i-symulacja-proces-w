from windowState import WindowState
from Commands.Command import Command
import Figures

class DebugCommand(Command):
   def __init__(self, state: WindowState):
      super().__init__(state)

   def execute(self):
      self._state.debug = not self._state.debug