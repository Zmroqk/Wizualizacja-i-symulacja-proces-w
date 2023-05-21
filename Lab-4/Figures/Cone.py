from IO.FigureFileSchema import FigureFileSchema
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
      self.circle = Circle(self._state, self.radius, is2d=False)

   def _createVerticiesArray(self):
      v, vTop = self.createVertices()
      vOut = []
      vLinesOut = []
      for i in range(len(v) - 1):
         vOut.append(v[i])
         vOut.append(v[i + 1])
         vOut.append(vTop)

      vOut.append(v[0])
      vOut.append(v[-1])
      vOut.append(vTop)

      for i in range(len(v)):
         vLinesOut.append(v[i])
         vLinesOut.append(vTop)

      return vOut, vLinesOut

   def setup(self):
      self.circle.setup()
      vOut, vLinesOut = self._createVerticiesArray()

      self.size = self._bindVertexData(self.vertex_buffer_id, np.array(vOut, dtype=np.float32))
      self._bindColorData(self.vertex_color_id, np.array(self.figureColor, dtype=np.float32), self.size)

      self.lineSize = self._bindVertexData(self.line_buffer_id, np.array(vLinesOut, dtype=np.float32))
      self._bindColorData(self.line_color_id, np.array(self._state.currentLineColor, dtype=np.float32), self.size)
   
   def export(self) -> FigureFileSchema:
      vOut, vLinesOut = self._createVerticiesArray()
      return {
         'Vertices': np.array(vOut, dtype=np.float32).tolist()
         , 'Indices': []
         , 'Colors': self._generateColorArray(self.figureColor, self.size)
         , 'LineVertices': np.array(vLinesOut, dtype=np.float32).tolist()
         , 'LineColor': self._state.currentLineColor
      }

   def draw(self):
      self.circle.draw()
      self._drawTriangle()
      self._drawLines()

   
   def createVertices(self):
      return (self.circle.createVertices(), [0., self.height, 0.])