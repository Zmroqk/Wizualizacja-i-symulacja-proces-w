from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLUT.fonts import *
from typing import Tuple
import random
import time
import math
import ctypes
import vectorOperations as vo
import Figures as f
import windowState as ws

import numpy as np

class Window:
   
   def __init__(self
      , width = 640
      , height = 480
      , name = "Window"
      , background : Tuple[float, float, float, float] = (0.,0.,0.,0.)
      , msaa = True
      ):
      self.width = width
      self.height = height
      self.name = name
      self.background = background
      self.showFunc = None
      self.printFunc = None
      self.run = False
      self.commandMode = False
      self.command = ""
      self.matrix_stack_count = 0
      self.figures = []
      self.rotation_quality = 5
      self.autoRotationEnabled = False
      self.msaa = msaa
      self.state = ws.WindowState()

   def SetupWindow(self):
      glutInit()
      self.__setupOptionalFunctionalities()
      glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH | GLUT_MULTISAMPLE)
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

   def __setupOptionalFunctionalities(self):
      if self.msaa:
         glEnable(GL_MULTISAMPLE)
         glutSetOption(GLUT_MULTISAMPLE, 8)

   def __setupViewPort(self):
      glViewport(0, 0, 640, 480)
      self.__perspecitve_rendering()

   def __keyboardCommand(self, char, x, y):
      if self.commandMode and char != b'\r':
         if char == b'\x08':
            self.command = self.command[:-1]
         else:   
            self.command += char.decode('utf-8')
      elif self.commandMode and char == b'\r':
         self.commandMode = False
         self.printFunc = None
         self.__handleCommand()
      elif char == b' ':
         self.commandMode = not self.commandMode
         self.command = ""
         self.printFunc = self.__print_text
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
      figure: f.Figure = None
      if self.command.startswith('cube'):
         figure = f.Cube(self.state, int(params[0]))
      elif self.command.startswith('cuboid'):
         figure = f.Cuboid(self.state, *map(lambda x: int(x), params))
      elif self.command.startswith('pyramid'):
         figure = f.Pyramid(self.state, *map(lambda x: float(x), params))
      elif self.command.startswith('circle'):
         figure = f.Circle(self.state, polygonSideLength=float(params[0]), is2d=params[1] == 'True')
      elif self.command.startswith('cylinder'):
         figure = f.Cylinder(self.state, float(params[0]), float(params[1]))
      elif self.command.startswith('cone'):
         figure = f.Cone(self.state, float(params[0]), float(params[1]))
      elif self.command.startswith('sphere'):
         figure = f.Sphere(self.state, float(params[0]), int(params[1]))
      elif self.command.startswith('autorotation'):
         self.autoRotationEnabled = True
         self.state.currentRotation = 0
         if params[1] == 'x':
            self.state.currentRotationType = vo.Rotation.OX
         elif params[1] == 'y':
            self.state.currentRotationType = vo.Rotation.OY
         else:
            self.state.currentRotationType = vo.Rotation.OZ
         glutTimerFunc(17, self.__autoRotation, int(params[0]))
      elif self.command.startswith('disable-autorotation'):
         self.autoRotationEnabled = False
      elif self.command.startswith('color'):
         self.state.currentColor = [float(params[0]), float(params[1]), float(params[2])]
         glColor3f(*self.state.currentColor)
      elif self.command.startswith('quality'):
         self.state.circleQuality = int(params[0])
      elif self.command.startswith('rotation-quality'):
         self.rotation_quality = int(params[0])
      elif self.command.startswith('exit'):
         self.exit()
      elif self.command.startswith('help'):
         self.printFunc = self.__print_help
      
      if figure is not None:
         self.showFunc = figure.draw

   def __windowLoop(self):
      glClearColor(*self.background)
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
      if self.printFunc is not None:
         self.printFunc()
      if self.showFunc is not None:
         self.showFunc()
      glutSwapBuffers()

   def __timerLoop(self, time):
      glutPostRedisplay()
      if self.run is True:
         glutTimerFunc(17, self.__timerLoop, 0)

   def __print_string(self, text, startX=10, y = 10):
      x = startX
      for char in text:
         glWindowPos2i(x, y)
         glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ctypes.c_int(ord(char)))
         x += glutBitmapWidth(GLUT_BITMAP_TIMES_ROMAN_24, ctypes.c_int(ord(char)))

   def __get_string_width(self, text):
      x = 0
      for char in text:
         x += glutBitmapWidth(GLUT_BITMAP_TIMES_ROMAN_24, ctypes.c_int(ord(char)))
      return x

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
      glOrtho(0, self.width, 0, self.height, -2, 10)
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

   def __autoRotation(self, speed):
      self.state.currentRotation += (1/self.rotation_quality)/(2*np.pi)
      if self.autoRotationEnabled is True:
         glutTimerFunc(int(1000./speed), self.__autoRotation, speed)

   def __print_text(self):
      glColor3f(1.0, 1.0, 1.0)
      width = self.__get_string_width("Command: ")
      self.__print_string("Command: ")
      self.__print_string(self.command, startX=10 + width)
      glColor3f(*self.state.currentColor)

   def __print_help(self):
      glColor3f(1.0, 1.0, 1.0)
      self.__print_string("Manual", y = self.height - 20)
      self.__print_string("wsadqe - movement", y = self.height - 40)
      self.__print_string("uiojkl - rotation", y = self.height - 60)
      self.__print_string("exit", y = self.height - 80)
      self.__print_string("quality <n> - sets circle quality", y = self.height - 100)
      self.__print_string("rotation-quality <n> - sets rotation quality", y = self.height - 120)
      self.__print_string("color <r> <g> <b> - sets color", y = self.height - 140)
      self.__print_string("0, 9 - sets background color (from black to white)", y = self.height - 160)
      self.__print_string("cube <a> - creates cube", y = self.height - 180)
      self.__print_string("cuboid <a> <b> <c> - creates cuboid", y = self.height - 200)
      self.__print_string("circle <a> <bool> - a => length | bool => is2d", y = self.height - 220)
      self.__print_string("cylinder <r> <h> - r => radius | h => height", y = self.height - 240)

   def exit(self):
      self.run = False
      glutLeaveMainLoop()
      exit(-1)

window = Window()
window.SetupWindow()