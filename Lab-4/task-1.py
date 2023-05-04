from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np
import math as mt



side_number = int(input("Provide number of polygon sides (min 3 sides): "))
side_length = float(input("Provide length of the regular polygon's sides: "))


def show():
    angleIncrement = 360. / side_number
    angleIncrement *= np.pi / 180

    glBegin(GL_TRIANGLE_FAN)

    angle = 0.

    r = side_length / (2 * np.sin(side_length / 2))

    for _ in range(side_number):
        glVertex3f(r * np.cos(angle), np.sin(angle), 0.)
        angle += angleIncrement
    glEnd()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(800, 800)
glutInitWindowPosition(100, 100)
glutCreateWindow("Program 1")
glClearColor(1.0, 1.0, 1.0, 1.0)
glutDisplayFunc(show)
glutMainLoop()