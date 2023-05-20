from windowState import WindowState
from Commands.Command import Command

class CameraNearCommand(Command):
   def __init__(self, state: WindowState, *params):
      super().__init__(state)
      self.near = float(params[0])

   def execute(self):
      self._state.cameraNear = self.near