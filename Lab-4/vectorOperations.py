import numpy as np
from enum import Enum
from typing import List

def rotateX(vec, angle):
   return [
      vec[0]
      , vec[1] * np.cos(angle) - vec[2] * np.sin(angle)
      , vec[1] * np.sin(angle) + vec[2] * np.cos(angle)
   ]

def rotateY(vec, angle):
   return [
      vec[0] * np.cos(angle) + vec[2] * np.sin(angle)
      , vec[1]
      , - vec[0] * np.sin(angle) + vec[2] * np.cos(angle)
   ]

def rotateZ(vec, angle):
   return [
      vec[0] * np.cos(angle) - vec[1] * np.sin(angle)
      , vec[0] * np.sin(angle) + vec[1] * np.cos(angle)
      , vec[2]
   ]

class Rotation(Enum):
   OX = 1
   OY = 2
   OZ = 3

def applyRotation(vecArray: List[List[float]], angle, rotation: Rotation) -> List[List[float]] :
   rotationFunc = None
   if rotation == Rotation.OX:
      rotationFunc = rotateX
   elif rotation == Rotation.OY:
      rotationFunc = rotateY
   else:
      rotationFunc = rotateZ
   return list(map(lambda vec: rotationFunc(vec, angle), vecArray))

def applyRotationSingle(vec: List[float], angle, rotation: Rotation) -> List[List[float]] :
   rotationFunc = None
   if rotation == Rotation.OX:
      rotationFunc = rotateX
   elif rotation == Rotation.OY:
      rotationFunc = rotateY
   else:
      rotationFunc = rotateZ
   return list(rotationFunc(vec, angle))