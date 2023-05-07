from Figures.Figure import Figure
from Figures.Circle import Circle
from windowState import WindowState
import numpy as np
import vectorOperations as vo

class Cylinder(Figure):
   def __init__(self, state: WindowState, radius: float, h: float):
      super().__init__(state)
      self.radius = radius
      self.h = h

   def draw(self):
      circleLow = Circle(self._state, self.radius, is2d=False)
      circleHigh = Circle(self._state, self.radius, is2d=False, x = 0, y = self.h)
      vLow = circleLow.createVertices()
      vHigh = circleHigh.createVertices()
      circleLow.draw()
      circleHigh.draw()
      
      self._restoreColor()
      self._startDrawingTriangles()
      for i in range(len(vLow) - 1):
         self._drawTriangle(vLow[i], vLow[i + 1], vHigh[i])
         self._drawTriangle(vHigh[i], vHigh[i + 1], vLow[i + 1])
      self._drawTriangle(vLow[0], vLow[-1], vHigh[0])
      self._drawTriangle(vHigh[0], vHigh[-1], vLow[-1])
      self._endDrawingBlock()

      self._setColor(0, 0, 0)
      self._startDrawingLines()
      for i in range(len(vLow)):
         self._drawLine(vLow[i], vHigh[i])
      self._endDrawingBlock()

   def createVertices(self):
      circleLow = Circle(self._state, self.radius, is2d=False)
      circleHigh = Circle(self._state, self.radius, is2d=False, x = 0, y = self.h)
      vLow = circleLow.createVertices()
      vHigh = circleHigh.createVertices()
      return (vLow, vHigh)