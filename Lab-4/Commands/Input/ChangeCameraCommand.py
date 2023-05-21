from windowState import WindowState
from Commands.Command import Command
import camera

class ChangeCameraCommand(Command):
   def __init__(self, state: WindowState):
      super().__init__(state)

   def execute(self):
      if self._state.currentCamera == camera.CameraType.Ortographic:
         self._state.currentCamera = camera.CameraType.Perspective
      else:
         self._state.currentCamera = camera.CameraType.Ortographic