import numpy as np
import matplotlib.pyplot as plot

T = 5730
m = float(input("Provide m: "))
k = -0.000121
t = np.linspace(0, 50000, 100)

# e^kt = r ^ (t/T)
# kt = t/T ln r
# k = 1/T ln r
# n(t) = n(0) e^kt = n(0) e^(t * ln r)/T
# where r = 1/2

# y = m * np.exp(t/T * np.log(0.5))
y = m * np.exp(k*t)
_, ax = plot.subplots(figsize=(10, 5))

ax.plot(t, y)
ax.legend()
ax.set_xlabel('years')
ax.set_ylabel('weight')

plot.show()
