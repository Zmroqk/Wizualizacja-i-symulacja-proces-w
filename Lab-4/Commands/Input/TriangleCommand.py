from windowState import WindowState
from Commands.Command import Command
import Figures

class TriangleCommand(Command):
   def __init__(self, state: WindowState):
      super().__init__(state)

   def execute(self):
      triangle = Figures.Triangle(self._state)
      self._state.figures[triangle.id] = triangle
      triangle.setup()