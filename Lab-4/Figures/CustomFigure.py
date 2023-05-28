from Figures.Figure import Figure
from windowState import WindowState
from typing import List
import numpy as np
import vectorOperations as vo

class CustomFigure(Figure):
   def __init__(self, state: WindowState
      , verticies: List[List[float]]
      , colors: List[List[float]]
      , lineVertices: List[List[float]] = []
      , lineColor: List[float] = [0, 0, 0]
      , indices: List[float] = []
      ):
      super().__init__(state)
      self.type = 'Custom figure'
      self.verticies = verticies 
      self.colors = colors
      self.lineVertices = lineVertices
      self.lineColor = lineColor
      self.indices = indices

   def setup(self):
      self.size = self._bindVertexData(self.vertex_buffer_id, np.array(vo.applyPosition(self.verticies, *self._state.cameraTarget), dtype=np.float32))
      self._bindMultipleColorData(self.vertex_color_id, np.array(self.colors, dtype=np.float32))
      if len(self.indices) > 0:
         self.vertices_indices_size = self._bindVertexIndicesData(self.vertex_indices_buffer_id, np.array(self.indices, dtype=np.int32))
      if len(self.lineVertices) > 0:
         self.lineSize = self._bindVertexData(self.line_buffer_id, np.array(vo.applyPosition(self.lineVertices, *self._state.cameraTarget), dtype=np.float32))
         self._bindColorData(self.line_color_id, np.array(self.lineColor, dtype=np.float32), self.lineSize)

   def draw(self):
      if len(self.indices) > 0:
         self._drawTrianglesIndices()
      else:
         self._drawTriangle()
      self._drawLines()
   
   def export(self):
      return {
         'Verticies': self.verticies
         , 'Colors': self.colors
         , 'LineVerticies': self.lineVertices
         , 'LineColor': self.lineColor
         , 'Indicies': self.indices
      }
   
   def createVertices(self):
      return []