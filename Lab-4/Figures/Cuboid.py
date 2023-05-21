from Figures.Figure import Figure
from vectorOperations import *
from typing import List
from windowState import WindowState

class Cuboid(Figure):
   def __init__(self, state: WindowState, a: float, b: float, c: float):
      super().__init__(state)
      self.type = 'Cuboid'
      self.a = a
      self.b = b
      self.c = c

   def draw(self):
      self._drawTriangle()
      self._drawLines()

   def export(self):
      v = self.createVertices()

      return {
         'Vertices': [
            [*v[0]], [*v[1]], [*v[2]],
            [*v[0]], [*v[2]], [*v[3]],
            [*v[4]], [*v[5]], [*v[6]],
            [*v[4]], [*v[6]], [*v[7]],
            [*v[0]], [*v[1]], [*v[5]],
            [*v[0]], [*v[5]], [*v[4]],
            [*v[1]], [*v[2]], [*v[6]],
            [*v[1]], [*v[6]], [*v[5]],
            [*v[2]], [*v[3]], [*v[7]],
            [*v[2]], [*v[7]], [*v[6]],
            [*v[0]], [*v[3]], [*v[7]],
            [*v[0]], [*v[7]], [*v[4]],
         ]
         , 'Colors': self._generateColorArray(self.figureColor, self.size).tolist()
         , 'LineVertices': [
            [*v[0]], [*v[1]],
            [*v[0]], [*v[3]],
            [*v[0]], [*v[4]],
            [*v[2]], [*v[1]],
            [*v[2]], [*v[3]],
            [*v[2]], [*v[6]],
            [*v[5]], [*v[1]],
            [*v[5]], [*v[4]],
            [*v[5]], [*v[6]],
            [*v[7]], [*v[3]],
            [*v[7]], [*v[4]],
            [*v[7]], [*v[6]],
         ]
         , 'LineColor': self._state.currentLineColor
         , 'Indices': []
      }

   def setup(self):
      v = np.array(self.createVertices())
      self.size = self._bindVertexData(self.vertex_buffer_id, np.array([
         v[0], v[1], v[2],
         v[0], v[2], v[3],
         v[4], v[5], v[6],
         v[4], v[6], v[7],
         v[0], v[1], v[5],
         v[0], v[5], v[4],
         v[1], v[2], v[6],
         v[1], v[6], v[5],
         v[2], v[3], v[7],
         v[2], v[7], v[6],
         v[0], v[3], v[7],
         v[0], v[7], v[4],
      ], dtype=np.float32))

      self._bindColorData(self.vertex_color_id, np.array(self.figureColor, dtype=np.float32), self.size)

      self.lineSize = self._bindVertexData(self.line_buffer_id, np.array([
         v[0], v[1],
         v[0], v[3],
         v[0], v[4],
         v[2], v[1],
         v[2], v[3],
         v[2], v[6],
         v[5], v[1],
         v[5], v[4],
         v[5], v[6],
         v[7], v[3],
         v[7], v[4],
         v[7], v[6],
      ], dtype=np.float32))

      self._bindColorData(self.line_color_id, np.array(self._state.currentLineColor, dtype=np.float32), self.size)

   def createVertices(self):
      return [
         [-self.a/2, -self.b/2, -self.c/2], [self.a/2, -self.b/2, -self.c/2], [self.a/2, -self.b/2, self.c/2], [-self.a/2, -self.b/2, self.c/2],
         [-self.a/2, self.b/2, -self.c/2], [self.a/2, self.b/2, -self.c/2], [self.a/2, self.b/2, self.c/2], [-self.a/2, self.b/2, self.c/2],
      ]