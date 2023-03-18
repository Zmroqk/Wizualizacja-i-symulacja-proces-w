import math

import numpy as np
import matplotlib.pyplot as plot
import customMath as cm

m = float(input("Provide m: "))
b = float(input("Provide b: "))
k = float(input("Provide k: "))

def force(t):
    return k * (1 - (m/(m-b)) * np.exp(-t/m) + (b/(m-b)) * np.exp(-t/b)) * np.vectorize(cm.strangeMathematicalFunction)(t)

t = np.linspace(0, 1000, 1000)

_, ax = plot.subplots(figsize=(10, 5))

ax.plot(t, force(t))
ax.legend()
ax.set_xlabel('time')
ax.set_ylabel('???')

plot.show()
