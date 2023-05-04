from OpenGL.GLUT import *
from OpenGL.GL import *

# Wyświetlenie trójkąta

def show():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.5, 0)
    glVertex2f(0.5, 0)
    glVertex2f(0, 0.5)
    glEnd()

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(640, 480)
glutInitWindowPosition(100, 100)
glutCreateWindow("Program 02")
glClearColor(1.0, 1.0, 1.0, 1.0)
glutDisplayFunc(show)
glutMainLoop()