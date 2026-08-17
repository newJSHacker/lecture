# Lecture 13 — Polish and performance

**Course:** Interactive Web Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** pooling, culling 2D  
**Board first:** offscreen skip

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

1. Skip draw if off canvas.
2. Object pool name.
3. Measure fps.
4. Reduce overdraw.
5. Profiler.

---

## 1. Culling

AABB vs canvas. CG geometry AABB.

## 2. Pooling

Reuse particles.

## 3. Measure

performance.now frames.

## Live coding (60 min)

1000 particles: naive vs skip-offscreen.

---

## Lab

1. pool extra.
2. fps readout.

---

## Homework

1. Written: when to pool.
2. Code: cull.

---

## Quiz (10 min)

1. offscreen skip (4)
2. pool (3)
3. overdraw (3)

## Snippet

```js
if (x < -r || x > w + r) return;
```

---

## Common mistakes

- pooling without measuring.
- invented fps.

---

## Board drawings

1. Cull.

