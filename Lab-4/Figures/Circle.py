from OpenGL.GL import *
from Figures.Figure import Figure
from windowState import WindowState
import numpy as np
import vectorOperations as vo

class Circle(Figure):
   def __init__(self, state: WindowState, radius: float = None, polygonSideLength: float = None, is2d = True, x = 0., y = 0.):
      super().__init__(state)
      if polygonSideLength is not None:
         self.radius = polygonSideLength/(2 * np.sin(180./self._state.circleQuality))
      else:
         self.radius = radius
      self.is2d = is2d
      self.x = x
      self.y = y
   
   def createVertices(self):
      angleIncrement = 360. / self._state.circleQuality
      angleIncrement *= np.pi / 180

      angle = 0.
      
      # r = side_length / (2 * np.sin(side_length / 2))

      v = []
      for _ in range(self._state.circleQuality):
         if self.is2d is True:
            vTemp = [self.radius * np.cos(angle) + self.x, np.sin(angle) + self.y, 0.]
            v.append(vTemp)
         else:
            vTemp = [self.radius * np.cos(angle) + self.x, self.y, np.sin(angle)]
            v.append(vTemp)
         angle += angleIncrement
      return v
   
   def draw(self):
      angleIncrement = 360. / self._state.circleQuality
      angleIncrement *= np.pi / 180
      angle = 0.
      
      # r = side_length / (2 * np.sin(side_length / 2))
      
      v = vo.applyRotationAll(self.createVertices(), self._state.currentRotation)
      v = vo.applyPosition(v, *self._state.currentPosition)

      self._restoreColor()
      glBegin(GL_TRIANGLE_FAN)
      for vTemp in v:
         glVertex3f(*vTemp)
         angle += angleIncrement
      glEnd()

      self._setColor(0, 0, 0)
      self._startDrawingLines()
      for i in range(len(v) - 1):
         self._drawLine(v[i], v[i+1])
      self._drawLine(v[0], v[-1])
      self._endDrawingBlock()
      self._restoreColor()