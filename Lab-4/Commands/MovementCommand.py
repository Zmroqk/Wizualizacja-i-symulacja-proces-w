from Commands.Command import Command
from windowState import WindowState
import glfw

class MovementCommand(Command):
   def __init__(self, state: WindowState, key: int):
      super().__init__(state)
      self.key = key

   def execute(self):
      if self._state.currentFigure is None:
         if self.key == glfw.KEY_Q:
            self._state.cameraDistance = self._state.cameraDistance + 0.1
         elif self.key == glfw.KEY_E:
            self._state.cameraDistance = self._state.cameraDistance - 0.1
      if self._state.currentFigure is not None:
         if self.key == glfw.KEY_A:
            self._state.currentFigure.globalPosition = [
               self._state.currentFigure.globalPosition[0] - 0.1
               , self._state.currentFigure.globalPosition[1]
               , self._state.currentFigure.globalPosition[2]
            ]
         elif self.key == glfw.KEY_D:
            self._state.currentFigure.globalPosition = [
               self._state.currentFigure.globalPosition[0] + 0.1
               , self._state.currentFigure.globalPosition[1]
               , self._state.currentFigure.globalPosition[2]
            ]
         elif self.key == glfw.KEY_S:
            self._state.currentFigure.globalPosition = [
               self._state.currentFigure.globalPosition[0]
               , self._state.currentFigure.globalPosition[1] - 0.1
               , self._state.currentFigure.globalPosition[2]
            ]
         elif self.key == glfw.KEY_W:
            self._state.currentFigure.globalPosition = [
               self._state.currentFigure.globalPosition[0]
               , self._state.currentFigure.globalPosition[1] + 0.1
               , self._state.currentFigure.globalPosition[2]
            ]
         elif self.key == glfw.KEY_Q:
            self._state.currentFigure.globalPosition = [
               self._state.currentFigure.globalPosition[0]
               , self._state.currentFigure.globalPosition[1]
               , self._state.currentFigure.globalPosition[2] - 0.1
            ]
         elif self.key == glfw.KEY_E:
            self._state.currentFigure.globalPosition = [
               self._state.currentFigure.globalPosition[0]
               , self._state.currentFigure.globalPosition[1]
               , self._state.currentFigure.globalPosition[2] + 0.1
            ]
      