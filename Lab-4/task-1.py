from OpenGL.GLUT import *
from OpenGL.GL import *
import numpy as np
import math as mt

side_number = ''
side_length = ''


while(not side_number.isnumeric()):
    side_number = input("Provide number of polygon sides (min 3 sides): ")

while(not side_length.isnumeric()):
    side_length = input("Provide length of the regular polygon's sides: ")
