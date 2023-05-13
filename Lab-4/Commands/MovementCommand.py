from Commands.Command import Command
from windowState import WindowState
import glfw

class MovementCommand(Command):
    def __init__(self, state: WindowState, key: int):
      super().__init__(state)
      self.key = key
   
    def execute(self):
      if self.key == glfw.KEY_A:
         self._state.currentPosition = [self._state.currentPosition[0] - 0.1, self._state.currentPosition[1], self._state.currentPosition[2]]
      elif self.key == glfw.KEY_D:
         self._state.currentPosition = [self._state.currentPosition[0] + 0.1, self._state.currentPosition[1], self._state.currentPosition[2]]
      elif self.key == glfw.KEY_S:
         self._state.currentPosition = [self._state.currentPosition[0], self._state.currentPosition[1] - 0.1, self._state.currentPosition[2]]
      elif self.key == glfw.KEY_W:
         self._state.currentPosition = [self._state.currentPosition[0], self._state.currentPosition[1] + 0.1, self._state.currentPosition[2]]
      elif self.key == glfw.KEY_Q:
         self._state.currentPosition = [self._state.currentPosition[0], self._state.currentPosition[1], self._state.currentPosition[2] - 0.1]
      elif self.key == glfw.KEY_E:
         self._state.currentPosition = [self._state.currentPosition[0], self._state.currentPosition[1], self._state.currentPosition[2] + 0.1]