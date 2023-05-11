from abc import ABC, abstractmethod
from typing import List
import OpenGL.GL as gl
from windowState import WindowState
import numpy as np
import ctypes

class Figure(ABC):
   def __init__(self, state: WindowState):
      self._state = state
      self.vertex_buffer_id = self._generate_buffer()
      self.vertex_color_id = self._generate_buffer()
      self.line_buffer_id = self._generate_buffer()
      self.line_color_id = self._generate_buffer()
      self.color = 0
      self.size = 0

   @abstractmethod
   def setup(self):
      pass

   @abstractmethod
   def draw(self):
      pass

   @abstractmethod
   def createVertices(self):
      pass

   def _generate_buffer(self) -> int:
      return gl.glGenBuffers(1)

   def _bindColorData(self, buffer_id, color, count):
      colors = np.full((count, 3), color, dtype=np.float32)
      gl.glBindBuffer(gl.GL_ARRAY_BUFFER, buffer_id)
      gl.glBufferData(gl.GL_ARRAY_BUFFER, colors.nbytes, colors, gl.GL_STATIC_DRAW)

   def _bindVertexData(self, buffer, vertices):
      self.size = len(vertices) * 3
      gl.glBindBuffer(gl.GL_ARRAY_BUFFER, buffer)
      gl.glBufferData(gl.GL_ARRAY_BUFFER, vertices.nbytes, vertices, gl.GL_STATIC_DRAW)
   
   def _drawTriangle(self):
      gl.glEnableVertexAttribArray(1)

      gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vertex_color_id)
      gl.glVertexAttribPointer(1, 3, gl.GL_FLOAT, gl.GL_FALSE, 0, ctypes.c_void_p(0))

      gl.glEnableVertexAttribArray(0)

      gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vertex_buffer_id)
      gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, gl.GL_FALSE, 0, ctypes.c_void_p(0))
      gl.glDrawArrays(gl.GL_TRIANGLES, 0, self.size)

      gl.glDisableVertexAttribArray(0)
      gl.glDisableVertexAttribArray(1)

   def _drawLines(self):
      gl.glEnableVertexAttribArray(1)
      gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.line_color_id)
      gl.glVertexAttribPointer(1, 3, gl.GL_FLOAT, gl.GL_FALSE, 0, ctypes.c_void_p(0))
      gl.glDisableVertexAttribArray(1)
      gl.glEnableVertexAttribArray(0)
      gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.line_buffer_id)
      gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, gl.GL_FALSE, 0, ctypes.c_void_p(0))
      gl.glDrawArrays(gl.GL_LINES, 0, self.size)
      gl.glDisableVertexAttribArray(0)
