# Lecture 1 — The shader as a program

**Course:** Shader Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** VS/FS, varyings  
**Board first:** vertex → interpolate → fragment

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 10 | Quiz from last week (Week 1: course contract) |
| 25 | Core definition and one picture |
| 45 | Worked examples / derivation |
| 65 | Live pitfalls and policy |
| 75 | Preview lab, then stand up for live coding |

---

## Learning goals

1. Write a vertex shader that passes a varying.
2. Write a fragment shader that uses it.
3. State clip-space gl_Position.
4. Not to treat Shadertoy as the only home.
5. Course contract: GLSL ES 3.00.

---

## 1. Two homes

Mesh shaders live in [[17 WebGL Programming]]. Fullscreen procedural live in Shadertoy-style `mainImage(out vec4, in vec2)` — [[WebGL/shadertoy/index.html]]. This course uses both.

## 2. Interpolation

VS outputs are interpolated. That is why a color at three vertices becomes a gradient. Normals must be renormalized in the FS.

## 3. Precision

`precision highp float` in ES fragment shaders. Desktop GLSL is looser — do not copy Shadertoy 1:1 into WebGL without version and precision.

## Live coding (60 min)

WebGL2: pass v_uv and display as color. Then the same idea in a fullscreen triangle.

---

## Lab

1. Break interpolation: output a step function in VS vs FS.
2. Read compile logs.

---

## Homework

1. Written: varying vs uniform.
2. Code: uv-as-color.

---

## Quiz (10 min)

1. who interpolates (4)
2. gl_Position space (3)
3. precision (3)

## Snippet

```glsl
#version 300 es
precision highp float;
in vec2 v_uv;
out vec4 c;
void main(){ c = vec4(v_uv, 0.0, 1.0); }
```

## Extra exercises

Walk [[WebGL/demos/08-uv-debug.html]] and [[WebGL/11 Vertex and Fragment]].
1. Draw the VS→FS dataflow.
2. Convert a Shadertoy header to WebGL2.
3. Quiz: what is a uniform this week vs a varying?

---

## Common mistakes

- Shadertoy copy-paste into WebGL without #version.
- Normalizing in VS only.

---

## Board drawings

1. Pipeline.
2. Varying arrows.

