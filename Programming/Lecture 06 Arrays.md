# Lecture 6 — Arrays

**Course:** Introduction to Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** push, map, index  
**Board first:** boxes 0..n-1

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

1. Index from 0.
2. Push/pop vs rewrite.
3. Loop with for-of and with index.
4. Not to use holes.
5. Copy with slice.

---

## 1. A list of values

Vertices will be arrays of points. Indices into a cube. Off-by-one here becomes a missing triangle later.

## 2. Mutation

push changes the array. `const a = []` can still push. Copy before sort if you need the original.

## 3. Higher-order preview

`arr.map` / `filter` names only. Required: for-loop. Optional: map for the homework extra.

## Live coding (60 min)

Average of an array; then find max index.

---

## Lab

1. Reverse a copy.
2. Remove duplicates with a nested loop (n small).

---

## Homework

1. Histogram of letters.
2. Written: index vs value.

---

## Quiz (10 min)

1. Index of last element (2)
2. push return value (2)
3. Copy vs alias (6)

## Snippet

```js
const b = a.slice();
```

---

## Common mistakes

- `a = a.push(x)`.
- Using map without understanding for.

---

## Board drawings

1. Array of vertices.
2. Alias vs copy.

