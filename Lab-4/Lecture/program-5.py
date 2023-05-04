from OpenGL.GLUT import *
from OpenGL.GL import *

def drawCube():
    p = [
            [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
            [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
        ]

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex(p[0])
    glVertex(p[1])
    glVertex(p[2])
    glVertex(p[0])
    glVertex(p[2])
    glVertex(p[3])
    glColor3f(0.0, 1.0, 0.0)
    glVertex(p[1])
    glVertex(p[5])
    glVertex(p[2])
    glVertex(p[2])
    glVertex(p[5])
    glVertex(p[6])
    glColor3f(0.0, 0.0, 1.0)
    glVertex(p[0])
    glVertex(p[4])
    glVertex(p[3])
    glVertex(p[3])
    glVertex(p[4])
    glVertex(p[7])
    glEnd()
    glutSwapBuffers()




glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(640, 480)
glutInitWindowPosition(100, 100)
glutCreateWindow("Program 05")
glClearColor(1.0, 1.0, 1.0, 1.0)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glScalef(0.5, 0.5, 0.5)
glRotate(1, 0, 0, 1)

glEnable(GL_BLEND)
glEnable(GL_DEPTH_TEST)
glutDisplayFunc(drawCube)
glutMainLoop()