# Extra exercises — Week 01 (The shader as a program)

Lecture: [[Shader Programming/Lecture 01 The shader as a program]]

## Written and coding

Walk [[WebGL/demos/08-uv-debug.html]] and [[WebGL/11 Vertex and Fragment]].
1. Draw the VS→FS dataflow.
2. Convert a Shadertoy header to WebGL2.
3. Quiz: what is a uniform this week vs a varying?

## Snippet

```glsl
#version 300 es
precision highp float;
in vec2 v_uv;
out vec4 c;
void main(){ c = vec4(v_uv, 0.0, 1.0); }
```
