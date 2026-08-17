# Lecture 10 — Multiple objects

**Course:** WebGL Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** scene loop, many uniforms  
**Board first:** for each mesh: bind, uniform M, draw

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

1. A mesh record.
2. Loop draws.
3. Share program.
4. Don't compile shaders per object.
5. Simple scene graph extra.

---

## 1. CPU loop

Three.js Object3D is this with more.

## 2. State

bind VAO/buffer, set M, drawArrays/elements.

## 3. Demo

14 instancing later; this week naive loop.

## Live coding (60 min)

Three cubes different M.

---

## Lab

1. parented second cube extra.
2. shared geometry.

---

## Homework

1. Written: why one program.
2. Code: loop.

---

## Quiz (10 min)

1. what changes per object (4)
2. compile per mesh? (3)
3. VAO name (3)

## Snippet

```js
for (const o of objects) { setM(o.m); gl.drawElements(...); }
```

---

## Common mistakes

- new program per cube.
- leaking binds.

---

## Board drawings

1. Loop.

