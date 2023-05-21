from windowState import WindowState
from Commands.Command import Command
import Figures

class CylinderCommand(Command):
   def __init__(self, state: WindowState, *params):
      super().__init__(state)
      self.r = float(params[0])
      self.h = float(params[1])

   def execute(self):
      cylinder = Figures.Cylinder(self._state, self.r, self.h)
      self._state.figures[cylinder.id] = cylinder
      cylinder.setup()