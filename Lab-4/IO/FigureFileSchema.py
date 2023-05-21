from typing import TypedDict, List

class FigureFileSchema(TypedDict):
   Vertices: List[List[float]]
   Colors: List[List[float]]
   LineVertices: List[List[float]]
   LineColor: List[float]
   Indices: List[float]