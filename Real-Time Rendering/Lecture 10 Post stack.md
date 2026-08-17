# Lecture 10 — Post stack

**Course:** Real-Time Rendering  
**Time:** 75 min lecture + 60 min live coding  
**This week:** order of operations  
**Board first:** hdr → shadowed shade → bloom → tonemap → lut

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

1. Write a stack order.
2. Color LUT name.
3. DoF/motion blur names.
4. Don't randomize order each frame.
5. Document the graph.

---

## 1. Order matters

Bloom on HDR. Tonemap before 8-bit. Grain after. LUT last or before grain — pick.

## 2. Look dev

A product shot is a stack, not one shader.

## 3. Kill switches

Each pass toggles for grading and for perf.

## Live coding (60 min)

Three toggles: bloom, grain, vignette; freeze order in README.

---

## Lab

1. one LUT extra (tiny 16³ or 2D strip).
2. screenshot matrix.

---

## Homework

1. Written: your order and why.
2. graph figure.

---

## Quiz (10 min)

1. tonemap vs bloom order (4)
2. LUT (3)
3. kill switch (3)

## Snippet

```
shade(HDR) → bloom → tonemap → sRGB → grain
```

---

## Common mistakes

- eight Instagram filters as 'RTR'.
- undocumented order.

---

## Board drawings

1. Graph.

