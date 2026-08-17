# Lecture 8 — Midterm and shadow research names

**Course:** Advanced Computer Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** midterm; VSM, CSM, PCSS  
**Board first:** moments; cascades; penumbra

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

1. Sit midterm: GI taxonomy, radiosity, path tracing, volumes, tiled lights.
2. VSM: mean + variance, Chebyshev.
3. CSM: split frustum.
4. PCSS name.
5. Don't implement all three.

---

## 1. Midterm

ideas + a tiny tracer or 2×2 radiosity.

## 2. Shadows beyond PCF

VSM light leak. CSM seams. PCSS blocker search.

## 3. Pick

Students write 1 page comparing two, implement none or one extra.

## Live coding (60 min)

Written compare VSM vs CSM vs PCSS (table). Optional tiny VSM extra.

---

## Lab

1. draw cascade splits.
2. light leak sketch.

---

## Homework

1. Midterm reflection + table.

---

## Quiz (10 min)

1. None.

## Snippet

```
Chebyshev: p = variance / (variance + (d-mean)^2)
```

---

## Common mistakes

- all three implemented badly.
- Nanite as a shadow method.

---

## Board drawings

1. Three columns.

