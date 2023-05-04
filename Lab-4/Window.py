from OpenGL.GLUT import *
from OpenGL.GL import *
from typing import Tuple
import time
import math

class Window:
   
   def __init__(self
      , width = 640
      , height = 480
      , name = "Window"
      , background : Tuple[float, float, float, float] = (1.,1.,1.,1.)
      ):
      self.width = width
      self.height = height
      self.name = name
      self.background = background
      self.showFunc = None
      self.run = False
      self.commandMode = False
      self.command = ""

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
      self.run = True
      self.__setupViewPort()
      glutMainLoop()

   def __setupViewPort(self):
      glViewport(0, 0, 640, 480)
      glMatrixMode(GL_PROJECTION)
      glLoadIdentity()
      glFrustum(-2, 2, -2, 2, 1, 10)
      glMatrixMode(GL_MODELVIEW)

   def __keyboardCommand(self, char, x, y):
      if self.commandMode and char != b'\r':
         if char == b'\x08':
            self.command = self.command[:-1]
         else:   
            self.command += char.decode('utf-8')
         os.system('clear')
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

   def __handleCommand(self):
      print('Executing command')
      if self.command == 'cube':
         self.showFunc = self.__cube
      elif self.command.startswith('cuboid'):
         params = self.command.split(' ')[1:]
         self.showFunc = self.__cuboid(*map(lambda x: int(x), params))
      elif self.command.startswith('pyramid'):
         params = self.command.split(' ')[1:]
         self.showFunc = self.__pyramid(*map(lambda x: int(x), params))

   def __windowLoop(self):
      glClearColor(*self.background)
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
      if self.showFunc is not None:
         self.showFunc()
      glutSwapBuffers()

   def __polygon(self):
      pass

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

   def __cube(self):
      p = [
            [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
            [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
      ]

      glBegin(GL_TRIANGLES)
      glColor3f(1.0, 0.0, 0.0)
      glVertex(p[0])
      glVertex(p[1])
      glVertex(p[2])
      glVertex(p[0])
      glVertex(p[2])
      glVertex(p[3])
      glColor3f(0.0, 1.0, 0.0)
      glVertex(p[1])
      glVertex(p[5])
      glVertex(p[2])
      glVertex(p[2])
      glVertex(p[5])
      glVertex(p[6])
      glColor3f(0.0, 0.0, 1.0)
      glVertex(p[0])
      glVertex(p[4])
      glVertex(p[3])
      glVertex(p[3])
      glVertex(p[4])
      glVertex(p[7])
      glEnd()

   def exit(self):
      self.run = False
      exit(-1)

