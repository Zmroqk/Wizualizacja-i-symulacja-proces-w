from abc import ABC, abstractmethod
from typing import List
from OpenGL.GLUT import *
from OpenGL.GL import *
from windowState import WindowState

class Figure(ABC):
   def __init__(self, state: WindowState):
      self._state = state

   @abstractmethod
   def draw(self):
      pass

   @abstractmethod
   def createVertices(self):
      pass

   def _startDrawingLines(self):
      glBegin(GL_LINES)

   def _startDrawingTriangles(self):
      glBegin(GL_TRIANGLES)

   def _endDrawingBlock(self):
      glEnd()

   def _drawLine(self, v1: List[float], v2: List[float]):
      glVertex(v1)
      glVertex(v2)

   def _drawTriangle(self, v1: List[float], v2: List[float], v3: List[float]):
      glVertex(v1)
      glVertex(v2)
      glVertex(v3)

   def _setColor(self, r: float, g: float, b: float):
      glColor3f(r, g, b)

   def _restoreColor(self):
      if self._state.currentColor is not None:
         glColor3f(*self._state.currentColor)
   