from Figures.Figure import Figure
from vectorOperations import *
from typing import List
from windowState import WindowState

class Cuboid(Figure):
   def __init__(self, state: WindowState, a: float, b: float, c: float):
      super(Cuboid, self).__init__(state)
      self.a = a
      self.b = b
      self.c = c

   # def draw(self):
   #    # v = applyRotation(self.createVertices(), self._state.currentRotation, self._state.currentRotationType)
   #    # v = applyRotationAll(self.createVertices(), self._state.currentRotation)
   #    # v = applyPosition(v, *self._state.currentPosition)

   #    # self._setColor(*self._state.currentColor)

   #    # self._startDrawingTriangles()
   #    # self._drawTriangle(v[0], v[1], v[2]) #DOWN
   #    # self._drawTriangle(v[0], v[2], v[3]) #DOWN
   #    # self._drawTriangle(v[4], v[5], v[6]) #UP
   #    # self._drawTriangle(v[4], v[6], v[7]) #UP
   #    # self._drawTriangle(v[0], v[1], v[5]) #SIDE
   #    # self._drawTriangle(v[0], v[5], v[4]) #SIDE
   #    # self._drawTriangle(v[1], v[2], v[6]) #SIDE 2
   #    # self._drawTriangle(v[1], v[6], v[5]) #SIDE 2
   #    # self._drawTriangle(v[2], v[3], v[7]) #SIDE 3
   #    # self._drawTriangle(v[2], v[7], v[6]) #SIDE 3
   #    # self._drawTriangle(v[0], v[3], v[7]) #SIDE 4
   #    # self._drawTriangle(v[0], v[7], v[4]) #SIDE 4
   #    # self._endDrawingBlock()

   #    # self._setColor(0, 0, 0)

   #    # self._startDrawingLines()
   #    # self._drawLine(v[0], v[1])
   #    # self._drawLine(v[0], v[3])
   #    # self._drawLine(v[0], v[4])
   #    # self._drawLine(v[2], v[1])
   #    # self._drawLine(v[2], v[3])
   #    # self._drawLine(v[2], v[6])
   #    # self._drawLine(v[5], v[1])
   #    # self._drawLine(v[5], v[4])
   #    # self._drawLine(v[5], v[6])
   #    # self._drawLine(v[7], v[3])
   #    # self._drawLine(v[7], v[4])
   #    # self._drawLine(v[7], v[6])
   #    # self._endDrawingBlock()

   #    self._restoreColor()
   
   def draw(self):
      self._drawTriangle()
      self._drawLines()

   def setup(self):
      v = np.array(applyRotationAll(self.createVertices(), [np.pi/1.5, np.pi/1.5, np.pi/2.4]))
      self._bindVertexData(self.vertex_buffer_id, np.array([
         *v[0], *v[1], *v[2],
         *v[0], *v[2], *v[3],
         *v[4], *v[5], *v[6],
         *v[4], *v[6], *v[7],
         *v[0], *v[1], *v[5],
         *v[0], *v[5], *v[4],
         *v[1], *v[2], *v[6],
         *v[1], *v[6], *v[5],
         *v[2], *v[3], *v[7],
         *v[2], *v[7], *v[6],
         *v[0], *v[3], *v[7],
         *v[0], *v[7], *v[4],
      ], dtype=np.float32))

      self._bindColorData(self.vertex_color_id, np.array([0, 1, 0], dtype=np.float32), self.size)

      self._bindVertexData(self.line_buffer_id, np.array([
         *v[0], *v[1],
         *v[0], *v[3],
         *v[0], *v[4],
         *v[2], *v[1],
         *v[2], *v[3],
         *v[2], *v[6],
         *v[5], *v[1],
         *v[5], *v[4],
         *v[5], *v[6],
         *v[7], *v[3],
         *v[7], *v[4],
         *v[7], *v[6],
      ], dtype=np.float32))

      self._bindColorData(self.line_color_id, np.array([0, 0, 0], dtype=np.float32), self.size)

   def createVertices(self):
      return [
         [-self.a/2, -self.b/2, -self.c/2], [self.a/2, -self.b/2, -self.c/2], [self.a/2, -self.b/2, self.c/2], [-self.a/2, -self.b/2, self.c/2],
         [-self.a/2, self.b/2, -self.c/2], [self.a/2, self.b/2, -self.c/2], [self.a/2, self.b/2, self.c/2], [-self.a/2, self.b/2, self.c/2],
      ]