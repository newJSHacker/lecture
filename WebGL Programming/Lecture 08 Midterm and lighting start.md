# Lecture 8 — Midterm and lighting start

**Course:** WebGL Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** midterm; Lambert in FS  
**Board first:** n·l in the fragment

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

1. Sit midterm on pipeline/buffers/shaders/textures.
2. Pass normals.
3. Lambert in FS.
4. normal matrix name.
5. Debug n as color.

---

## 1. Midterm

pipeline, attrib, uniform, depth, uv.

## 2. Lighting

CG I Lambert. Now per fragment.

## 3. Demo

06 phong cube.

## Live coding (60 min)

Lambert cube; light vector uniform.

---

## Lab

1. n as color.
2. two-sided extra.

---

## Homework

1. Written: VS vs FS lighting.
2. reflection.

---

## Quiz (10 min)

1. None.

## Snippet

```glsl
float d = max(0.0, dot(n, l));
```

---

## Common mistakes

- lighting in VS only and calling it Phong.

---

## Board drawings

1. n color.

