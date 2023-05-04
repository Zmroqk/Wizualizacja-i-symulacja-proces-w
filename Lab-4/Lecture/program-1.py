from OpenGL.GLUT import *

# Tworzenie okna

def show():
    pass

glutInit()
glutInitWindowSize(640, 480)
glutInitWindowPosition(100, 100)
glutCreateWindow("Program 01")
glutDisplayFunc(show)
glutMainLoop()