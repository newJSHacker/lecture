# Lecture 3 — Dot product

**Course:** Mathematics for Computer Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** projection, cosine  
**Board first:** two arrows, shadow of one on the other

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

1. Compute a·b.
2. Get cosθ from unit vectors.
3. Project b onto a.
4. See Lambert as n·l preview.
5. Know perpendicular means 0.

---

## 1. Algebra

a·b = ax bx + ay by (+ az bz). Also |a||b|cosθ.

## 2. Projection

proj_a b = (a·b / a·a) a. Lighting and collision use this.

## 3. Sign

Acute, obtuse, right. Back-face intuition.

## Live coding (60 min)

Slider θ; show dot and a numeric projection.

---

## Lab

1. project(b,a).
2. Reject a perpendicular pair.

---

## Homework

1. Written: Lambert one sentence.
2. Code: tests including 90°.

---

## Quiz (10 min)

1. dot of perpendicular (3)
2. cos of 0° (2)
3. projection formula (5)

## Snippet

```js
const d = a.x*b.x + a.y*b.y;
```

---

## Common mistakes

- Forgetting to unit-ize before using as cosine.
- 3D forgetting z.

---

## Board drawings

1. Projection.
2. Unit circle cos.

