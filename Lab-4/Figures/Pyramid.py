from Figures.Figure import Figure
from windowState import WindowState
import numpy as np
import vectorOperations as vo

class Pyramid(Figure):
   def __init__(self, state: WindowState, d: float, h: float):
      super(Pyramid, self).__init__(state)
      self.d = d
      self.h = h
    

   def setup(self):
      v = self.createVertices()

      vOut = []
      vLinesOut = []

      # DOWN
      vOut.append(v[0])
      vOut.append(v[1])
      vOut.append(v[2])

      # SIDE
      vOut.append(v[0])
      vOut.append(v[1])
      vOut.append(v[3])


      # SIDE
      vOut.append(v[1])
      vOut.append(v[2])
      vOut.append(v[3])


       # SIDE
      vOut.append(v[0])
      vOut.append(v[2])
      vOut.append(v[3])


      vLinesOut.append(v[0])
      vLinesOut.append(v[1])

      vLinesOut.append(v[1])
      vLinesOut.append(v[2])

      vLinesOut.append(v[0])
      vLinesOut.append(v[2])

      vLinesOut.append(v[1])
      vLinesOut.append(v[3])

      vLinesOut.append(v[2])
      vLinesOut.append(v[3])

      vLinesOut.append(v[0])
      vLinesOut.append(v[3])

      self.size = self._bindVertexData(self.vertex_buffer_id, np.array(vOut, dtype=np.float32))
      self._bindColorData(self.vertex_color_id, np.array(self.figureColor, dtype=np.float32), self.size)

      self.lineSize = self._bindVertexData(self.line_buffer_id, np.array(vLinesOut, dtype=np.float32))
      self._bindColorData(self.line_color_id, np.array(self._state.currentLineColor, dtype=np.float32), self.size)  

   def draw(self):
      self._drawTriangle()
      self._drawLines()

   def export(self):
      v = self.createVertices()
      return {
         'Verticies': np.array([
            v[0], v[1], v[2],
            v[0], v[1], v[3],
            v[1], v[2], v[3],
            v[0], v[2], v[3]
         ], dtype=np.float32).tolist()
         , 'Indices': []
         , 'Colors': self._generateColorArray(self.figureColor, self.size).tolist()
         , 'LineVertices': np.array([
            v[0], v[1],
            v[1], v[2],
            v[0], v[2],
            v[1], v[3],
            v[2], v[3],
            v[0], v[3]
         ], dtype=np.float32).tolist()
         , 'LineColor': self._state.currentLineColor
      }

   def createVertices(self):
      return [
         [-self.d/2, 0, 0], [self.d/2, 0, 0], [0, 0, (np.sqrt(3) * self.d)/2],
         [0, self.h, (np.sqrt(3) * self.d)/4]
      ]