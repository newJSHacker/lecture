# Lecture 1 — Coordinates and why math

**Course:** Mathematics for Computer Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** axes, points, units  
**Board first:** x right, y up on paper; canvas y down

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

1. Plot a point in 2D.
2. Distinguish canvas y vs math y.
3. Use radians in code.
4. Name the CG I space chain as preview.
5. Course contract.

---

## 1. Graphics is numbers

A cube is vertices. A camera is a matrix. This course is the algebra Computer Graphics I will spend on pictures.

## 2. Two y conventions

Mathematics: +y up. HTML Canvas: +y down. CG I flips in the viewport. Say it every time a plot appears.

## 3. Radians

`Math.cos` takes radians. 180° = π. Convert on the board, store radians in code.

## Live coding (60 min)

Plot 8 points on a canvas with y flipped; label axes.

---

## Lab

1. Convert 30°, 45°, 90° to radians in a table.
2. Distance between two points.

---

## Homework

1. Written: why radians.
2. Code: plot y=sin(x).

---

## Quiz (10 min)

1. π radians in degrees (2)
2. canvas y direction (4)
3. point vs pixel (4)

## Snippet

```js
const rad = deg * Math.PI / 180;
```

---

## Common mistakes

- Degrees in cos.
- Forgetting y-flip.

---

## Board drawings

1. Two y-axes.
2. Unit circle preview.

