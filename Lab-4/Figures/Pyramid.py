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
      v = vo.applyRotationAll(self.createVertices(), self._state.currentRotation)
      v = vo.applyPosition(v, *self._state.currentPosition)

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
      self._bindColorData(self.vertex_color_id, np.array(self._state.currentColor, dtype=np.float32), self.size)

      self.lineSize = self._bindVertexData(self.line_buffer_id, np.array(vLinesOut, dtype=np.float32))
      self._bindColorData(self.line_color_id, np.array(self._state.currentLineColor, dtype=np.float32), self.size)  

   def draw(self):
      self._drawTriangle()
      self._drawLines()

   def createVertices(self):
      return [
         [-self.d/2, 0, 0], [self.d/2, 0, 0], [0, 0, (np.sqrt(3) * self.d)/2],
         [0, self.h, (np.sqrt(3) * self.d)/4]
      ]