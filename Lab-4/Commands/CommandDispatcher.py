from windowState import WindowState
import glfw
import Commands

class CommandDispatcher():
   def __init__(self, state: WindowState) -> None:
      self._state = state
      self.currentCommand = None

   def dispatch(self, window, key: int, scancode: int, action: int, mods: int):
      if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
         glfw.set_window_should_close(window, glfw.TRUE)

      if self.currentCommand is None:
         if key in [glfw.KEY_A, glfw.KEY_D, glfw.KEY_W, glfw.KEY_S, glfw.KEY_Q, glfw.KEY_E]:
            Commands.MovementCommand(self._state, key).execute()
         if key in [glfw.KEY_U, glfw.KEY_I, glfw.KEY_O, glfw.KEY_J, glfw.KEY_K, glfw.KEY_L]:
            Commands.RotationCommand(self._state, key).execute()
         if key == glfw.KEY_SPACE:
            self.currentCommand = Commands.InputCommand(self._state)
      elif isinstance(self.currentCommand, Commands.InputCommand) and action == glfw.PRESS:
         if key == glfw.KEY_ENTER:
            self.currentCommand.execute()
            self.currentCommand = None
         else:
            self.currentCommand.appendText(key)
         
      