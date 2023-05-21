from windowState import WindowState
from Commands.Command import Command

class RemoveCommand(Command):
   def __init__(self, state: WindowState, *params):
      super().__init__(state)
      self.removeId = int(params[0])
   def execute(self):
      self._state.figures.pop(self.removeId)