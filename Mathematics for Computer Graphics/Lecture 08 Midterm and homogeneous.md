# Lecture 8 — Midterm and homogeneous

**Course:** Mathematics for Computer Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** midterm; then w  
**Board first:** 3-vector (x,y,1)

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

1. Sit midterm on vectors/dot/cross/2×2.
2. Homogeneous point vs direction.
3. Translation as a matrix.
4. w=1 vs 0.
5. Preview 4×4.

---

## 1. Midterm

vec, dot, cross, mul2, det.

## 2. Homogeneous

Translation does not fit 2×2 linear. Add a 1. CG I Week 5 is the 4×4 version.

## 3. Directions

w=0 ignores translation. Lights-as-directions.

## Live coding (60 min)

3×3 2D affine: translate a triangle.

---

## Lab

1. T(1,0) * point.
2. T * direction unchanged.

---

## Homework

1. Written: why 3×3 for 2D affine.
2. Midterm reflection.

---

## Quiz (10 min)

1. None.

## Snippet

```js
// (x,y,1) point   (x,y,0) direction
```

---

## Common mistakes

- Translating normals as points.

---

## Board drawings

1. Homogeneous column.

