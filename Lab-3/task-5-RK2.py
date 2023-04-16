import matplotlib.pyplot as plt
import numpy as np


T = float(input("T: "))
x1_0 = float(input("Provide x1_0: "))
x2_0 = float(input("Provide x2_0: "))
x3_0 = float(input("Provide x3_0: "))
w1 = float(input("Provide w1: "))   # prędkość liniowa
w2 = float(input("Provide w2: "))   # prędkość obrotowa

t = np.linspace(0, 100, 101)

constraints = {
    "lin": [],
    "cir": []
}

is_chosing = True
if input("complex linear or circular? y/n") == 'n':
    is_chosing = False


while(is_chosing):
    con = input("Provide which movement lin or cir, startT, maxT and the value - ex: lin,0.1,2,0.2: ").split(",")
    constraints[con[0]].append((float(con[1]), float(con[2]), float(con[3])))

    if input("Continue? y/n") == 'n':
        is_chosing = False


def get_linear_velocity(t):
    for constraint in constraints["lin"]:
        min_t, max_t, velocity = constraint
        if t >= min_t and t <= max_t:
            return velocity
    
    return w1

def get_circular_velocity(t):
    for constraint in constraints["cir"]:
        min_t, max_t, velocity = constraint
        if t >= min_t and t <= max_t:
            return velocity
    
    return w2

def next_x(t, x, z):
    k1 = ((x + T * get_linear_velocity(t) * np.cos(z)) - x)
    k2 = ((x * k1/2 + T * get_linear_velocity(t + T/2) * np.cos(z)) - x * k1/2)
    return x + (1/4 * k1 + 3/4 * k2)

def next_y(t, y, z):
    k1 = ((y + T * get_linear_velocity(t) * np.sin(z)) - y)
    k2 = ((y * k1/2 + T * get_linear_velocity(t + T/2) * np.sin(z)) - y * k1/2)
    return y + (1/4 * k1 + 3/4 * k2)

def next_z(t, z):
    k1 = ((z + T * get_circular_velocity(t)) - z)
    k2 = ((z * k1/2 + T * get_circular_velocity(t)) - z * k1/2)   # get_circular_velocity(T/2) ?
    return z + (1/4 * k1 + 3/4 * k2)

def generate_position(n):
    x = x1_0
    y = x2_0
    z = x3_0
    xv = [x]
    yv = [y]
    zv = [z]
    for step in n:

        z = next_z(step, z)
        x = next_x(step, x, z)
        y = next_y(step, y, z)

        xv.append(x)
        yv.append(y)
        zv.append(z)

    return (xv, yv, zv)


x, y, z = generate_position(t)

# _, ax = plt.scatter(figsize=(10,5))
plt.scatter(x, y, color='blue', label='y=x(t)')


# plt.set_xlabel("time(seconds)")
# plt.set_ylabel("position(m)")
# plt.set_title("Spring Position")
plt.legend()
plt.show()