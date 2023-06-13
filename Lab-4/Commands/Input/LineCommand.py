from windowState import WindowState
from windowState import WindowState
from Commands.Command import Command
import Figures

class LineCommand(Command):
   def __init__(self, state: WindowState):
      super().__init__(state)

   def execute(self):
      line = Figures.Line(self._state)
      self._state.figures[line.id] = line
      line.setup()