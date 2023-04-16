import numpy as np
import matplotlib.pyplot as plot
import customMath as cm

h = float(input("Provide h: "))
k = float(input("Provide k: "))

n = np.linspace(0, 100, 100)

values = list()

def xplus1(n): # x** + x* + x
    if n == 0:
        values.append(k)
        return values[-1]
    values.append(h * (0 - values[-1]) + values[-1])
    return values[-1]

_, ax = plot.subplots(figsize=(10, 5))

f = np.vectorize(xplus1)

y = f(n)
print(y)

ax.plot(n, y)
ax.legend()

plot.show()