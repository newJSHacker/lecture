# Lecture 5 — Functions

**Course:** Introduction to Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** parameters, return, scope  
**Board first:** box with in-arrows and one out-arrow

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

1. Write a pure function with a return.
2. Trace parameter vs argument.
3. Local vs outer scope.
4. Avoid globals.
5. Name functions with verbs.

---

## 1. A function is a named recipe

Parameters are local. Return sends a value out. `console.log` inside is a side effect — allowed for debugging, not as the only result of a math helper.

## 2. Scope

let is block-scoped. A loop `i` is not visible after the block. Closures wait until Week 11 of Modern JS; here just: inner can read outer.

## 3. Graphics later

`putPixel`, `dot`, `orient` are functions. If they cannot write a `clamp(x,a,b)`, they cannot write a renderer.

## Live coding (60 min)

Implement `clamp`, `lerp`, `min3`. Unit-test with console.assert.

---

## Lab

1. isEven, max3, countVowels.
2. A function that returns, not only logs.

---

## Homework

1. 8 tests for lerp.
2. Written: side effect vs return.

---

## Quiz (10 min)

1. What does a missing return yield? (3)
2. Scope of let in for (3)
3. Write clamp (4)

## Snippet

```js
function clamp(x, a, b) { return Math.max(a, Math.min(b, x)); }
```

---

## Common mistakes

- Functions that only log.
- Globals for everything.

---

## Board drawings

1. Function box.
2. Call stack two frames.

