from Commands.Command import Command
from windowState import WindowState
import glfw
import numpy as np

class RotationCommand(Command):
    def __init__(self, state: WindowState, key: int):
      super().__init__(state)
      self.key = key
   
    def execute(self):
      if self._state.currentFigure is None:
         if self.key == glfw.KEY_J:
            self._state.cameraXRotation = self._state.cameraXRotation + np.pi/self._state.rotationQuality
         elif self.key == glfw.KEY_L:
            self._state.cameraXRotation = self._state.cameraXRotation - np.pi/self._state.rotationQuality
         elif self.key == glfw.KEY_I:
            self._state.cameraZRotation = self._state.cameraZRotation + np.pi/self._state.rotationQuality
         elif self.key == glfw.KEY_K:
            self._state.cameraZRotation = self._state.cameraZRotation - np.pi/self._state.rotationQuality
      if self._state.currentFigure is not None:
         if self.key == glfw.KEY_K:
            self._state.currentFigure.rotation = [
               self._state.currentFigure.rotation[0] - np.pi/self._state.rotationQuality
               , self._state.currentFigure.rotation[1]
               , self._state.currentFigure.rotation[2]
            ]
         elif self.key == glfw.KEY_I:
            self._state.currentFigure.rotation = [
               self._state.currentFigure.rotation[0] + np.pi/self._state.rotationQuality
               , self._state.currentFigure.rotation[1]
               , self._state.currentFigure.rotation[2]
            ]
         elif self.key == glfw.KEY_L:
            self._state.currentFigure.rotation = [
               self._state.currentFigure.rotation[0]
               , self._state.currentFigure.rotation[1] - np.pi/self._state.rotationQuality
               , self._state.currentFigure.rotation[2]
            ]
         elif self.key == glfw.KEY_J:
            self._state.currentFigure.rotation = [
               self._state.currentFigure.rotation[0]
               , self._state.currentFigure.rotation[1] + np.pi/self._state.rotationQuality
               , self._state.currentFigure.rotation[2]
            ]
         elif self.key == glfw.KEY_U:
            self._state.currentFigure.rotation = [
               self._state.currentFigure.rotation[0]
               , self._state.currentFigure.rotation[1]
               , self._state.currentFigure.rotation[2] - np.pi/self._state.rotationQuality
            ]
         elif self.key == glfw.KEY_O:
            self._state.currentFigure.rotation = [
               self._state.currentFigure.rotation[0]
               , self._state.currentFigure.rotation[1]
               , self._state.currentFigure.rotation[2] + np.pi/self._state.rotationQuality
            ]