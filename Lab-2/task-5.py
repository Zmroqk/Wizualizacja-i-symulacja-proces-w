import numpy as np
import matplotlib.pyplot as plot
import customMath as cm

m = float(input("Provide m: "))
b = float(input("Provide b: "))
k = float(input("Provide k: "))

# m = T0^2
T0 = np.sqrt(m)
# b = 2ET0
E = b/(2*T0)
W0 = 1/T0
D = E*W0

# if E < 0 or E >= 1:
#    exit()

t = np.linspace(0, 1000, 1000)

x0 = 5
v0 = 0

#y = k * (1 - ((np.exp(-E * W0 * t)/(np.sqrt(1 - E**2))) * np.sin(W0 * np.sqrt(1 - E**2) * t + np.arctan(np.sqrt(W0**2 - D**2)/D))))

Beta = b / 2 * m
W0 = np.sqrt(k / m)

rPlus = -Beta + np.sqrt(Beta**2 - W0**2)
rMinus = -Beta - np.sqrt(Beta**2 - W0**2)
A = x0 * (rPlus*x0 - v0) / (rMinus - rPlus)
B = -1 * (rPlus * x0 - v0) / (rMinus - rPlus)

x = A * np.exp(rPlus * t) + B * np.exp(rMinus * t)

_, ax = plot.subplots(figsize=(10, 5))

ax.plot(t, x)
ax.legend()
ax.set_xlabel('time')
ax.set_ylabel('???')

plot.show()
