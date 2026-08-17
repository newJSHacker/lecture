# Lecture 9 — Search

**Course:** Introduction to Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** linear vs binary  
**Board first:** sorted row of numbers, mid probe

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

1. Implement linear search.
2. Implement binary search on a sorted array.
3. State the sorted precondition.
4. Count comparisons.
5. Give Θ(n) vs Θ(log n) at teaching level.

---

## 1. Linear search

Scan until found. Always correct. Slow for large n.

## 2. Binary search

Needs sorted input. Mid index, shrink left or right. Off-by-one in `hi` is the classic bug.

## 3. Why graphics people care

Picking, BVH, and kd-trees (computational geometry) are search. Binary search is the warmup.

## Live coding (60 min)

Both searches on the same array; log comparison counts.

---

## Lab

1. Binary search tests: found, missing, empty, one element.
2. Plant an unsorted array and show binary fail.

---

## Homework

1. Written: 1 page why sorted is required.
2. Code: recursive binary extra.

---

## Quiz (10 min)

1. Precondition of binary search (3)
2. Comparisons worst case linear (3)
3. Mid formula (4)

## Snippet

```js
while (lo <= hi) { const mid = (lo + hi) >> 1; /* ... */ }
```

---

## Common mistakes

- Binary on unsorted data.
- `mid = (lo+hi)/2` floats.

---

## Board drawings

1. Probe picture.
2. Count table.

