import OpenGL.GL as gl
import glfw
import ctypes
import numpy as np
import sys
import shaders
import Figures

class Window_glfw:
   
   def __init__(self, width = 720, height = 480, title = "GLFW Window", monitor = None, share = None) -> None:
      self.window = None
      self.width = width
      self.height = height
      self.title = title
      self.monitor = monitor
      self.share = share
      self.framebuffer_size = None
      self.vao = 0
      self.vertexBuffer = 0
      self.vertexShaderId = 0
      self.fragmentShaderId = 0
      self.vertexes = []
      self.glProgramId = None

   def setup_window(self) -> None:
      if not glfw.init():
         exit(-1)
      self.window = glfw.create_window(self.width, self.height, self.title, self.monitor, self.share)

      if not self.window:
         glfw.terminate()
         exit(-2)

      glfw.make_context_current(self.window)
      glfw.set_key_callback(self.window, self._key_callback)

      glfw.window_hint(glfw.SAMPLES, 4)
      glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
      glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 6)
      glfw.swap_interval(1)
      gl.glEnable(gl.GL_DEPTH_TEST)
      gl.glDepthFunc(gl.GL_LESS)

   def _prepareShaders(self, vertexShaderCode, fragmentShaderCode):
      self.vertexShaderId = gl.glCreateShader(gl.GL_VERTEX_SHADER)
      self.fragmentShaderId = gl.glCreateShader(gl.GL_FRAGMENT_SHADER)
      gl.glShaderSource(self.vertexShaderId, vertexShaderCode)
      gl.glShaderSource(self.fragmentShaderId, fragmentShaderCode)
      gl.glCompileShader(self.vertexShaderId)
      if not gl.glGetShaderiv(self.vertexShaderId, gl.GL_COMPILE_STATUS):
         print('vertex shader: ', str(gl.glGetShaderInfoLog(self.vertexShaderId).decode()), file=sys.stderr)
      gl.glCompileShader(self.fragmentShaderId)
      if not gl.glGetShaderiv(self.fragmentShaderId, gl.GL_COMPILE_STATUS):
         print('fragment shader: ',str(gl.glGetShaderInfoLog(self.fragmentShaderId).decode()), file=sys.stderr)

      self.glProgramId = gl.glCreateProgram()
      gl.glAttachShader(self.glProgramId, self.vertexShaderId)
      gl.glAttachShader(self.glProgramId, self.fragmentShaderId)
      gl.glLinkProgram(self.glProgramId)
      if not gl.glGetProgramiv(self.glProgramId, gl.GL_LINK_STATUS):
         print("p:" + str(gl.glGetProgramInfoLog(self.glProgramId)), file=sys.stderr)
      
      gl.glDetachShader(self.glProgramId, self.vertexShaderId)
      gl.glDetachShader(self.glProgramId, self.fragmentShaderId)

      gl.glDeleteShader(self.vertexShaderId)
      gl.glDeleteShader(self.fragmentShaderId)

   def _setup_draw(self):
      self.vao = gl.glGenVertexArrays(1)
      gl.glBindVertexArray(self.vao)
      # self.vertexes = np.array([(-1., -1., 0)
      #                           , (1., -1., 0)
      #                           , (1., 1., 0)
      #                           , (-1., -1., 0)
      #                           , (1., 1., 0)
      #                           , (-1., 1., 0)], dtype=np.float32)
      # self.vertexBuffer = gl.glGenBuffers(1)
      # gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vertexBuffer)
      # gl.glBufferData(gl.GL_ARRAY_BUFFER, self.vertexes.nbytes, self.vertexes, gl.GL_STATIC_DRAW)

   def _key_callback(self, window, key: int, scancode: int, action: int, mods: int):
      if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
         glfw.set_window_should_close(self.window, glfw.TRUE)

   def _test_draw(self):
      gl.glEnableVertexAttribArray(0)
      gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vertexBuffer)
      gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, gl.GL_FALSE, 0, ctypes.c_void_p(0))
      gl.glDrawArrays(gl.GL_TRIANGLES, 0, 6)
      gl.glDisableVertexAttribArray(0)


   def run_main_loop(self):
      self._setup_draw()
      cuboid = Figures.Cuboid(None, 1, 1, 1)
      cuboid.setup()

      self._prepareShaders(shaders.vsc, shaders.fsc)
      while not glfw.window_should_close(self.window):       
         self.framebuffer_size = glfw.get_framebuffer_size(self.window)
         gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

         # draw
         gl.glUseProgram(self.glProgramId)
         #self._test_draw()      
         cuboid.draw() 
         # end draw

         glfw.swap_buffers(self.window)
         glfw.poll_events()

      glfw.terminate()
      exit(0)

window = Window_glfw()
window.setup_window()
window.run_main_loop()