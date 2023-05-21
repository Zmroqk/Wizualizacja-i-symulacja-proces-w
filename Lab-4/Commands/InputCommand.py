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
      self.shiftMode = False

   def appendText(self, key: int):
      if key == glfw.KEY_LEFT_SHIFT:
         self.shiftMode = not self.shiftMode
         return
      addValue = 0
      if not self.shiftMode and 65 <= key <= 90:
         addValue = 32
      if key == glfw.KEY_BACKSPACE:
         self.commandText = self.commandText[:-1]
      else:
         self.commandText = self.commandText + chr(key + addValue)
      self.shiftMode = False
      os.system('cls' if os.name == 'nt' else 'clear')
      print("Command:", self.commandText)

   def execute(self):
      elems = self.commandText.split(' ')
      params = elems[1:]
      command = elems[0].upper()
      print('executing')

      if command == 'HELP':
         InputCommands.HelpCommand(self._state).execute()
      elif command.startswith('CUBE'):
         InputCommands.CubeCommand(self._state, *params).execute()
      elif command.startswith('CYLINDER'):
         InputCommands.CylinderCommand(self._state, *params).execute()
      elif command.startswith('CIRCLE-QUALITY'):
         InputCommands.CircleQualityCommand(self._state, *params).execute()
      elif command.startswith('CIRCLE'):
         InputCommands.CircleCommand(self._state, *params).execute()
      elif command.startswith('ROTATION-QUALITY'):
         InputCommands.RotationQualityCommand(self._state, *params).execute()
      elif command.startswith('CONE'):
         InputCommands.ConeCommand(self._state, *params).execute()
      elif command.startswith('CUBOID'):
         InputCommands.CuboidCommand(self._state, *params).execute()
      elif command.startswith('PYRAMID'):
         InputCommands.PyramidCommand(self._state, *params).execute()
      elif command.startswith('SPHERE'):
         InputCommands.SphereCommand(self._state, *params).execute()
      elif command.startswith('RESET'):
         InputCommands.ResetCommand(self._state).execute()
      elif command.startswith('COLOR'):
         InputCommands.ColorCommand(self._state, *params).execute()
      elif command.startswith('LINE-COLOR'):
         InputCommands.LineColorCommand(self._state, *params).execute()
      elif command.startswith('AUTOROTATION'):
         CommandsBuffer().registerCommand(InputCommands.AutorotationCommand(self._state, *params))
      elif command.startswith("DISABLE-AUTOROTATION"):
         CommandsBuffer().unregisterCommand()
      elif command.startswith('PRINT-FIGURES'):
         InputCommands.PrintFiguresCommand(self._state).execute()
      elif command.startswith('SET-CONTEXT'):
         InputCommands.ContextCommand(self._state, *params).execute()
      elif command.startswith('SET-CAMERA-NEAR'):
         InputCommands.CameraNearCommand(self._state, *params).execute()
      elif command.startswith('SET-CAMERA-FAR'):
         InputCommands.CameraFarCommand(self._state, *params).execute()
      elif command.startswith('READ-FIGURE'):
         InputCommands.ReadFigureCommand(self._state, *params).execute()
      elif command.startswith('EXPORT'):
         InputCommands.ExportCommand(self._state, *params).execute()
      elif command.startswith('CHANGE-CAMERA'):
         InputCommands.ChangeCameraCommand(self._state).execute()
      elif command.startswith('REMOVE'):
         InputCommands.RemoveCommand(self._state, *params).execute()
      