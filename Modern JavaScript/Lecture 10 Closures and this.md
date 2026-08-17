# Lecture 10 — Closures and this

**Course:** Modern JavaScript Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** factory, bind  
**Board first:** inner function remembering n

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

1. Write a closure counter.
2. Explain lexical scope.
3. this in method vs arrow.
4. bind / arrow field.
5. Don't overuse bind.

---

## 1. Closure

Function + environment. Private counters. Module state.

## 2. this

Methods. Losing this on callback — arrow or bind.

## 3. Graphics

A closure over a GL context is common and easy to leak — mention.

## Live coding (60 min)

makeCounter(); then a button this bug and fix.

---

## Lab

1. Once function extra.
2. Tests for counter.

---

## Homework

1. Written: closure vs global.
2. Code: fix this.

---

## Quiz (10 min)

1. what a closure keeps (4)
2. this in arrow (3)
3. bind (3)

## Snippet

```js
function makeCounter(){ let n=0; return () => ++n; }
```

---

## Common mistakes

- Closures as magic.
- this hacked with window.

---

## Board drawings

1. Environment box.

