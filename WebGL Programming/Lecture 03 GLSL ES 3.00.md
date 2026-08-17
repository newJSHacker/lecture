# Lecture 3 — GLSL ES 3.00

**Course:** WebGL Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** version, precision, in/out  
**Board first:** #version 300 es

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

1. #version 300 es first line.
2. precision highp float in FS.
3. in/out vs attribute/varying.
4. gl_Position.
5. out vec4 color.

---

## 1. Language

[[WebGL/11 Vertex and Fragment]].

## 2. Errors

Compile log is the teacher.

## 3. Types

vec3, mat4, sampler2D.

## Live coding (60 min)

Break a shader; read the log; fix.

---

## Lab

1. A second program (debug color).
2. precision extra.

---

## Homework

1. Written: WebGL1 vs 2 shader diffs.
2. Code: versioned pair.

---

## Quiz (10 min)

1. first line (3)
2. gl_FragColor in WebGL2? (4)
3. precision (3)

## Snippet

```glsl
#version 300 es
precision highp float;
out vec4 outColor;
```

---

## Common mistakes

- version after other lines.
- using texture2D in 300 es.

---

## Board drawings

1. Shader stages.

