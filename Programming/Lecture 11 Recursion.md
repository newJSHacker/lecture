# Lecture 11 — Recursion

**Course:** Introduction to Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** base case, stack  
**Board first:** factorial tree

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

1. Write a recursive factorial.
2. State a base case.
3. Trace a stack 4 frames.
4. Know recursion can replace some loops.
5. Avoid infinite recursion.

---

## 1. Base case first

If missing, stack overflow. Write it before the recursive call.

## 2. Graphics later

Scene graphs, kd-trees, closest-pair divide-and-conquer. Recursion is not optional in IGWT.

## 3. vs loop

Factorial as loop is finer. Recursion is for divide-and-conquer structure.

## Live coding (60 min)

factorial, then recursive sum of an array (slice or index).

---

## Lab

1. fibonacci naive + why it is slow (count calls).
2. flatten a nested array extra.

---

## Homework

1. Written: stack drawing for fact(4).
2. Code: binary search recursive.

---

## Quiz (10 min)

1. Base case of fact (2)
2. What happens with no base (3)
3. One IGWT later use (5)

## Snippet

```js
function fact(n){ if(n<=1) return 1; return n*fact(n-1); }
```

---

## Common mistakes

- No base case.
- Recursing on the same n.

---

## Board drawings

1. Stack frames.
2. Tree of fib.

