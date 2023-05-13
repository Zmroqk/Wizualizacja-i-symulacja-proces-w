import vectorOperations as vo

class WindowState:
    def __init__(self):
        self.currentRotationType = vo.Rotation.OX
        self.currentPosition = [0., 0., 0.]
        self.currentRotation = [0., 0., 0.]
        self.currentColor = [1., 1., 1.]
        self.circleQuality = 20
        self.rotationQuality = 100