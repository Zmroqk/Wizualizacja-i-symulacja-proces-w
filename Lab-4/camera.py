import numpy as np
from enum import Enum

class CameraType(Enum):
   Perspective = 0
   Ortographic = 1

def perspectiveCameraMatrix(near = 1, far = 10, left = -1, right = 1, bottom = -1, top = 1):
   return np.array([
      [2*near / (right - left), 0, (right + left) / (right - left), 0],
      [0, 2 * near / (top - bottom), (top + bottom) / (top - bottom), 0],
      [0, 0, -(far + near) / (far - near), -2 * far * near / (far - near)],
      [0, 0, -1, 0],
   ], dtype=np.float32)

def _setupCamera(mvp, rotX = 0, rotZ = 0, distance = 2):
   x = distance * np.sin(rotX)
   y = 0
   z = distance * np.cos(rotZ)
   xyz = np.array([x, y, z], dtype=np.float32)
   target = np.array([0, 0, 0], dtype = np.float32)
   direction = xyz - target
   direction = direction / np.linalg.norm(direction)
   up = np.array([0, 1, 0], dtype = np.float32)
   right = np.cross(direction, up) * -1
   up = np.cross(right, direction) * -1

   mvp2 = np.array([
      [1, 0, 0, -xyz[0]],
      [0, 1, 0, -xyz[1]],
      [0, 0, 1, -xyz[2]],
      [0, 0, 0, 1]
      ], dtype=np.float32
   )

   mvp3 = np.array([
      [right[0], right[1], right[2], 0],
      [up[0], up[1], up[2], 0],
      [direction[0], direction[1], direction[2], 0],
      [0, 0, 0, 1]
   ], dtype=np.float32)

   mvpmat = np.matmul(mvp3, mvp2)
   mvpmat = np.matmul(mvp, mvp2)
   return mvpmat.transpose()

def ortographicCameraMatrix(near = 1, far = 10, left = -1, right = 1, bottom = -1, top = 1):
   return np.array([
      [2 / (right - left), 0, 0, - (right + left) / (right - left)],
      [0, 2 / (top - bottom), 0, - (top + bottom) / (top - bottom)],
      [0, 0, -2 / (far - near), - (far + near) / (far - near)],
      [0, 0, 0, 1],
   ], dtype=np.float32)

def getCamera(cameraType: CameraType, distance = 2, rotX = 0, rotZ = 0, near = 1, far = 10):
   if cameraType == CameraType.Ortographic:
      return _setupCamera(ortographicCameraMatrix(near = near, far = far), distance = distance)
   else:
      return _setupCamera(perspectiveCameraMatrix(near = near, far = far), distance = distance, rotX = rotX, rotZ = rotZ)