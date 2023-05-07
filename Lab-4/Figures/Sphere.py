from Figures.Figure import Figure
from Figures.Circle import Circle
from windowState import WindowState
import numpy as np
import vectorOperations as vo

class Sphere(Figure):
   def __init__(self, state: WindowState, radius, rings):
      super().__init__(state)
      self.radius = radius
      self.rings = rings

   def draw(self):
      rotationChange = np.pi/(self.rings)
      circles = self.createVertices()

      self._restoreColor()
      self._startDrawingTriangles()
      for circle in circles:
         for j in range(len(circle) - 1):
            self._drawTriangle(circle[j], circle[j+1], vo.applyRotationSingle(circle[j], rotationChange, vo.Rotation.OZ))
            self._drawTriangle(vo.applyRotationSingle(circle[j], rotationChange, vo.Rotation.OZ), vo.applyRotationSingle(circle[j+1], rotationChange, vo.Rotation.OZ), circle[j + 1])
         self._drawTriangle(circle[-1], circle[0], vo.applyRotationSingle(circle[-1], rotationChange, vo.Rotation.OZ))
         self._drawTriangle(vo.applyRotationSingle(circle[-1], rotationChange, vo.Rotation.OZ), vo.applyRotationSingle(circle[0], rotationChange, vo.Rotation.OZ), circle[0])
      self._endDrawingBlock()

      self._setColor(0, 0, 0)
      self._startDrawingLines()
      for circle in circles:
         for j in range(len(circle) - 1):
            self._drawLine(circle[j], circle[j + 1])
            self._drawLine(circle[j], vo.applyRotationSingle(circle[j], rotationChange, vo.Rotation.OZ))
            self._drawLine(circle[j + 1], vo.applyRotationSingle(circle[j + 1], rotationChange, vo.Rotation.OZ))
            self._drawLine(circle[j + 1], vo.applyRotationSingle(circle[j], rotationChange, vo.Rotation.OZ))
         self._drawLine(circle[-1], circle[0])
         self._drawLine(circle[0], vo.applyRotationSingle(circle[-1], rotationChange, vo.Rotation.OZ))
      self._endDrawingBlock()
      self._restoreColor()
   
   def createVertices(self):
      circle = Circle(self._state, self.radius, is2d=False)
      v = circle.createVertices()
      rotationChange = np.pi/(self.rings)
      circles = []
      for i in range(self.rings):
         circles.append(vo.applyRotation(v, rotationChange * i, vo.Rotation.OZ))
      return circles