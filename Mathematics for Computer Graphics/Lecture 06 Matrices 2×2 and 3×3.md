# Lecture 6 — Matrices 2×2 and 3×3

**Course:** Mathematics for Computer Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** multiply, identity  
**Board first:** rows × columns

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

1. Multiply 2×2 by hand.
2. Identity.
3. Linear maps: rotate/scale.
4. Column vectors in this program.
5. Not commutative.

---

## 1. What a matrix is

A linear function. Columns are where basis vectors go.

## 2. Multiply

Composition. AB ≠ BA. Same story as CG I T R vs R T.

## 3. Code

Write mul2 later as nested loops; this week by hand and a tiny function.

## Live coding (60 min)

Apply a 2×2 to a square's four corners; draw before/after.

---

## Lab

1. mat2 mul tests.
2. Scale then rotate vs reverse.

---

## Homework

1. Written: columns as images of basis.
2. Code: mul2.

---

## Quiz (10 min)

1. I times A (2)
2. AB vs BA (4)
3. 2×2 rotate 90 of (1,0) (4)

## Snippet

```js
function mul2(A,B){ /* 2×2 */ }
```

---

## Common mistakes

- Row-vector formulas mixed.
- Commuting blindly.

---

## Board drawings

1. Basis images.
2. Non-commute.

