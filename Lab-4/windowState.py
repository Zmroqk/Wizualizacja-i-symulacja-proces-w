import vectorOperations as vo

class WindowState:
    def __init__(self):
        self.currentRotation = 0.
        self.currentRotationType = vo.Rotation.OX
        self.currentColor = [1., 1., 1.]
        self.circleQuality = 20