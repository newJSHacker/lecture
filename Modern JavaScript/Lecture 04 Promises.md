# Lecture 4 — Promises

**Course:** Modern JavaScript Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** then catch finally  
**Board first:** pending fulfilled rejected

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

1. Create a Promise.
2. then/catch.
3. Promise.all name.
4. Error swallow bug.
5. Fetch returns a promise.

---

## 1. States

Pending, fulfilled, rejected.

## 2. Composition

then chains. all vs allSettled names.

## 3. Errors

Forgotten catch. async week next.

## Live coding (60 min)

Fake load with setTimeout wrapped in a Promise; then fetch data.json.

---

## Lab

1. Promise.all of two fake loads.
2. Error path UI.

---

## Homework

1. Written: why promises vs callbacks.
2. Code: timeout promise.

---

## Quiz (10 min)

1. three states (3)
2. fetch return type (3)
3. unhandled rejection (4)

## Snippet

```js
new Promise((res) => setTimeout(res, 500));
```

---

## Common mistakes

- then without catch.
- new Promise for already-sync code everywhere.

---

## Board drawings

1. State machine.

