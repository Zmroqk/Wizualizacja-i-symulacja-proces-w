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

def show():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glViewport(0, 0, 640, 480)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Program 05a
    glFrustum(-2, 2, -2, 2, 1, 10)
    # Program 05b
    #glOrtho(-2, 2, -2, 2, 1, 10)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glPushMatrix()
    glTranslate(2, 0, -3)
    drawCube()
    glPopMatrix()
    glTranslate(-1 ,-2, -5)
    drawCube()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(640, 480)
glutInitWindowPosition(100, 100)
glutCreateWindow("Program 05a")
# glutCreateWindow("Program 05b")
glClearColor(1.0, 1.0, 1.0, 1.0)
glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LESS)
glutDisplayFunc(show)
glutMainLoop()