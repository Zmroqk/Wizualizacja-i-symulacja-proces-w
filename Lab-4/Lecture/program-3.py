from OpenGL.GLUT import *
from OpenGL.GL import *

# Blending

def show():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor4f(1.0, 0.0, 0.0,1.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.5, 0)
    glVertex2f(0.5, 0)
    glVertex2f(0, 0.5)
    glEnd()
    glColor4f(0.0, 1.0, 0.0, 0.5)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.3, -0.3)
    glVertex2f(0.3, -0.3)
    glVertex2f(0, 0.3)
    glEnd()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(640, 480)
glutInitWindowPosition(100, 100)
glutCreateWindow("Program 03")
glClearColor(1.0, 1.0, 1.0, 1.0)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glEnable(GL_BLEND)
glutDisplayFunc(show)
glutMainLoop()