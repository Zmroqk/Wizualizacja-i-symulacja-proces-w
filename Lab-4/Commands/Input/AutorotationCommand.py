from windowState import WindowState
from Commands.CommandWithTimer import CommandWithTimmer
import numpy as np

class AutorotationCommand(CommandWithTimmer):
   def __init__(self, state: WindowState, *params):
      super().__init__(state)
      self.axis = params[0]

   def execute(self):
      if self.axis == 'X':
         self._createTimer(self._rotateX)
      elif self.axis == 'Y':
         self._createTimer(self._rotateY)
      elif self.axis == 'Z':
         self._createTimer(self._rotateZ)
   
   def _rotateX(self):
      self._state.currentRotation = [self._state.currentRotation[0] + np.pi/self._state.rotationQuality, *self._state.currentRotation[1:]]
      self.execute()

   def _rotateZ(self):
      self._state.currentRotation = [*self._state.currentRotation[:-1], self._state.currentRotation[2] + np.pi/self._state.rotationQuality]
      self.execute()

   def _rotateY(self):
      self._state.currentRotation = [self._state.currentRotation[0], self._state.currentRotation[1] + np.pi/self._state.rotationQuality, self._state.currentRotation[2]]
      self.execute()