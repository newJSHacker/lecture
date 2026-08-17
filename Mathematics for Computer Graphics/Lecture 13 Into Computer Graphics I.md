# Lecture 13 — Into Computer Graphics I

**Course:** Mathematics for Computer Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** PVM preview  
**Board first:** object→world→view→clip

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

1. Recite the space chain.
2. Where this course's math sits.
3. Homogeneous multiply chain.
4. What they will implement next semester.
5. Joint figure with CG I Week 1.

---

## 1. Map

Vectors, matrices, frames, lerp → renderer.

## 2. PVM

p' = P V M p. Do not derive P today.

## 3. Geometry course

orient and barycentric are this week's cross and areas.

## Live coding (60 min)

If CG I kernel exists, multiply PVM on one point and print clip. Else multiply 3×3 affine only.

---

## Lab

1. One-page map: math week → CG I week.
2. Three numerical PVM multiplies extra.

---

## Homework

1. Written: six spaces.
2. No new code required.

---

## Quiz (10 min)

1. six spaces (5)
2. w of a point (2)
3. which course implements z-buffer (3)

## Snippet

```
p_clip = P * V * M * p
```

---

## Common mistakes

- Claiming they already wrote a GPU.

---

## Board drawings

1. Pipeline.
2. Map table.

