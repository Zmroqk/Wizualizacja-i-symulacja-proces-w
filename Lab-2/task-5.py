import matplotlib.pyplot as plt
import numpy as np

m = float(input("Provide m: "))
b = float(input("Provide b: "))
k = float(input("Provide k: "))
A0 = float(input("Provide starting spring pos: "))

# F = mx + bx + kx
# m*(d^2x/dt^2) + b*(dx/dt) + kx = 0
# x(t) = A0 * e^(-b*t/2m) * cos(wt + q)
# w = sqrt((k/m) - (b/2m)^2)
# x(t) = A0 * e^(-b*t/2m) * cos(sqrt((k/m) - (b/2m)^2) * t)

def spring_position(time):
    return A0 * np.power(np.e, (-b * time) / (2 * m)) * np.cos(np.sqrt((k / m) - (b / (2 * m))**2) * time)

t = np.linspace(0, 100, 1000)

_, ax = plt.subplots(figsize=(10,5))
ax.plot(t, spring_position(t), color='blue', label='y=x(t)')

ax.set_xlabel("time(seconds)")
ax.set_ylabel("position(m)")
ax.set_title("Spring Position")
ax.legend()
plt.show()
