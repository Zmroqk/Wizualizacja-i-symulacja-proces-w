import numpy as np
import matplotlib.pyplot as plot

H = int(input("Provide H: "))
x0 = float(input("Provide x0: "))
y0 = float(input("Provide y0: "))
r = float(input("Provide r: "))
h = float(input("Provide h: "))
T = 1

#vt = input("Provide v(t): ").split(',')
#pt = input("Provide p(t): ").split(',')

vt = [-1, -3, -5, 10, -3, -5, -1, 10, -5, -4]
pt = [40, 40, 50, 50, 40, 40, 50, 40, 50, 60]

xValues = []
yValues = []


def xt(n):
    if n == 0:
        xValues.append(x0)
        return x0
    xValues.append((T*r-1) * xValues[-1] - T * h * yValues[int(n)] - T * float(vt[int(n)]) * float(pt[int(n)]))
    return xValues[-1]


def yt(n):
    if n == 0:
        yValues.append(y0)
        return y0
    yValues.append(yValues[-1] + T * float(vt[int(n)]))
    return yValues[-1]


funX = np.vectorize(xt)
funY = np.vectorize(yt)

N = np.linspace(0, H-1, H)

Y = funY(N)
X = funX(N)
print(Y)
print(X)
funToFloat = np.vectorize(lambda x: float(x))
VT = funToFloat(vt)
PT = funToFloat(pt)

_, ax = plot.subplots(figsize=(6, 6))
_, ax2 = plot.subplots(figsize=(6, 6))

ax.plot(N, Y, label="y(t)")
ax2.plot(N, X, label="x(t)")
ax.plot(N, VT, label="v(t)")
ax2.plot(N, PT, label="p(t)")
ax.legend()
ax2.legend()
plot.show()
