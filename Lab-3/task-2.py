import numpy as np
import matplotlib.pyplot as plot
import customMath as cm

h = float(input("Provide h: "))
k = float(input("Provide k: "))

n = np.linspace(0, 100, 1000)

func = np.sin

# u(t) = sin(t)
def xplus2(n): # x** + x* + x
    return h**2*k*func(n*h)-(h**2-h+1)*func((n-1)*h)-(h-2)*func((n-2)*h)
def xplus2b(n): # x** + x*
    return h**2*k*func(n*h)-(1-h)*func((n-1)*h)-(h-2)*func((n-2)*h)

_, ax = plot.subplots(figsize=(10, 5))
_, ax2 = plot.subplots(figsize=(10, 5))

f = np.vectorize(xplus2)
fb = np.vectorize(xplus2b)

y = f(n)
y2 = fb(n)

ax.plot(n, y)
ax.legend()

ax2.plot(n, y2)
ax2.legend()

_, ax3 = plot.subplots(figsize=(10, 5))
_, ax4 = plot.subplots(figsize=(10, 5))

func = cm.diracDelta

y = f(n)
y2 = fb(n)

ax3.plot(n, y)
ax3.legend()

ax4.plot(n, y2)
ax4.legend()

plot.show()