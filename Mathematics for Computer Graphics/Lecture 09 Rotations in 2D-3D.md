# Lecture 9 — Rotations in 2D/3D

**Course:** Mathematics for Computer Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** Ry, composition  
**Board first:** right-hand thumb on axis

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

1. Write R2(θ).
2. Compose two rotations.
3. Euler angles as a warning.
4. Axis-angle name.
5. Match CG I Ry convention.

---

## 1. 2D

[[c,-s],[s,c]] or the course's documented variant — **write one and freeze**.

## 2. 3D

Rx, Ry, Rz. Order matters. Euler gimbal lock: name and a picture; quaternions named, not required.

## 3. Convention

Same Ry as [[Computer Graphics/Lecture 05 Homogeneous Transforms]].

## Live coding (60 min)

Rotate a cube wireframe with Ry from CG I kernel if available, or 2D square.

---

## Lab

1. Ry(90)*(1,0,0) test.
2. Two Euler orders compared.

---

## Homework

1. Written: gimbal lock in 6 sentences.
2. Code: rotateZ.

---

## Quiz (10 min)

1. R(90) of (1,0) (3)
2. why order matters (4)
3. gimbal lock name (3)

## Snippet

```js
// use the same Ry as Computer Graphics/code/kernel.js
```

---

## Common mistakes

- Mixing conventions.
- Degrees in matrices.

---

## Board drawings

1. Thumb.
2. Euler vs matrix.

