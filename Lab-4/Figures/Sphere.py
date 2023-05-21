from IO.FigureFileSchema import FigureFileSchema
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

   def _createVerticiesArray(self):
      vOut = []
      vLinesOut = []
      rotationChange = np.pi/(self.rings)
      circles = self.createVertices()

      for circle in circles:
         for j in range(len(circle) - 1):
            vOut.append(circle[j])
            vOut.append(circle[j + 1])
            vOut.append(vo.applyRotationSingle(circle[j], rotationChange, vo.Rotation.OZ))

            vOut.append(vo.applyRotationSingle(circle[j], rotationChange, vo.Rotation.OZ))
            vOut.append(vo.applyRotationSingle(circle[j+1], rotationChange, vo.Rotation.OZ))
            vOut.append(circle[j + 1])

         vOut.append(circle[-1])
         vOut.append(circle[0])
         vOut.append(vo.applyRotationSingle(circle[-1], rotationChange, vo.Rotation.OZ))
         vOut.append(vo.applyRotationSingle(circle[-1], rotationChange, vo.Rotation.OZ))
         vOut.append(vo.applyRotationSingle(circle[0], rotationChange, vo.Rotation.OZ))
         vOut.append(circle[0])


         for circle in circles:
            for j in range(len(circle) - 1):
               vLinesOut.append(circle[j])
               vLinesOut.append(circle[j + 1])

               vLinesOut.append(circle[j])
               vLinesOut.append(vo.applyRotationSingle(circle[j], rotationChange, vo.Rotation.OZ))

               vLinesOut.append(circle[j + 1])
               vLinesOut.append(vo.applyRotationSingle(circle[j + 1], rotationChange, vo.Rotation.OZ))

               vLinesOut.append(circle[j + 1])
               vLinesOut.append(vo.applyRotationSingle(circle[j], rotationChange, vo.Rotation.OZ))

            vLinesOut.append(circle[-1])
            vLinesOut.append(circle[0])
            vLinesOut.append(circle[0])
            vLinesOut.append(vo.applyRotationSingle(circle[-1], rotationChange, vo.Rotation.OZ))
      return vOut, vLinesOut

   def setup(self):
      vOut, vLinesOut = self._createVerticiesArray()
      self.size = self._bindVertexData(self.vertex_buffer_id, np.array(vOut, dtype=np.float32))
      self._bindColorData(self.vertex_color_id, np.array(self.figureColor, dtype=np.float32), self.size)

      self.lineSize = self._bindVertexData(self.line_buffer_id, np.array(vLinesOut, dtype=np.float32))
      self._bindColorData(self.line_color_id, np.array(self._state.currentLineColor, dtype=np.float32), self.size)

   def export(self) -> FigureFileSchema:
      vOut, vLinesOut = self._createVerticiesArray()
      return {
         'Indices': []
         , 'Vertices': np.array(vOut, dtype=np.float32).tolist()
         , 'Colors': self._generateColorArray(self.figureColor, self.size).tolist()
         , 'LineColor': self._state.currentLineColor
         , 'LineVertices': np.array(vLinesOut, dtype=np.float32).tolist()
      }

   def draw(self):
      self._drawTriangle()
      self._drawLines()
   
   def createVertices(self):
      circle = Circle(self._state, self.radius, is2d=False)
      v = circle.createVertices()
      rotationChange = np.pi/(self.rings)
      circles = []
      for i in range(self.rings):
         circles.append(vo.applyRotation(v, rotationChange * i, vo.Rotation.OZ))
      return circles