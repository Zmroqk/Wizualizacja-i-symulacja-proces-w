from Commands.CommandWithTimer import CommandWithTimmer
from typing import List

class Singleton(object):
     def __new__(cls, *args, **kw):
         if not hasattr(cls, '_instance'):
             orig = super(Singleton, cls)
             cls._instance = orig.__new__(cls, *args, **kw)
         return cls._instance

class CommandsBuffer(Singleton):
   buffer : List[CommandWithTimmer] = []

   def registerCommand(self, command: CommandWithTimmer):
      self.buffer.append(command)
      command.execute()

   def unregisterCommand(self):
      command = self.buffer[0]
      command.stop()
      self.buffer = self.buffer[1:]