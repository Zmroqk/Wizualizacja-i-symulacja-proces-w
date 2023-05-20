import yaml
import Figures
from windowState import WindowState

class ReadFigure:
   @staticmethod
   def readFigure(state : WindowState, path: str):
      print("Loading File...")
      with open(path, "r") as file:
         data = {}
         try:
            data = yaml.load(file, Loader=yaml.FullLoader)
         except OSError:
            print("Error during loading file")
         return Figures.CustomFigure(state, data['Vertices'], data['Colors'], data['LineVertices'], data['LineColor'], data['Indices'])
