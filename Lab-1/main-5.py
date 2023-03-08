import matplotlib.pyplot as plt
import numpy as np

startX = int(input('Provide starting x: '))
endX = int(input('Provide ending x: '))

x = np.linspace(startX, endX, 200)           # Changed num from 10 to 60 to smooth sin(x), Changed form 60 to 200 (depends on the x size)
_, ax = plt.subplots(figsize=(10, 5))

functions = {
                 'x':  (x, 'y=x'),
                 'x2': (x**2, 'y=x^2'),
                 'x3': (np.power(x, 3), 'y=x^3'),
                 'sin': (np.sin(x), 'y=sin(x)'),
                 'cos': (np.cos(x), 'y=cos(x)'),
             }
print('Pick functions to display, write them all using separetor' +
      '\nx -> y=x' +
      '\nx2 -> y=x^2' +
      '\nx3 -> y=x^3' +
      '\nsin -> y=sin(x)' +
      '\ncos -> y=cos(x)' +
      'example: x,x2,x3')
print()

picked_functions = str(input('Provide functions by delimeter: ')).split(',')

for fun in picked_functions:
    chart_color = str(input(f'Provide chart color for {fun} function: '))
    function, label = functions[fun]
    ax.plot(x, function, color=chart_color, label=label)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title("Wykres")
ax.legend()
plt.show()