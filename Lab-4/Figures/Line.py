from Figures.Figure import Figure
from vectorOperations import *
from typing import List
from windowState import WindowState

class Line(Figure):
   def __init__(self, state: WindowState):
      super().__init__(state)
      self.type = 'Line'

   def draw(self):
      self._drawTriangle()
      self._drawLines()

   def export(self):
      v = self.createVertices()

      return {
         'Vertices': []
         , 'Colors': self._generateColorArray(self.figureColor, self.size).tolist()
         , 'LineVertices': []
         , 'LineColor': self._state.currentLineColor
         , 'Indices': []
      }

   def setup(self):
      position = self._state.cameraTarget + self.globalPosition
      v = np.array(applyPosition(applyRotationAll(self.createVertices(), self.rotation), *position))

      self.verticies = np.array([
         v[0], v[1]
      ], dtype=np.float32)

      self.size = self._bindVertexData(self.vertex_buffer_id, self.verticies)

      if self.isColliding:
         self._bindColorData(self.vertex_color_id, np.array([1, 0, 0], dtype=np.float32), self.size)
      else:
         self._bindColorData(self.vertex_color_id, np.array(self.figureColor, dtype=np.float32), self.size)

   def createVertices(self):
      return [[-0.5, 0, 0], [0.5, 0, 0]]