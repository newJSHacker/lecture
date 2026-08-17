# Lecture 5 — A cube and depth

**Course:** WebGL Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** indices, DEPTH_TEST, cull  
**Board first:** enable DEPTH_TEST

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

1. Indexed cube.
2. enable depth.
3. clear depth.
4. cull CCW.
5. Near/far from CG I.

---

## 1. Hidden surfaces

Same as CG I z-buffer. Now the GPU.

## 2. Winding

CCW front. Inside-out = winding or mirrored scale.

## 3. Demo

04 cube, conventions.

## Live coding (60 min)

Cube with depth; toggle depth to show painter bugs.

---

## Lab

1. cull toggle.
2. wireframe extra.

---

## Homework

1. Written: GPU depth vs CPU z-buffer.
2. Code: cube.

---

## Quiz (10 min)

1. DEPTH_TEST (3)
2. CCW (3)
3. clear depth (4)

## Snippet

```js
gl.enable(gl.DEPTH_TEST);
gl.enable(gl.CULL_FACE);
```

---

## Common mistakes

- no depth clear.
- near=0.

---

## Board drawings

1. Cube.
2. cull.

