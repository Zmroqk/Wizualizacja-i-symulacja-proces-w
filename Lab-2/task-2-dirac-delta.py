import numpy as np
import matplotlib.pyplot as plot

D = 1
T = float(input("Provide T: "))
k = float(input("Provide k: "))

t = np.linspace(0, 10, 1000)

y = (k*D)/T * np.exp(-t/T)

_, ax = plot.subplots(figsize=(10, 5))


ax.plot(t, y)
ax.legend()
ax.set_xlabel('time')
ax.set_ylabel('???')

plot.show()
