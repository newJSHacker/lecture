# Lecture 1 — ES6 bindings and arrows

**Course:** Modern JavaScript Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** let const arrow  
**Board first:** function vs =>

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

1. let/const.
2. Arrow functions.
3. Default params.
4. No var.
5. When this is different (name).

---

## 1. Why ES6+

The language of Three.js examples. Teaching old var is harm.

## 2. Arrows

Shorter, lexical this. Not identical to function in all ways — constructors.

## 3. Defaults

function f(x=0).

## Live coding (60 min)

Rewrite a var/function script into const/arrows.

---

## Lab

1. 5 arrows with tests.
2. A default-param helper.

---

## Homework

1. Written: this and arrows, 1 page.
2. Code: rewrite.

---

## Quiz (10 min)

1. const rebound (3)
2. arrow vs function construct (4)
3. default param (3)

## Snippet

```js
const add = (a, b = 0) => a + b;
```

---

## Common mistakes

- var.
- arrows as constructors.

---

## Board drawings

1. Binding table.

