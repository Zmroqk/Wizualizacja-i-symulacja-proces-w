from Figures.Figure import Figure
from vectorOperations import *
from typing import List
from windowState import WindowState

class Cuboid(Figure):
   def __init__(self, state: WindowState, a: float, b: float, c: float):
      super(Cuboid, self).__init__(state)
      self.a = a
      self.b = b
      self.c = c

   def draw(self):
      v = applyRotation(self.createVertices(), self._state.currentRotation, self._state.currentRotationType)

      self._setColor(*self._state.currentColor)
      self._startDrawingTriangles()
      self._drawTriangle(v[0], v[1], v[2]) #DOWN
      self._drawTriangle(v[0], v[2], v[3]) #DOWN
      self._drawTriangle(v[4], v[5], v[6]) #UP
      self._drawTriangle(v[4], v[6], v[7]) #UP
      self._drawTriangle(v[0], v[1], v[5]) #SIDE
      self._drawTriangle(v[0], v[5], v[4]) #SIDE
      self._drawTriangle(v[1], v[2], v[6]) #SIDE 2
      self._drawTriangle(v[1], v[6], v[5]) #SIDE 2
      self._drawTriangle(v[2], v[3], v[7]) #SIDE 3
      self._drawTriangle(v[2], v[7], v[6]) #SIDE 3
      self._drawTriangle(v[0], v[3], v[7]) #SIDE 4
      self._drawTriangle(v[0], v[7], v[4]) #SIDE 4
      self._endDrawingBlock()

      self._setColor(0, 0, 0)
      self._startDrawingLines()
      self._drawLine(v[0], v[1])
      self._drawLine(v[0], v[3])
      self._drawLine(v[0], v[4])
      self._drawLine(v[2], v[1])
      self._drawLine(v[2], v[3])
      self._drawLine(v[2], v[6])
      self._drawLine(v[5], v[1])
      self._drawLine(v[5], v[4])
      self._drawLine(v[5], v[6])
      self._drawLine(v[7], v[3])
      self._drawLine(v[7], v[4])
      self._drawLine(v[7], v[6])
      self._endDrawingBlock()

      self._restoreColor()
      
   def createVertices(self):
      return [
         [-self.a/2, -self.b/2, -self.c/2], [self.a/2, -self.b/2, -self.c/2], [self.a/2, -self.b/2, self.c/2], [-self.a/2, -self.b/2, self.c/2],
         [-self.a/2, self.b/2, -self.c/2], [self.a/2, self.b/2, -self.c/2], [self.a/2, self.b/2, self.c/2], [-self.a/2, self.b/2, self.c/2],
      ]