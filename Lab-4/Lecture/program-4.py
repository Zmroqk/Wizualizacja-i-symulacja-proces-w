from OpenGL.GLUT import *
from OpenGL.GL import *

# viewport - The viewport as specified by glViewport is just the rectangle in pixels on the screen that you wish to render to

def show():
    glClear(GL_COLOR_BUFFER_BIT)
    glViewport(320, 240, 320, 240)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.5, 0)
    glVertex2f(0.5, 0)
    glVertex2f(0, 0.5)
    glEnd()
    glViewport(0, 0, 320, 240)
    glColor4f(0.0, 1.0, 0.0, 0.5)
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
glutCreateWindow("Program 04")
glClearColor(1.0, 1.0, 1.0, 1.0)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glEnable(GL_BLEND)
glutDisplayFunc(show)
glutMainLoop()