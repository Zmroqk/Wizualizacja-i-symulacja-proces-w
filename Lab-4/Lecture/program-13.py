from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np
import math as mt

vsc = """
attribute vec3 pozycja;
attribute vec4 kolor;
varying vec4 frag_kolor;
void main() {
    gl_Position = vec4(pozycja, 1.0);
    frag_kolor = kolor;
}     """
fsc = """
varying vec4 frag_kolor;
void main() {
    gl_FragColor = frag_kolor;
}     """

prog = None
vao1 = None
vao2 = None

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
    global prog, vao1, vao2
    # KOŁO
    verts = np.zeros(14, [("poz", np.float32, 3),
        ("kol", np.float32, 4)])
    verts['poz'][0] = ((0, 0, 0))
    verts['kol'][0] = ((1, 0, 0, 1))
    for i in range(13):
        verts['poz'][i + 1] = ((0.5 * mt.cos(2 * mt.pi * i / 12),
        0.5 * mt.sin(2 * mt.pi * i / 12), -0.5))
        verts['kol'][i + 1] = ((0, 1, 0, 1))
    vao1 = glGenVertexArrays(1)
    glBindVertexArray(vao1)
    
    buf = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, buf)
    glBufferData(GL_ARRAY_BUFFER, verts.nbytes, verts,
        GL_STATIC_DRAW)
    
    width = verts.strides[0]
    offset = ctypes.c_void_p(0)
    position = glGetAttribLocation(prog, "pozycja")
    glEnableVertexAttribArray(position)
    glBindBuffer(GL_ARRAY_BUFFER, buf)
    glVertexAttribPointer(position, 3, GL_FLOAT, False, width,
    offset)
    offset = ctypes.c_void_p(verts.dtype["poz"].itemsize)
    color = glGetAttribLocation(prog, "kolor")
    glEnableVertexAttribArray(color)
    glBindBuffer(GL_ARRAY_BUFFER, buf)
    glVertexAttribPointer(color, 4, GL_FLOAT, False, width,
        offset)
    
    # KWADRAT
    vao2 = glGenVertexArrays(1)
    glBindVertexArray(vao2)
    verts = np.zeros(4, [("poz", np.float32, 3),
    ("kol", np.float32, 4)])
    verts['poz'] = [(-1, -1, 0), (1, -1, 0), (1, 1, 0),
    (-1, 1, 0)]
    verts['kol'] = [(0, 0, 1, 1), (0, 0, 1, 1),
    (0, 0, 1, 0), (0, 0, 1, 0)]
    buf = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, buf)
    glBufferData(GL_ARRAY_BUFFER, verts.nbytes, verts,
    GL_STATIC_DRAW)
    width = verts.strides[0]
    offset = ctypes.c_void_p(0)
    position = glGetAttribLocation(prog, "pozycja")
    glEnableVertexAttribArray(position)
    glBindBuffer(GL_ARRAY_BUFFER, buf)
    glVertexAttribPointer(position, 3, GL_FLOAT, False, width,
        offset)
    offset = ctypes.c_void_p(verts.dtype["poz"].itemsize)
    color = glGetAttribLocation(prog, "kolor")
    glEnableVertexAttribArray(color)
    glBindBuffer(GL_ARRAY_BUFFER, buf)
    glVertexAttribPointer(color, 4, GL_FLOAT, False, width,
    offset)
    inds = np.zeros(6, [("vals", np.int32)])
    inds["vals"] = [0, 1, 2, 0, 2, 3]
    ebo = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, inds.nbytes, inds,
    GL_STATIC_DRAW)
    glBindVertexArray(0)

def show():
    glClear(GL_COLOR_BUFFER_BIT)
    glBindVertexArray(vao2)
    glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, None)
    glBindVertexArray(vao1)
    glDrawArrays(GL_TRIANGLE_FAN, 0, 14)
    glutSwapBuffers()


def reshape(w, h):
    glViewport(0, 0, w, h)

def keyboard(k, x, y):
    glutLeaveMainLoop()


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_DOUBLE)
glutInitWindowSize(640, 480)
glutInitWindowPosition(100, 100)
glutCreateWindow("Program 13")
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