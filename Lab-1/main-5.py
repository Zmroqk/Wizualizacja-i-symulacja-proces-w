import matplotlib.pyplot as plt
import numpy as np

startX = int(input('Provide starting x: '))
endX = int(input('Provide ending x: '))

x = np.linspace(startX, endX, 60) # Changed num from 10 to 60 to smooth sin(x)

_, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, x, color='black', label='y=x')
ax.plot(x, np.sin(x), label='y=sin(x)')
ax.plot(x, np.cos(x), label='y=cox(x)')
ax.plot(x, np.power(x, 3), label='y=x^3')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title("Wykres")
ax.legend()
plt.show()