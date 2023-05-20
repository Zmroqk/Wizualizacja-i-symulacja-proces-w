from windowState import WindowState
from Commands.Command import Command
from IO.ReadFigure import ReadFigure
import yaml

class ExportCommand(Command):
   def __init__(self, state: WindowState, *params):
      super().__init__(state)
      self.path = params[0]

   def execute(self):
      if self._state.currentFigure is not None:
         dict = self._state.currentFigure.export()
         with open(self.path, "w") as file:
            print(dict)
            yaml.dump(dict, file, default_flow_style=None)
            print("Exported succesfully")