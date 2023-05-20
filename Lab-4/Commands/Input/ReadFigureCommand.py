from windowState import WindowState
from Commands.Command import Command
from IO.ReadFigure import ReadFigure

class ReadFigureCommand(Command):
   def __init__(self, state: WindowState, *params):
      super().__init__(state)
      self.path = params[0]

   def execute(self):
      customFigure = ReadFigure.readFigure(self._state, self.path)
      self._state.figures[customFigure.id] = customFigure
      customFigure.setup()
      print("Loaded file succesfully")