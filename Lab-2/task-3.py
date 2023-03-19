import numpy as np
import matplotlib.pyplot as plot
import customMath as cm

a = float(input("Provide a: "))
b = float(input("Provide b: "))
Ti = b
T = a/b

t = np.linspace(0, 10, 1000)

y = (1/Ti) * (t - T * (1 - np.exp(-t/T)))
_, ax = plot.subplots(figsize=(10, 5))


ax.plot(t, y)
ax.legend()
ax.set_xlabel('time')
ax.set_ylabel('???')

plot.show()
