import math

import numpy as np
import matplotlib.pyplot as plot
import customMath as cm

D = 2
T = float(input("Provide T: "))
k = float(input("Provide k: "))


def y2(time):
   if time < D:
       return 0
   else:
       return -k * (1 - np.exp(-(time - D)/T)) * cm.strangeMathematicalFunction(time - D)


t = np.linspace(0, 10, 1000)

y1 = k * (1 - np.exp(-t/T))
y2Func = np.vectorize(y2)
y2Calculated = y2Func(t)

_, ax = plot.subplots(figsize=(10, 5))


ax.plot(t, y1 + y2Calculated)
ax.legend()
ax.set_xlabel('time')
ax.set_ylabel('???')

plot.show()
