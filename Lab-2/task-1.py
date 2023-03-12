import numpy as np
import matplotlib.pyplot as plot

ul = float(input("Provide speed of left wheel (m/s): "))
ur = float(input("Provide speed of right wheel (m/s): "))
r = float(input("Provide track width (m): "))

rotationSpeed = (1/r) * (ur - ul)

def rotation(time):
   return rotationSpeed * time

x = np.linspace(0, 10)

_, ax = plot.subplots(figsize=(10, 5))

ax.plot(x, rotation(x))
ax.legend()
ax.set_xlabel('time')
ax.set_ylabel('rotation')

plot.show()
