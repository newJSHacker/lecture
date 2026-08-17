# Lecture 3 — Conditions

**Course:** Introduction to Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** if / else / comparisons  
**Board first:** true/false diamond

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

1. Write a three-way if.
2. Use ===.
3. Explain && and ||.
4. Avoid assignment inside if.
5. Trace a nested if.

---

## 1. Boolean expressions

`===` and `!==`. `==` is forbidden in this course except to show a bug once. `NaN === NaN` is false — show it.

## 2. Control flow

if / else if / else. Early return as a style. Nested if more than two deep is a smell; use a function.

## 3. Guarding graphics later

`if (!gl)` is the WebGL black-screen cousin. Conditions are how programs refuse to crash.

## Live coding (60 min)

Grade classifier; then `if (x = 0)` bug live.

---

## Lab

1. Guessing game (1–10).
2. Fizz for multiples of 3 (no buzz yet).

---

## Homework

1. Rock-paper-scissors vs computer random.
2. Written: == vs ===.

---

## Quiz (10 min)

1. Result of `0 == ''` (2)
2. Write if for age ≥ 18 (4)
3. Why === (4)

## Snippet

```js
if (x === 0) console.log('zero');
```

---

## Common mistakes

- Assignment in if.
- else attached to the wrong if.

---

## Board drawings

1. Flowchart.
2. == vs === table.

