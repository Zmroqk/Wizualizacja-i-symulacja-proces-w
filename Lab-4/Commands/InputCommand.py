from Commands.Command import Command
from windowState import WindowState
import glfw
import os
import Commands.Input as InputCommands
from Commands.CommandsBuffer import CommandsBuffer

class InputCommand(Command):
   def __init__(self, state: WindowState):
      super().__init__(state)
      self.commandText = ""

   def appendText(self, key: int):
      if key == glfw.KEY_BACKSPACE:
         self.commandText = self.commandText[:-1]
      else:
         self.commandText = self.commandText + chr(key)
      os.system('cls' if os.name == 'nt' else 'clear')
      print("Command:", self.commandText)

   def execute(self):
      params = self.commandText.split(' ')[1:]
      print('executing')

      if self.commandText == 'HELP':
         InputCommands.HelpCommand(self._state).execute()
      elif self.commandText.startswith('CUBE'):
         InputCommands.CubeCommand(self._state, *params).execute()
      elif self.commandText.startswith('CYLINDER'):
         InputCommands.CylinderCommand(self._state, *params).execute()
      elif self.commandText.startswith('CIRCLE-QUALITY'):
         InputCommands.CircleQualityCommand(self._state, *params).execute()
      elif self.commandText.startswith('CIRCLE'):
         InputCommands.CircleCommand(self._state, *params).execute()
      elif self.commandText.startswith('ROTATION-QUALITY'):
         InputCommands.RotationQualityCommand(self._state, *params).execute()
      elif self.commandText.startswith('CONE'):
         InputCommands.ConeCommand(self._state, *params).execute()
      elif self.commandText.startswith('CUBOID'):
         InputCommands.CuboidCommand(self._state, *params).execute()
      elif self.commandText.startswith('PYRAMID'):
         InputCommands.PyramidCommand(self._state, *params).execute()
      elif self.commandText.startswith('SPHERE'):
         InputCommands.SphereCommand(self._state, *params).execute()
      elif self.commandText.startswith('RESET'):
         InputCommands.ResetCommand(self._state).execute()
      elif self.commandText.startswith('COLOR'):
         InputCommands.ColorCommand(self._state, *params).execute()
      elif self.commandText.startswith('LINE-COLOR'):
         InputCommands.LineColorCommand(self._state, *params).execute()
      elif self.commandText.startswith('AUTOROTATION'):
         CommandsBuffer().registerCommand(InputCommands.AutorotationCommand(self._state, *params))
      elif self.commandText.startswith("DISABLE-AUTOROTATION"):
         CommandsBuffer().unregisterCommand()
      