from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLUT.fonts import *
from typing import Tuple
import random
import time
import math

import numpy as np

class Window:
   
   def __init__(self
      , width = 640
      , height = 480
      , name = "Window"
      , background : Tuple[float, float, float, float] = (0.,0.,0.,0.)
      ):
      self.width = width
      self.height = height
      self.name = name
      self.background = background
      self.showFunc = None
      self.run = False
      self.commandMode = False
      self.command = ""
      self.matrix_stack_count = 0
      self.figures = []
      self.circle_quality = 20
      self.autoRotationEnabled = False
      self.rotation = [1, 1, 1]

   def SetupWindow(self):
      glutInit()
      glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
      glutInitWindowSize(self.width, self.height)
      glutCreateWindow(self.name)
      glClearColor(*self.background)
      glEnable(GL_DEPTH_TEST)
      glDepthFunc(GL_LESS)
      glutKeyboardFunc(self.__keyboardCommand)
      glutDisplayFunc(self.__windowLoop)
      glutTimerFunc(17, self.__timerLoop, 0)
      self.run = True
      self.__setupViewPort()
      glutMainLoop()

   def __setupViewPort(self):
      glViewport(0, 0, 640, 480)
      self.__perspecitve_rendering()

   def __keyboardCommand(self, char, x, y):
      if self.commandMode and char != b'\r':
         if char == b'\x08':
            self.command = self.command[:-1]
         else:   
            self.command += char.decode('utf-8')
         os.system('clear')
         # self.__print_text(char)
         print(self.command)
      elif self.commandMode and char == b'\r':
         self.commandMode = False
         self.__handleCommand()
      elif char == b' ':
         self.commandMode = not self.commandMode
         self.command = ""
         print('Command mode enabled')
      elif char == b'2':
         pass
      elif char == b'0':
         self.background = (self.background[0] + 0.1, self.background[1] + 0.1, self.background[2] + 0.1, self.background[3] + 0.1)
      elif char == b'9':
         self.background = (self.background[0] - 0.1, self.background[1] - 0.1, self.background[2] - 0.1, self.background[3] - 0.1)
      else:
         self.__handleLocation(char)
         self.__handleRotation(char)
      glutPostRedisplay()

   def __handleLocation(self, char):
      if char == b'w':
         glTranslate(0, 1, 0)
      elif char == b's':
         glTranslate(0, -1, 0)
      elif char == b'a':
         glTranslate(-1, 0, 0)
      elif char == b'd':
         glTranslate(1, 0, 0)
      elif char == b'q':
         glTranslate(0, 0, -1)
      elif char == b'e':
         glTranslate(0, 0, 1)

   def __handleRotation(self, char):
      mod = glutGetModifiers()
      multiplier = 1
      if mod == GLUT_ACTIVE_ALT:
         multiplier = 6
      if char == b'u':
         glRotate(5 * multiplier, 0, 1, 0)
      elif char == b'o':
         glRotate(5 * multiplier, 0, -1, 0)
      elif char == b'i':
         glRotate(5 * multiplier, 1, 0, 0)
      elif char == b'k':
         glRotate(5 * multiplier, -1, 0, 0)
      elif char == b'j':
         glRotate(5 * multiplier, 0, 0, 1)
      elif char == b'l':
         glRotate(5 * multiplier, 0, 0, -1)

   def __handleCommand(self):
      print('Executing command')
      params = self.command.split(' ')[1:]
      if self.command.startswith('cube'):
         self.showFunc = self.__cube(params[0])
      elif self.command.startswith('cuboid'):
         self.showFunc = self.__cuboid(*map(lambda x: int(x), params))
      elif self.command.startswith('pyramid'):
         self.showFunc = self.__pyramid(*map(lambda x: int(x), params))
      elif self.command.startswith('circle'):
         self.showFunc = self.__circle(int(params[0]), float(params[1]), params[2] == 'True')
      elif self.command.startswith('cylinder'):
         self.showFunc = self.__cylinder(float(params[0]), float(params[1]))
      elif self.command.startswith('sphere'):
         self.showFunc = self.__sphere(float(params[0]), int(params[1]))
      elif self.command.startswith('autorotation'):
         self.autoRotationEnabled = True
         self.rotation = [1, 1, 1]
         glutTimerFunc(17, self.__autoRotation, params[0])
      elif self.command.startswith('disable-autorotation'):
         self.autoRotationEnabled = False
      elif self.command.startswith('cone'):
         self.showFunc = self.__cone(float(params[0]), float(params[1]))
      elif self.command.startswith('color'):
         glColor3f(float(params[0]), float(params[1]), float(params[2]))
      elif self.command.startswith('quality'):
         self.circle_quality = int(params[0])

   def __windowLoop(self):
      glClearColor(*self.background)
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
      glPushMatrix()
      if self.showFunc is not None:
         self.showFunc()
      glutSwapBuffers()
      glPopMatrix()

   def __timerLoop(self, time):
      glutPostRedisplay()
      glutTimerFunc(17, self.__timerLoop, 0)

   def __polygon(self):
      pass

   def __circle(self, side_number, side_length, is2d = True, x = 0., y = 0.):
      def __circle_gl():
         angleIncrement = 360. / side_number
         angleIncrement *= np.pi / 180

         glBegin(GL_TRIANGLE_FAN)

         angle = 0.
         
         r = side_length / (2 * np.sin(side_length / 2))

         v = []

         for _ in range(side_number):
            if is2d is True:
               v.append([r * np.cos(angle) + x, np.sin(angle) + y, 0.])
               glVertex3f(r * np.cos(angle) + x, np.sin(angle) + y, 0.)
            else:
               v.append([r * np.cos(angle) + x, y, np.sin(angle)])
               glVertex3f(r * np.cos(angle) + x, y, np.sin(angle))
            angle += angleIncrement
         glEnd()
         self.figures.append(v)
      return __circle_gl

   def __cylinder(self, r, h):
      def __cylinder_gl():
         n = self.circle_quality
         a = 2 * r * np.tan(np.pi/n) # a = 2r tg(pi/n)
         self.__circle(n, a, False)()
         self.__circle(n, a, False, 0, h)()
         vLow = self.figures[-2]
         vHigh = self.figures[-1]
         glBegin(GL_TRIANGLES)
         for i in range(len(vLow) - 1):
            glVertex(vLow[i]);glVertex(vLow[i+1]);glVertex(vHigh[i])
            glVertex(vHigh[i]);glVertex(vHigh[i+1]);glVertex(vLow[i+1])
         glVertex(vLow[0]);glVertex(vLow[-1]);glVertex(vHigh[0])
         glVertex(vHigh[0]);glVertex(vHigh[-1]);glVertex(vLow[-1])
         glEnd()
      return __cylinder_gl

   def __autoRotation(self, speed):
      ox = np.array([[1, 0, 0], [0, np.cos(1), -np.sin(1)], [0, np.sin(1), np.cos(1)]])
      newRotation = np.matmul(self.rotation, ox)
      glRotatef(speed, newRotation[0] - self.rotation[0], newRotation[1] - self.rotation[1], newRotation[2] - self.rotation[2])
      self.rotation = newRotation
      if self.autoRotationEnabled is True:
         glutTimerFunc(17, self.__autoRotation, speed)

   def __cone(self, r, h):
      def __cone_gl():
         n = self.circle_quality
         a = 2 * r * np.tan(np.pi/n) # a = 2r tg(pi/n)
         self.__circle(n, a, False)()
         v = self.figures[-1]
         vTop = [0., h, 0.]
         glBegin(GL_TRIANGLES)
         for i in range(len(v) - 1):
            glVertex(v[i]);glVertex(v[i+1]);glVertex(vTop)
         glVertex(v[0]);glVertex(v[-1]);glVertex(vTop)
         glEnd()
      return __cone_gl


   def __cube(self, a):
      def __cube_gl():
         self.__cuboid(a, a, a)()
      
      return __cube_gl

   def __cuboid(self, a, b, c):
      def __cuboid_gl():
         v = [
            [-a/2, -b/2, -c/2], [a/2, -b/2, -c/2], [a/2, -b/2, c/2], [-a/2, -b/2, c/2],
            [-a/2, b/2, -c/2], [a/2, b/2, -c/2], [a/2, b/2, c/2], [-a/2, b/2, c/2],
         ]
         glBegin(GL_TRIANGLES)
         glColor3f(1.0, 0.0, 0.0)
         glVertex(v[0]);glVertex(v[1]);glVertex(v[2]) # DOWN
         glVertex(v[0]);glVertex(v[2]);glVertex(v[3]) # DOWN
         glVertex(v[4]);glVertex(v[5]);glVertex(v[6]) # UP
         glVertex(v[4]);glVertex(v[6]);glVertex(v[7]) # UP
         glVertex(v[0]);glVertex(v[1]);glVertex(v[5]) # SIDE
         glVertex(v[0]);glVertex(v[5]);glVertex(v[4]) # SIDE
         glVertex(v[1]);glVertex(v[2]);glVertex(v[6]) # SIDE 2
         glVertex(v[1]);glVertex(v[6]);glVertex(v[5]) # SIDE 2
         glVertex(v[2]);glVertex(v[3]);glVertex(v[7]) # SIDE 3
         glVertex(v[2]);glVertex(v[7]);glVertex(v[6]) # SIDE 3
         glVertex(v[0]);glVertex(v[3]);glVertex(v[7]) # SIDE 4
         glVertex(v[0]);glVertex(v[7]);glVertex(v[4]) # SIDE 4
         glEnd()
      return __cuboid_gl

   def __print_text(self, char):
      self.__ortogtaphic_rendering()
      glColor3f(0.0, 1.0, 0.0)
      glRasterPos2f(10, 10)
      print(GLUT_BITMAP_TIMES_ROMAN_24)
      glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, int.from_bytes(char, 'big'))
      self.__reset_matrixes()
      # self.__perspecitve_rendering()

   def __perspecitve_rendering(self):
      if self.matrix_stack_count > 0:
         self.__reset_matrixes()
      glMatrixMode(GL_PROJECTION)
      self.__push_matrixes()
      glFrustum(-2, 2, -2, 2, 1, 10)
      glMatrixMode(GL_MODELVIEW)
      self.__push_matrixes()
      self.matrix_stack_count += 1

   def __ortogtaphic_rendering(self):
      if self.matrix_stack_count > 0:
         self.__reset_matrixes()
      glMatrixMode(GL_PROJECTION)
      self.__push_matrixes()
      glOrtho(0, self.width, 0, self.height, 1, 10)
      glMatrixMode(GL_MODELVIEW)
      self.__push_matrixes()
      self.matrix_stack_count += 1

   def __push_matrixes(self):
      glPushMatrix()
      glLoadIdentity()

   def __reset_matrixes(self):
      glMatrixMode(GL_PROJECTION)
      glPopMatrix()
      glMatrixMode(GL_MODELVIEW)
      glPopMatrix()
      self.matrix_stack_count -= 1

   def __pyramid(self, h, d):
      def __pyramid_gl():
         v = [
            [-d/2, 0, 0], [d/2, 0, 0], [0, 0, (math.sqrt(3) * d)/2],
            [0, h, (math.sqrt(3) * d)/4]
         ]
         glBegin(GL_TRIANGLES)
         glColor3f(1.0, 0.0, 0.0)
         glVertex(v[0]);glVertex(v[1]);glVertex(v[2]) # DOWN
         glVertex(v[0]);glVertex(v[1]);glVertex(v[3]) # SIDE
         glVertex(v[1]);glVertex(v[2]);glVertex(v[3]) # SIDE
         glVertex(v[0]);glVertex(v[2]);glVertex(v[3]) # SIDE
         glEnd()
      return __pyramid_gl

   def __sphere(self, r, rings):
      def __sphere_gl():
         n = self.circle_quality
         a = 2 * r * np.tan(np.pi/n) # a = 2r tg(pi/n)
         glBegin(GL_POINTS)
         glVertex(0,0,0)
         glEnd()
         rotationChange = 180./rings
         for i in range(rings):
            glPushMatrix()
            glRotatef(rotationChange * i, 0, 0, 1)
            self.__circle(n, a, False)()       
            glPopMatrix()
      return __sphere_gl

   def exit(self):
      self.run = False
      exit(-1)

window = Window()
window.SetupWindow()