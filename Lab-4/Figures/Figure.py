from abc import ABC, abstractmethod
from typing import List
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
      self.triangles = []
      self.verticies = []

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

   def _generate_triangles_from_verticies(self, verticies: List[float]):
      triangles = []
      for i in range(0, len(verticies), 3):
         triangles.append([verticies[i] + self.globalPosition, verticies[i+1] + self.globalPosition, verticies[i+2] + self.globalPosition])
      self.triangles = np.array(triangles)

   def _detect_collision(self, otherFigure):
      self._generate_triangles_from_verticies(self.verticies)
      otherFigure._generate_triangles_from_verticies(otherFigure.verticies)
      for otherTriangle in otherFigure.triangles:
         for triangle in self.triangles:
            n2 = self.__n_param(otherTriangle)
            d2 = self.__d_param(n2, otherTriangle)
            if not self.__check_plane_overlap(d2, n2, triangle):
               return False

            n1 = self.__n_param(triangle)
            d1 = self.__d_param(n1, triangle)
            if not self.__check_plane_overlap(d1, n1, otherTriangle):
               return False
            
            dv10 = np.matmul(n2, triangle[0]) + d2
            dv11 = np.matmul(n2, triangle[1]) + d2
            dv12 = np.matmul(n2, triangle[2]) + d2

            dv20 = np.matmul(n1, otherTriangle[0]) + d1
            dv21 = np.matmul(n1, otherTriangle[1]) + d1
            dv22 = np.matmul(n1, otherTriangle[2]) + d1

            D = np.matmul(n1, n2)
            p10 = D * triangle[0]
            p11 = D * triangle[1]
            p12 = D * triangle[2]

            p20 = D * otherTriangle[0]
            p21 = D * otherTriangle[1]
            p22 = D * otherTriangle[2]

            t11 = p10 + (p11 - p10) * dv10 / (dv10 - dv11)
            t12 = p12 + (p11 - p12) * dv12 / (dv12 - dv11)

            t21 = p20 + (p21 - p20) * dv20 / (dv20 - dv21)
            t22 = p22 + (p21 - p22) * dv22 / (dv22 - dv21)
            print(t11, t12)
            print(t21, t22)


   def __2d_collisionCheck(self, triangle, otherTriangle):
      pass

   def __n_param(self, triangle: List[List[float]]):
      return (triangle[1] - triangle[0]) * (triangle[2] - triangle[0])

   def __d_param(self, n, triangle: List[List[float]]):
      return np.matmul(-n, triangle[0])
   
   def __check_plane_overlap(self, d, n, triangle):
      distance1 = np.matmul(n, triangle[0]) + d
      distance2 = np.matmul(n, triangle[1]) + d
      distance3 = np.matmul(n, triangle[2]) + d
      if np.sign(distance1) == np.sign(distance2) == np.sign(distance3):
         return False
      return True
      