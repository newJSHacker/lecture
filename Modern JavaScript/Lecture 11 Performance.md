# Lecture 11 — Performance

**Course:** Modern JavaScript Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** measure, GC, hot loops  
**Board first:** performance.now()

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

1. Measure with performance.now().
2. Avoid allocating in hot loops.
3. Garbage collection name.
4. Don't optimize first.
5. n=1e6 array cost demo.

---

## 1. Measure

Invented timings forbidden. Same rule as CG reports.

## 2. Allocations

new objects per pixel is death. Reuse vecs in a renderer.

## 3. Big-O

From Programming week 10. Profiling tab name.

## Live coding (60 min)

Sum 1e7 numbers; compare push in loop vs prealloc.

---

## Lab

1. Don't ship a micro-opt without a number.
2. One GC-friendly rewrite.

---

## Homework

1. Written: when not to optimize.
2. Code: measured table.

---

## Quiz (10 min)

1. performance.now (3)
2. alloc in pixel loop (4)
3. prealloc (3)

## Snippet

```js
const t0 = performance.now();
```

---

## Common mistakes

- Optimizing unreadably without numbers.

---

## Board drawings

1. Timer.
2. Alloc vs reuse.

