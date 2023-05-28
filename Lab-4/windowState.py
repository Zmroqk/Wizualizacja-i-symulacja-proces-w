import vectorOperations as vo
import typing
import camera

class WindowState:
   def __init__(self):
      self.currentRotationType = vo.Rotation.OX
      self.currentColor = [1., 1., 1.]
      self.currentLineColor = [0., 0., 0.]
      self.circleQuality = 20
      self.rotationQuality = 100
      self.cameraDistance = 2
      self.cameraXRotation = 0
      self.cameraZRotation = 0
      self.cameraNear = 1
      self.cameraFar = 10
      self.cameraTarget = [0, 0, 1]
      import Figures
      self.currentFigure : Figures.Figure = None
      self.figures : typing.Dict[int, Figures.Figure] = {}
      self.currentCamera = camera.CameraType.Perspective

   