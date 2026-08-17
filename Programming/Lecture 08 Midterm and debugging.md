# Lecture 8 — Midterm and debugging

**Course:** Introduction to Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** midterm; then debugger  
**Board first:** red squiggle vs runtime error

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

1. Sit a written midterm.
2. Read a stack trace.
3. Use a breakpoint.
4. console.assert.
5. Binary-search a bug.

---

## 1. Midterm

Values, if, loops, functions, arrays, objects. No laptop. See the Week 7 list.

## 2. Debugging

Syntax error vs runtime vs wrong answer. Breakpoints in DevTools. Do not `console.log` fifty times as the only strategy — but it is allowed.

## 3. assert

`console.assert(lerp(0,10,0.5)===5)` is the seed of Week 19 kernel tests in later courses.

## Live coding (60 min)

After the exam: take a broken `average` and fix it with a breakpoint.

---

## Lab

1. Fix three planted bugs in a starter.
2. Write 5 asserts for last week's centroid.

---

## Homework

1. Reflection: one midterm item you missed, rewrite the solution.

---

## Quiz (10 min)

1. None — midterm week. Next quiz is Week 9.

## Snippet

```js
console.assert(clamp(5,0,3)===3, 'clamp high');
```

---

## Common mistakes

- Fixing by rewriting the whole file.
- Ignoring the first stack line.

---

## Board drawings

1. Error kinds.
2. Call stack.

