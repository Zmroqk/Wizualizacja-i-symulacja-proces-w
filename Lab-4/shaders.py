vsc = """#version 330 core
layout(location = 0) in vec3 vertexPosition;
layout(location = 1) in vec3 color;
uniform mat4 position;
uniform vec3 rotation;

out vec3 fragmentColor;

mat4 rx(float kat) {
   return mat4(1.0, 0, 0, 0,
      0, cos(kat), -sin(kat), 0,
      0, sin(kat), cos(kat), 0,
      0, 0, 0, 1);
}

mat4 ry(float kat) {
   return mat4(cos(kat), 0, sin(kat), 0,
      0, 1.0, 0, 0,
      -sin(kat), 0, cos(kat), 0,
      0, 0, 0, 1.0);
}
mat4 rz(float kat) {
   return mat4(cos(kat), -sin(kat), 0, 0,
      sin(kat), cos(kat), 0, 0,
      0, 0, 1.0, 0,
      0, 0, 0, 1.0);
}

void main() {
   gl_Position = vec4(vertexPosition, 1.0) * rx(rotation.x) * ry(rotation.y) * rz(rotation.z) * position;
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