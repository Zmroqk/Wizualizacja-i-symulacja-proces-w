import numpy as np
import matplotlib.pyplot as plot
import customMath as cm

h = float(input("Provide h: "))
k = float(input("Provide k: "))

n = np.linspace(0, 100, 1000)

func = np.sin
values = list()

# u(t) = sin(t)
def xplus2(n): # x** + x* + x
    if n == 0:
        values.append(0.)
        return values[-1]
    elif n == 1:
        values.append(np.sin(1))
        return values[-1]
    values.append(h**2*k*func(n*h)-(h**2-h+1)*values[-2]-(h-2)*values[-1])
    return values[-1]

_, ax = plot.subplots(figsize=(10, 5))

f = np.vectorize(xplus2)

y = f(n)
print(y)

ax.plot(n, y)
ax.legend()

plot.show()