import numpy as np
import matplotlib.pyplot as plot
import customMath as cm

h = float(input("Provide h: "))
k = float(input("Provide k: "))

n = np.linspace(0, 100, 101)

func = cm.diracDelta
values = []

# u(t) = sin(t)
def xplus2(n): # x** + x* + x
    if n == 0:
        values.append(k)
        return values[-1]
    elif n == 1:
        values.append(4.9)
        return values[-1]
    values.append(h**2*k*func(n*h)-(1-h)*values[-2]-(h-2)*values[-1])
    return values[-1]

_, ax = plot.subplots(figsize=(10, 5))

f = np.vectorize(xplus2)

y = f(n)
print(y)

ax.plot(n, y)
ax.legend()

plot.show()