# Lecture 2 — Vectors

**Course:** Mathematics for Computer Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** magnitude, add, scale  
**Board first:** arrow not a point

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

1. Add and scale vectors.
2. Compute length.
3. Subtract points to get a vector.
4. Refuse to add two points.
5. Draw a vector.

---

## 1. Point vs vector

A point is a location. A vector is a displacement. CG I Week 4 is this with 3D and w.

## 2. Operations

a+b parallelogram. s*a stretch. |a| = hypot.

## 3. Normalization

unit vector. Zero vector: do not divide.

## Live coding (60 min)

Interactive: two arrows add. Show the sum.

---

## Lab

1. vec2.js: add, sub, scale, len, normalize.
2. Tests including zero.

---

## Homework

1. Written: why p+q is meaningless.
2. Code: 8 tests.

---

## Quiz (10 min)

1. | (3,4) | (2)
2. unit of (0,2) (3)
3. p minus p (5)

## Snippet

```js
function len(a){ return Math.hypot(a.x, a.y); }
```

---

## Common mistakes

- Normalizing zero.
- Adding points.

---

## Board drawings

1. Parallelogram.
2. Unit arrow.

