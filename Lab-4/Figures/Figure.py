from abc import ABC, abstractmethod
import OpenGL.GL as gl
from windowState import WindowState
import numpy as np
import ctypes
from idGenerator import IdGenerator
from IO.FigureFileSchema import FigureFileSchema

class Figure(ABC):
   def __init__(self, state: WindowState):
      self.id = IdGenerator.generateId()
      self.vao = self._create_vao()
      self._state = state
      self.vertex_buffer_id = self._generate_buffer()
      self.vertex_color_id = self._generate_buffer()
      self.line_buffer_id = self._generate_buffer()
      self.line_color_id = self._generate_buffer()
      self.vertex_indices_buffer_id = self._generate_buffer()
      self.globalPosition = [0., 0., 0.]
      self.rotation = [0., 0., 0.]
      self.figureColor = [1., 1., 1.]
      self.size = 0
      self.lineSize = 0
      self.vertices_indices_size = 0
      self.type = None

   @abstractmethod
   def setup(self):
      pass

   @abstractmethod
   def draw(self):
      pass

   @abstractmethod
   def createVertices(self):
      pass

   @abstractmethod
   def export(self) -> FigureFileSchema:
      pass

   def toString(self):
      return f'{self.id} {self.type}'

   def getPosition(self):
      return self.globalPosition

   def getRotation(self):
      return self.rotation

   def _generate_buffer(self) -> int:
      self._bind_vao()
      return gl.glGenBuffers(1)

   def _generateColorArray(self, color, count):
      return np.full((count, 3), color, dtype=np.float32)

   def _bindColorData(self, buffer_id, color, count):
      self._bind_vao()
      colors = self._generateColorArray(color, count)
      gl.glBindBuffer(gl.GL_ARRAY_BUFFER, buffer_id)
      gl.glBufferData(gl.GL_ARRAY_BUFFER, colors.nbytes, colors, gl.GL_STATIC_DRAW)

   def _bindMultipleColorData(self, buffer_id, colors):
      self._bind_vao()
      gl.glBindBuffer(gl.GL_ARRAY_BUFFER, buffer_id)
      gl.glBufferData(gl.GL_ARRAY_BUFFER, colors.nbytes, colors, gl.GL_STATIC_DRAW)

   def _bindVertexData(self, buffer, vertices) -> int:
      self._bind_vao()
      gl.glBindBuffer(gl.GL_ARRAY_BUFFER, buffer)
      gl.glBufferData(gl.GL_ARRAY_BUFFER, vertices.nbytes, vertices, gl.GL_STATIC_DRAW)
      return len(vertices)
   
   def _bindVertexIndicesData(self, buffer, vertices_indices) -> int:
      self._bind_vao()
      gl.glBindBuffer(gl.GL_ELEMENT_ARRAY_BUFFER, buffer)
      gl.glBufferData(gl.GL_ELEMENT_ARRAY_BUFFER, vertices_indices.nbytes, vertices_indices, gl.GL_STATIC_DRAW)
      return len(vertices_indices)
   
   def _drawTriangleFans(self):
      self._bind_vao()

      gl.glEnableVertexAttribArray(1)

      gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vertex_color_id)
      gl.glVertexAttribPointer(1, 3, gl.GL_FLOAT, gl.GL_FALSE, 0, ctypes.c_void_p(0))

      gl.glEnableVertexAttribArray(0)

      gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vertex_buffer_id)
      gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, gl.GL_FALSE, 0, ctypes.c_void_p(0))
      gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 0, self.size)

      gl.glDisableVertexAttribArray(0)
      gl.glDisableVertexAttribArray(1)

   def _drawTriangle(self):
      self._bind_vao()
      gl.glEnableVertexAttribArray(1)

      gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vertex_color_id)
      gl.glVertexAttribPointer(1, 3, gl.GL_FLOAT, gl.GL_FALSE, 0, ctypes.c_void_p(0))

      gl.glEnableVertexAttribArray(0)

      gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vertex_buffer_id)
      gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, gl.GL_FALSE, 0, ctypes.c_void_p(0))
      gl.glDrawArrays(gl.GL_TRIANGLES, 0, self.size)

      gl.glDisableVertexAttribArray(0)
      gl.glDisableVertexAttribArray(1)

   def _drawTrianglesIndices(self):
      self._bind_vao()
      gl.glEnableVertexAttribArray(1)

      gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vertex_color_id)
      gl.glVertexAttribPointer(1, 3, gl.GL_FLOAT, gl.GL_FALSE, 0, ctypes.c_void_p(0))

      gl.glEnableVertexAttribArray(0)

      gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vertex_buffer_id)
      gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, gl.GL_FALSE, 0, ctypes.c_void_p(0))

      gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vertex_indices_buffer_id)
      gl.glDrawElements(gl.GL_TRIANGLES, self.vertices_indices_size, gl.GL_UNSIGNED_INT, None)

      gl.glDisableVertexAttribArray(0)
      gl.glDisableVertexAttribArray(1)

   def _drawLines(self):
      self._bind_vao()
      gl.glEnableVertexAttribArray(1)

      gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.line_color_id)
      gl.glVertexAttribPointer(1, 3, gl.GL_FLOAT, gl.GL_FALSE, 0, ctypes.c_void_p(0))

      gl.glEnableVertexAttribArray(0)

      gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.line_buffer_id)
      gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, gl.GL_FALSE, 0, ctypes.c_void_p(0))
      gl.glDrawArrays(gl.GL_LINES, 0, self.lineSize)

      gl.glDisableVertexAttribArray(1)
      gl.glDisableVertexAttribArray(0)

   def _create_vao(self):
      return gl.glGenVertexArrays(1)

   def _bind_vao(self):
      gl.glBindVertexArray(self.vao)
