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


def generate_position(n):
    x = x1_0
    y = x2_0
    z = x3_0
    xv = [x]
    yv = [y]
    zv = [z]
    for step in n:
        circular_velocity = w2
        linear_velocity = w1

        cir = constraints['cir']
        lin = constraints['lin']

        for constraint in cir:
            min_value, max_value, velocity_value = constraint
            if step >= min_value and step <= max_value:
                circular_velocity = velocity_value

        for constraint in lin:
            min_value, max_value, velocity_value = constraint
            if step >= min_value and step <= max_value:
                linear_velocity = velocity_value

        z = z + T * circular_velocity
        x = x + T * linear_velocity * np.cos(z)
        y = y + T * linear_velocity * np.sin(z)

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