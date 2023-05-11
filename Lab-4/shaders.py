vsc = """#version 330 core
layout(location = 0) in vec3 vertexPosition_modelspace;
layout(location = 1) in vec3 color;

out vec3 fragmentColor;

void main() {
   gl_Position.xyz = vertexPosition_modelspace;
   gl_Position.w = 1.0;
   fragmentColor = color;
}
"""

fsc = """#version 330 core
in vec3 fragmentColor;
out vec3 color;
void main(){
   color = fragmentColor;
}   
"""