import numpy as np
import matplotlib.pyplot as plot
import customMath as cm

k = float(input("Provide k: "))
T = float(input("Provide T: "))

t = np.linspace(0, 10, 1000)

y = k * (1 - np.exp(-t/T))
_, ax = plot.subplots(figsize=(10, 5))


ax.plot(t, y)
ax.legend()
ax.set_xlabel('time')
ax.set_ylabel('???')

plot.show()
