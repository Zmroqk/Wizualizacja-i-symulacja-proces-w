from IO.FigureFileSchema import FigureFileSchema
from OpenGL.GL import *
from Figures.Figure import Figure
from windowState import WindowState
import numpy as np
import vectorOperations as vo

class Circle(Figure):
   def __init__(self, state: WindowState, radius: float = None, polygonSideLength: float = None, is2d = True, x = 0., y = 0.):
      super().__init__(state)
      self.polygonSideLength = None
      if radius is not None:
         self.radius = radius

      if polygonSideLength is not None:
         self.radius = polygonSideLength/(2 * np.sin(180./self._state.circleQuality))

      self.is2d = is2d
      self.x = x
      self.y = y
   
   def setup(self):
      v = self.createVertices()
      
      self.size = self._bindVertexData(self.vertex_buffer_id, np.array(v, dtype=np.float32))
      self._bindColorData(self.vertex_color_id, np.array(self.figureColor, dtype=np.float32), self.size)
   
   def createVertices(self):
      if(self.polygonSideLength is not None):
         return self.createVertices()
      else:
         return self.createVerticesRadius(self.radius)

   def creationVerticesSide(self):
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

   def createVerticesRadius(self, radius):
      # Calculate the number of points to generate
      num_points = self._state.circleQuality

      v = []

      # Generate points
      for i in range(num_points):
         # Calculate angle in radians
         theta = 2 * np.pi * i / num_points

         # Calculate x and y coordinates
         x = radius * np.cos(theta)
         y = radius * np.sin(theta)

         if self.is2d is True:
            v.append([x + self.x, y + self.y, 0])
         else:
            v.append([x + self.x, self.y, y])

      return v
   
   def draw(self):
      self._drawTriangleFans()

   def export(self) -> FigureFileSchema:
      return {}