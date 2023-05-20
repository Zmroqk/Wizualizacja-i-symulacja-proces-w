from Commands.CommandWithTimer import CommandWithTimmer
from typing import List
from singleton import Singleton

class CommandsBuffer(Singleton):
   buffer : List[CommandWithTimmer] = []

   def registerCommand(self, command: CommandWithTimmer):
      self.buffer.append(command)
      command.execute()

   def unregisterCommand(self):
      command = self.buffer[0]
      command.stop()
      self.buffer = self.buffer[1:]