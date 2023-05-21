from IO.FigureFileSchema import FigureFileSchema
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
      self.circleLow = Circle(self._state, self.radius, is2d=False)
      self.circleHigh = Circle(self._state, self.radius, is2d=False, x = 0, y = self.h)

   def setup(self):  
      self.circleHigh.setup()
      self.circleLow.setup()
      vOut, vLinesOut = self._createVerticiesArray()

      self.size = self._bindVertexData(self.vertex_buffer_id, np.array(vOut, dtype=np.float32))
      self._bindColorData(self.vertex_color_id, np.array(self.figureColor, dtype=np.float32), self.size)

      self.lineSize = self._bindVertexData(self.line_buffer_id, np.array(vLinesOut, dtype=np.float32))
      self._bindColorData(self.line_color_id, np.array(self._state.currentLineColor, dtype=np.float32), self.size)      

   def _createVerticiesArray(self):
      vLow = self.circleLow.createVertices()
      vHigh = self.circleHigh.createVertices()
      vOut = []
      vLinesOut = []
      for i in range(len(vLow) - 1):
         vOut.append(vLow[i])
         vOut.append(vLow[i + 1])
         vOut.append(vHigh[i])

         vOut.append(vHigh[i])
         vOut.append(vHigh[i + 1])
         vOut.append(vLow[i + 1])
      vOut.append(vLow[0])
      vOut.append(vLow[-1])
      vOut.append(vHigh[0])
      vOut.append(vHigh[0])
      vOut.append(vHigh[-1])
      vOut.append(vLow[-1])

      for i in range(len(vLow)):
         vLinesOut.append(vLow[i])
         vLinesOut.append(vHigh[i])

      return vOut, vLinesOut

   def export(self) -> FigureFileSchema:
      vOut, vLinesOut = self._createVerticiesArray()
      return {
         'Vertices': np.array(vOut, dtype=np.float32).tolist()
         , 'Colors': self._generateColorArray(self.figureColor, self.size).tolist()
         , 'Indices': []
         , 'LineVertices': np.array(vLinesOut, dtype=np.float32).tolist()
         , 'LineColor': self._state.currentLineColor
      }

   def draw(self):
      self.circleLow.draw()
      self.circleHigh.draw()
      self._drawTriangle()
      self._drawLines()

   def createVertices(self):
      circleLow = Circle(self._state, self.radius, is2d=False)
      circleHigh = Circle(self._state, self.radius, is2d=False, x = 0, y = self.h)
      vLow = circleLow.createVertices()
      vHigh = circleHigh.createVertices()
      return (vLow, vHigh)