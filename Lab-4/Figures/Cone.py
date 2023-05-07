from Figures.Figure import Figure
from Figures.Circle import Circle
from windowState import WindowState
import numpy as np
import vectorOperations as vo

class Cone(Figure):
   def __init__(self, state: WindowState, radius: float, height: float):
      super().__init__(state)
      self.radius = radius
      self.height = height

   def draw(self):
      circle = Circle(self._state, self.radius, is2d=False)
      v = circle.createVertices()
      circle.draw()
      vTop = [0., self.height, 0.]
      vTop = vo.applyRotationSingle(vTop, self._state.currentRotation, self._state.currentRotationType)

      self._restoreColor()
      self._startDrawingTriangles()
      for i in range(len(v) - 1):
         self._drawTriangle(v[i], v[i + 1], vTop)
      self._drawTriangle(v[0], v[-1], vTop)
      self._endDrawingBlock()

      self._setColor(0, 0, 0)
      self._startDrawingLines()
      for i in range(len(v)):
         self._drawLine(v[i], vTop)
      self._endDrawingBlock()
      self._restoreColor()
   
   def createVertices(self):
      circle = Circle(self._state, self.radius, is2d=False)
      return (circle.createVertices(), [0., self.height, 0.])