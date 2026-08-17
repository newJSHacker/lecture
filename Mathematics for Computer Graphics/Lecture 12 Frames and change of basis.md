# Lecture 12 — Frames and change of basis

**Course:** Mathematics for Computer Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** origin + axes  
**Board first:** two frames, same point

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

1. Describe a frame.
2. Change of coordinates teaching-level.
3. Model matrix as a frame.
4. Orthonormal bases.
5. Right-handed three axes.

---

## 1. A frame is an origin and axes

Object space is a frame. World is a frame. Camera is a frame.

## 2. Columns of M

Where object x,y,z,origin go in world. CG I Week 6.

## 3. Orthonormal

dot 0, length 1. lookAt builds one.

## Live coding (60 min)

Draw a local frame on a rotated box; a world frame.

---

## Lab

1. Build orthonormal 2D from one vector + perp.
2. Tests.

---

## Homework

1. Written: M's columns.
2. Code: rotate a frame.

---

## Quiz (10 min)

1. what is a frame (3)
2. M columns (4)
3. orthonormal (3)

## Snippet

```js
// columns of M = object axes in world
```

---

## Common mistakes

- Scaling axes and still calling them orthonormal.

---

## Board drawings

1. Two frames.
2. Columns.

