from abc import ABC, abstractmethod
from windowState import WindowState

class Command(ABC):
   def __init__(self, state: WindowState):
      self._state = state

   @abstractmethod
   def execute(self):
      pass
   