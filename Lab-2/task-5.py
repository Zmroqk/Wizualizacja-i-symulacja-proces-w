import matplotlib.pyplot as plt
import numpy as np

m = float(input("Provide m: "))
b = float(input("Provide b: "))
k = float(input("Provide k: "))
F = float(input("Provide force: "))

# F = mx + bx + kx
# m*(d^2x/dt^2) + b*(dx/dt) + kx = 0
# x(t) = A0 * e^(-b*t/2m) * cos(wt + q)
# w = sqrt((k/m) - (b/2m)^2)
# x(t) = A0 * e^(-b*t/2m) * cos(sqrt((k/m) - (b/2m)^2) * t)

def delta(b, m, k):
   return np.sqrt(np.power(b, 2) - 4 * m * k)

def s1(b, m, k):
   return (-b - delta(b, m, k))/(2 * m)

def s2(b, m, k):
   return (-b + delta(b, m, k))/(2 * m)

def A(F, b, m, k):
   return F/(m * s1(b, m, k) * s2(b, m, k))

def B(F, b, m, k):
   return F/(m * (np.power(s1(b, m, k), 2) - s1(b, m, k) * s2(b, m, k)))

def C(F, b, m, k):
   return F/(m * (np.power(s2(b, m, k), 2) - s1(b, m, k) * s2(b, m, k)))

t = np.linspace(0, 100, 1000)

y = A(F, b, m, k) + B(F, b, m, k) * np.exp(s1(b, m, k) * t) + C(F, b, m, k) * np.exp(s2(b, m, k) * t)

_, ax = plt.subplots(figsize=(10,5))
ax.plot(t, y, color='blue', label='y=x(t)')

ax.set_xlabel("time(seconds)")
ax.set_ylabel("position(m)")
ax.set_title("Spring Position")
ax.legend()
plt.show()
