# Lecture 4 — Loops

**Course:** Introduction to Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** for, while, off-by-one  
**Board first:** i from 0 to n-1

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

1. Write a for loop over 0..n-1.
2. Sum an array of numbers.
3. Avoid infinite loops.
4. Nest two loops for a grid.
5. State loop invariant in one sentence.

---

## 1. for is the default

`for (let i = 0; i < n; i++)` is the graphics loop over pixels and vertices. while is for unknown count.

## 2. Off-by-one

Fenceposts. Inclusive vs exclusive end. Draw 4 posts, 3 rails.

## 3. Nested loops

A checkerboard is nested loops. This is Week 2 of Computer Graphics I later. Do it in text first: print `#.` rows.

## Live coding (60 min)

Print a triangle of stars; then a 8×8 checkerboard in the console.

---

## Lab

1. Sum 1..100.
2. Prime checker (trial division) for n ≤ 200.

---

## Homework

1. FizzBuzz 1..100.
2. Written: invariant of the sum loop.

---

## Quiz (10 min)

1. How many times does `i < 10` run from 0? (2)
2. Infinite loop cause (3)
3. Nested loop count for n×n (5)

## Snippet

```js
for (let i = 0; i < n; i++) s += a[i];
```

---

## Common mistakes

- `i <= a.length` and crash.
- Modifying i inside in two places.

---

## Board drawings

1. Fenceposts.
2. Checkerboard.

