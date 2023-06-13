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
      self.isColliding = False
      self.epsilon = 0.00001

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
         triangles.append([verticies[i], verticies[i+1], verticies[i+2]])
      self.triangles = np.array(triangles, dtype=np.float32)

   def _detect_collision(self, otherFigure: 'Figure'):
      self._generate_triangles_from_verticies(self.verticies)
      otherFigure._generate_triangles_from_verticies(otherFigure.verticies)
      for otherTriangle in otherFigure.triangles:
         for triangle in self.triangles:
            if self._check_triangle_collision(triangle, otherTriangle):
               return True
      if self.isColliding:
         self.isColliding = False
         self.setup()
      return False

   def _check_triangle_collision(self, triangle, otherTriangle):
      if self._state.debug:
         print('triangle:', triangle)
         print('otherTriangle:', otherTriangle)

      n2 = self.__n_param(otherTriangle)
      d2 = self.__d_param(n2, otherTriangle)

      if self.__check_plane_overlap(d2, n2, triangle) is False:
         return False

      n1 = self.__n_param(triangle)
      d1 = self.__d_param(n1, triangle)
      if self.__check_plane_overlap(d1, n1, otherTriangle) is False:
         return False
      
      dv10 = np.dot(n2, triangle[0]) + d2
      dv11 = np.dot(n2, triangle[1]) + d2
      dv12 = np.dot(n2, triangle[2]) + d2

      dv20 = np.dot(n1, otherTriangle[0]) + d1
      dv21 = np.dot(n1, otherTriangle[1]) + d1
      dv22 = np.dot(n1, otherTriangle[2]) + d1 

      if dv10 < self.epsilon:
         dv10 = 0
      if dv11 < self.epsilon:
         dv11 = 0
      if dv12 < self.epsilon:
         dv12 = 0
      if dv20 < self.epsilon:
         dv20 = 0
      if dv21 < self.epsilon:
         dv21 = 0
      if dv22 < self.epsilon:
         dv22 = 0

      if dv10 == dv11 == dv12 == 0:
         if self.__2d_collisionCheck(triangle, otherTriangle) or self.__2d_collisionCheck(otherTriangle, triangle):
            self.isColliding = True
            self.setup()
            if self._state.debug:
               print('2d colision detected')
            return True
         return False

      if self._state.debug:
         print('dv10, dv11, dv12, dv20, dv21, dv22', dv10, dv11, dv12, dv20, dv21, dv22)

      if np.sign(dv10) == np.sign(dv11):
         return self._check_triangle_collision([triangle[0], triangle[2], triangle[1]], otherTriangle)
      if np.sign(dv11) == np.sign(dv12):
         return self._check_triangle_collision([triangle[1], triangle[0], triangle[2]], otherTriangle)
      if np.sign(dv20) == np.sign(dv21):
         return self._check_triangle_collision(triangle, [otherTriangle[0], otherTriangle[2], otherTriangle[1]])
      if np.sign(dv21) == np.sign(dv22):
         return self._check_triangle_collision(triangle, [otherTriangle[1], otherTriangle[0], otherTriangle[2]])

      D = np.cross(n1, n2)
      p10 = self.__get_p_param(triangle[0], D)
      p11 = self.__get_p_param(triangle[1], D)
      p12 = self.__get_p_param(triangle[2], D)
      p20 = self.__get_p_param(otherTriangle[0], D)
      p21 = self.__get_p_param(otherTriangle[1], D)
      p22 = self.__get_p_param(otherTriangle[2], D)

      t11 = p10 + (p11 - p10) * dv10 / (dv10 - dv11)
      t12 = p12 + (p11 - p12) * dv12 / (dv12 - dv11)

      t21 = p20 + (p21 - p20) * dv20 / (dv20 - dv21)
      t22 = p22 + (p21 - p22) * dv22 / (dv22 - dv21)
      if self._state.debug:
         print('t11, t12, t21, t22', t11, t12, t21, t22)
      if t11 < t21 < t12 or t11 < t22 < t12 or t21 < t11 < t22 or t21 < t12 < t22 \
         or t11 > t21 > t12 or t11 > t22 > t12 or t21 > t11 > t22 or t21 > t12 > t22:
         self.isColliding = True
         self.setup()
         if self._state.debug:
            interval = t21
            if t11 < t21 < t12 or t11 > t21 > t12:
               interval = t21
            if t11 < t22 < t12 or t11 > t22 > t12:
               interval = t22
            if t21 < t11 < t22 or t21 > t11 > t22:
               interval = t11
            if t21 < t12 < t22 or t21 > t12 > t22:
               interval = t12
            print(f'Collision for figure with id {self.id} detected at:', interval * D)            
         return True
      return False

   def __get_p_param(self, vertex, D):
      return np.dot(D, vertex)

   def __2d_collisionCheck(self, triangle, otherTriangle):
      for point in otherTriangle:
         if self.__sameSide(point, triangle[0], triangle[1], triangle[2]) \
            and self.__sameSide(point, triangle[1], triangle[0], triangle[2]) \
            and self.__sameSide(point, triangle[2], triangle[0], triangle[1]):
            return True
      return False

   def __sameSide(self, p1, p2, a, b):
      cp1 = np.cross(b - a, p1 - a)
      cp2 = np.cross(b - a, p2 - a)
      if np.dot(cp1, cp2) >= 0:
         return True
      return False

   def __n_param(self, triangle: List[List[float]]):
      return np.cross(triangle[1] - triangle[0], triangle[2] - triangle[0])

   def __d_param(self, n, triangle: List[List[float]]):
      if self._state.debug:
         print('n:', n)
      return np.dot(np.negative(n), triangle[0])
   
   def __check_plane_overlap(self, d, n, triangle):
      distance1 = np.matmul(n, triangle[0]) + d
      distance2 = np.matmul(n, triangle[1]) + d
      distance3 = np.matmul(n, triangle[2]) + d
      if (distance1 != 0 or distance2 != 0 or distance3 != 0) and np.sign(distance1) == np.sign(distance2) == np.sign(distance3):
         return False
      return True
      