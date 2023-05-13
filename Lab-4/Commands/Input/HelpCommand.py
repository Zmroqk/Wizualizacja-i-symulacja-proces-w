from windowState import WindowState
from Commands.Command import Command

class HelpCommand(Command):
   def __init__(self, state: WindowState):
      super().__init__(state)

   def execute(self):
      print("Manual")
      print("wsadqe - movement")
      print("uiojkl - rotation")
      print("exit")
      print("quality <n> - sets circle quality")
      print("rotation-quality <n> - sets rotation quality")
      print("color <r> <g> <b> - sets color")
      print("0, 9 - sets background color (from black to white)")
      print("cube <a> - creates cube")
      print("cuboid <a> <b> <c> - creates cuboid")
      print("circle <a> <bool> - a => length | bool => is2d")
      print("cylinder <r> <h> - r => radius | h => height")
      print("cone <r> <h> - r => radius | h => height")
      print("sphere <r> <ring> - r => radius | ring - number of rings")
      print("pyramid <d> <h> - d => side of the triangle | h - height of the triangle")