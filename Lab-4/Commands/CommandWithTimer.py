from windowState import WindowState
from threading import Timer
from abc import ABC, abstractmethod
from Commands.Command import Command

class CommandWithTimmer(Command):
   def __init__(self, state: WindowState):
      self._state = state
      self.timer: Timer = None
      self.canExecute = True

   @abstractmethod
   def execute(self):
      pass

   def stop(self):
      self.canExecute = False
      if self.timer is not None:
         self.timer.cancel()

   def _createTimer(self, method, interval = 0.1):
      if self.canExecute is True:
         self.timer = Timer(interval, method)
      self.timer.start()
       