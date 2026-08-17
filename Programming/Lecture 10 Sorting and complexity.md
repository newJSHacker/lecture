# Lecture 10 — Sorting and complexity

**Course:** Introduction to Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** selection sort; Θ  
**Board first:** n cards, selection sort trace

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

1. Run selection sort by hand.
2. Implement it.
3. Define Θ(n²) teaching-level.
4. Know that built-in sort exists.
5. Not to use built-in as the lab.

---

## 1. Selection sort

Find min, swap to front. Easy to see. n² comparisons.

## 2. Complexity

Count nested loops. 'Twice as long' vs 'four times' when n doubles. No Master theorem.

## 3. Engine sort

`array.sort((a,b)=>a-b)` exists. Lab is selection sort so they feel n². Later they may use built-in.

## Live coding (60 min)

Sort 12 numbers on the board then in code; count swaps.

---

## Lab

1. Selection sort + tests.
2. Time n=1000 vs n=2000 (measured, not invented).

---

## Homework

1. Written: why n².
2. Insertion sort extra optional.

---

## Quiz (10 min)

1. Selection sort idea (4)
2. If n doubles, n² time? (3)
3. Built-in sort allowed in project? (3)

## Snippet

```js
for (let i=0;i<n;i++){ let m=i; for(let j=i+1;j<n;j++) if(a[j]<a[m]) m=j; swap(a,i,m); }
```

---

## Common mistakes

- Calling sort in the lab.
- Invented timings.

---

## Board drawings

1. Trace 6 numbers.
2. n vs n² sketch.

