from windowState import WindowState
from Commands.Command import Command
import Figures

class SphereCommand(Command):
   def __init__(self, state: WindowState, *params):
      super().__init__(state)
      self.r = float(params[0])
      self.rings = int(params[1])

   def execute(self):
      sphere = Figures.Sphere(self._state, self.r, self.rings)
      self._state.figures[sphere.id] = sphere
      sphere.setup()