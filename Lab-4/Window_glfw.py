import OpenGL.GL as gl
import glfw

class Window_glfw:
   
   def __init__(self, width = 720, height = 480, title = "GLFW Window", monitor = None, share = None) -> None:
      self.window = None
      self.width = width
      self.height = height
      self.title = title
      self.monitor = monitor
      self.share = share
      self.framebuffer_size = None

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

   def _key_callback(self, window, key: int, scancode: int, action: int, mods: int):
      if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
         glfw.set_window_should_close(self.widow, glfw.TRUE)

   def _test_draw(self):
      vao = 0
      gl.glGenVertexArrays(1, vao)
      gl.glBindVertexArray(vao)

   def run_main_loop(self):
      while not glfw.window_should_close(self.window):       
         self.framebuffer_size = glfw.get_framebuffer_size(self.window)
         gl.glViewport(0, 0, self.width, self.height)
         gl.glClear(gl.GL_COLOR_BUFFER_BIT)

         # draw
         self._test_draw()
         # end draw

         glfw.swap_buffers(self.window)
         glfw.poll_events()

      glfw.terminate()
      exit(0)

window = Window_glfw()
window.setup_window()
window.run_main_loop()