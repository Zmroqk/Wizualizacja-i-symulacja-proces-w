from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np

# Shaders

vsc = """
attribute vec3 position;
void main() {
    gl_Position = vec4(position, 1.0);
}     """

fsc = """
void main() {
    gl_FragColor = vec4(0.5, 0.5, 0.5, 1.0);
}     """
prog = None

def doShaders():
    global prog
    prog = glCreateProgram()
    
    vshader = glCreateShader(GL_VERTEX_SHADER)
    glShaderSource(vshader, vsc)
    glCompileShader(vshader)
    
    if not glGetShaderiv(vshader, GL_COMPILE_STATUS):
        print("v:" + str(glGetShaderInfoLog(vshader).decode()))
    
    fshader = glCreateShader(GL_FRAGMENT_SHADER)
    glShaderSource(fshader, fsc)
    glCompileShader(fshader)
    
    if not glGetShaderiv(fshader, GL_COMPILE_STATUS):
        print("f:" + str(glGetShaderInfoLog(fshader).decode()))

    glAttachShader(prog, vshader)
    glAttachShader(prog, fshader)
    glLinkProgram(prog)
    
    if not glGetProgramiv(prog, GL_LINK_STATUS):
        print("p:" + str(glGetProgramInfoLog(prog)))
    glUseProgram(prog)
    glDetachShader(prog, vshader)
    glDetachShader(prog, fshader)

def doPrerender():
    global prog
    verts = np.zeros(3, [("position", np.float32, 3)])
    verts['position'] = [(-1, -1, 0), (1, -1, 0), (1, 1, 0)]
    buf = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, buf)
    glBufferData(GL_ARRAY_BUFFER, verts.nbytes, verts,
    GL_STATIC_DRAW)
    width = verts.strides[0]
    offset = ctypes.c_void_p(0)
    position = glGetAttribLocation(prog, "position")
    glEnableVertexAttribArray(position)
    glBindBuffer(GL_ARRAY_BUFFER, buf)
    glVertexAttribPointer(position, 3, GL_FLOAT, False, width,
    offset)

def show():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glutSwapBuffers()
    
def reshape(w, h):
    glViewport(0, 0, w, h)

def keyboard(k, x, y):
    glutLeaveMainLoop()


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_DOUBLE)
glutInitWindowSize(640, 480)
glutInitWindowPosition(100, 100)
glutCreateWindow("Program 11")
glClearColor(1.0, 1.0, 1.0, 1.0)

glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LESS)

glutDisplayFunc(show)
glutIdleFunc(show)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)

doShaders()
doPrerender()

glutMainLoop()