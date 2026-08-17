# Lecture 7 — Inverse and systems

**Course:** Mathematics for Computer Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** 2×2 inverse, det  
**Board first:** det as area scale

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

1. Compute det 2×2.
2. Invert a rotation (transpose).
3. Invert a uniform scale.
4. Singular means det 0.
5. Solve 2×2 with inverse teaching-level.

---

## 1. Determinant

Area scale. Negative means flip (reflection / winding).

## 2. Inverse

Undo. Rotation inverse is transpose. If det=0, no inverse — collapsed geometry.

## 3. Normals preview

(M⁻¹)ᵀ in CG I. Name it; compute in 2D on a non-uniform scale.

## Live coding (60 min)

Scale non-uniform a square; show a wrong vs right normal.

---

## Lab

1. invert2 when det≠0.
2. Detect singular.

---

## Homework

1. Written: det 0 picture.
2. Code: tests.

---

## Quiz (10 min)

1. det of rotate (2)
2. inverse of Ry (4)
3. singular meaning (4)

## Snippet

```js
const det = a*d - b*c;
```

---

## Common mistakes

- Inverting by transposing a scale.
- Dividing by det 0.

---

## Board drawings

1. Area scale.
2. No inverse.

