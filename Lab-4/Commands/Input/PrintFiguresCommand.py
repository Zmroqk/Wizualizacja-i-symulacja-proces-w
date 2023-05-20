from windowState import WindowState
from Commands.Command import Command
import Figures

class PrintFiguresCommand(Command):
   def __init__(self, state: WindowState):
      super().__init__(state)
   def execute(self):
      for figure in self._state.figures.values():
         print(figure.toString())