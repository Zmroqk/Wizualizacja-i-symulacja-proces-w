from Commands.Command import Command
from windowState import WindowState
import glfw
import numpy as np

class RotationCommand(Command):
    def __init__(self, state: WindowState, key: int):
      super().__init__(state)
      self.key = key
   
    def execute(self):
      if self.key == glfw.KEY_K:
         self._state.currentRotation = [self._state.currentRotation[0] - np.pi/self._state.rotationQuality, self._state.currentRotation[1], self._state.currentRotation[2]]
      elif self.key == glfw.KEY_I:
         self._state.currentRotation = [self._state.currentRotation[0] + np.pi/self._state.rotationQuality, self._state.currentRotation[1], self._state.currentRotation[2]]
      elif self.key == glfw.KEY_L:
         self._state.currentRotation = [self._state.currentRotation[0], self._state.currentRotation[1] - np.pi/self._state.rotationQuality, self._state.currentRotation[2]]
      elif self.key == glfw.KEY_J:
         self._state.currentRotation = [self._state.currentRotation[0], self._state.currentRotation[1] + np.pi/self._state.rotationQuality, self._state.currentRotation[2]]
      elif self.key == glfw.KEY_U:
         self._state.currentRotation = [self._state.currentRotation[0], self._state.currentRotation[1], self._state.currentRotation[2] - np.pi/self._state.rotationQuality]
      elif self.key == glfw.KEY_O:
         self._state.currentRotation = [self._state.currentRotation[0], self._state.currentRotation[1], self._state.currentRotation[2] + np.pi/self._state.rotationQuality]