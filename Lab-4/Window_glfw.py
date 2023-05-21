import OpenGL.GL as gl
import glfw
import sys
import shaders
from windowState import WindowState
import vectorOperations as vo
import Commands
import camera as c
import numpy as np

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
      self.state = WindowState()
      self.commandDispatcher = Commands.CommandDispatcher(self.state)

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

      gl.glUseProgram(self.glProgramId)
      self.matrixLocationId = gl.glGetUniformLocation(self.glProgramId, "position")
      self.rotationLocationId = gl.glGetUniformLocation(self.glProgramId, "rotation")
      self.cameraLocationId = gl.glGetUniformLocation(self.glProgramId, "camera")

   def _key_callback(self, window, key: int, scancode: int, action: int, mods: int):
      try:
         self.commandDispatcher.dispatch(self.window, key, scancode, action, mods)
      except Exception as e:
         print(e)

   def run_main_loop(self):
      self._prepareShaders(shaders.vsc, shaders.fsc)
      while not glfw.window_should_close(self.window):       
         self.framebuffer_size = glfw.get_framebuffer_size(self.window)
         gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

         # draw
         gl.glUseProgram(self.glProgramId)
         gl.glUniformMatrix4fv(self.cameraLocationId, 1, gl.GL_FALSE, c.getCamera(self.state.currentCamera
            , distance = self.state.cameraDistance
            , rotX = self.state.cameraXRotation
            , rotZ = self.state.cameraZRotation
            , near = self.state.cameraNear
            , far = self.state.cameraFar
            , state = self.state
         ))   
         for figure in self.state.figures.values():
            gl.glUniform3f(self.matrixLocationId, *figure.getPosition())
            gl.glUniform3f(self.rotationLocationId, *figure.getRotation())
            figure.draw()
         # end draw
         glfw.swap_buffers(self.window)
         glfw.poll_events()

      glfw.terminate()
      exit(0)

window = Window_glfw(width=720, height=720)
window.setup_window()
window.run_main_loop()