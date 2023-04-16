import numpy as np


def diracDelta(time):
    if(time == 0):
        return np.inf
    else:
        return 0

def identityFunction(time):
    if(time < 0):
        return 0
    else:
        return 1