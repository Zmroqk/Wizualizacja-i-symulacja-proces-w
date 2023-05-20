from windowState import WindowState
from Commands.Command import Command

class CameraFarCommand(Command):
   def __init__(self, state: WindowState, *params):
      super().__init__(state)
      self.far = float(params[0])

   def execute(self):
      self._state.cameraFar = self.far