from Figures.Figure import Figure
from windowState import WindowState
import numpy as np
import vectorOperations as vo

class Pyramid(Figure):
   def __init__(self, state: WindowState, d: float, h: float):
      super(Pyramid, self).__init__(state)
      self.d = d
      self.h = h
    
   def draw(self):
      v = self.createVertices()
      v = vo.applyRotation(v, self._state.currentRotation, self._state.currentRotationType)

      self._restoreColor()
      self._startDrawingTriangles()
      self._drawTriangle(v[0], v[1], v[2]) # DOWN
      self._drawTriangle(v[0], v[1], v[3]) # SIDE
      self._drawTriangle(v[1], v[2], v[3]) # SIDE
      self._drawTriangle(v[0], v[2], v[3]) # SIDE
      self._endDrawingBlock()

      self._setColor(0, 0, 0)
      self._startDrawingLines()
      self._drawLine(v[0], v[1])
      self._drawLine(v[1], v[2])
      self._drawLine(v[0], v[2])
      self._drawLine(v[1], v[3])
      self._drawLine(v[2], v[3])
      self._drawLine(v[0], v[3])
      self._endDrawingBlock()
      self._restoreColor()

   def createVertices(self):
      return [
         [-self.d/2, 0, 0], [self.d/2, 0, 0], [0, 0, (np.sqrt(3) * self.d)/2],
         [0, self.h, (np.sqrt(3) * self.d)/4]
      ]