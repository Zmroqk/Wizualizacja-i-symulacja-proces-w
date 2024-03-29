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

def rotateAll(vec, angles):
   vec = rotateX(vec, angles[0])
   vec = rotateY(vec, angles[1])
   return rotateZ(vec, angles[2])

class Rotation(Enum):
   OX = 1
   OY = 2
   OZ = 3

def applyPosition(vecArray: List[List[float]], x: float, y: float, z: float) -> List[List[float]] :
   def add(vec, x, y, z):
      return [vec[0] + x, vec[1] + y, vec[2] + z]
   return list(map(lambda vec: add(vec, x, y, z), vecArray))

def applyRotationAll(vecArray: List[List[float]], angles) -> List[List[float]] :
   return list(map(lambda vec: rotateAll(vec, angles), vecArray))

def applyRotation(vecArray: List[List[float]], angle, rotation: Rotation) -> List[List[float]] :
   rotationFunc = None
   if rotation == Rotation.OX:
      rotationFunc = rotateX
   elif rotation == Rotation.OY:
      rotationFunc = rotateY
   else:
      rotationFunc = rotateZ
   return list(map(lambda vec: rotationFunc(vec, angle), vecArray))

def applyRotationSingle(vec: List[float], angle, rotation: Rotation) -> List[float] :
   rotationFunc = None
   if rotation == Rotation.OX:
      rotationFunc = rotateX
   elif rotation == Rotation.OY:
      rotationFunc = rotateY
   else:
      rotationFunc = rotateZ
   return list(rotationFunc(vec, angle))

def createPositionMatrix(vec: List[float]):
   return np.matrix([
      [1, 0, 0, vec[0]],
      [0, 1, 0, vec[1]],
      [0, 0, 1, vec[2]],
      [0, 0, 0, 1]
   ], dtype=np.float32)