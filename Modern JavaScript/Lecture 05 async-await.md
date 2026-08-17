# Lecture 5 — async/await

**Course:** Modern JavaScript Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** try/catch, sequential vs parallel  
**Board first:** await inside async

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

1. Rewrite then as await.
2. try/catch.
3. Parallel with Promise.all.
4. Don't await in a loop when parallel is right.
5. Error UI.

---

## 1. Sugar

await is then with nicer stack traces.

## 2. Parallel

Two independent fetches: all, not await a then await b unless order required.

## 3. for-await

Name only.

## Live coding (60 min)

Load two JSON files in parallel; render.

---

## Lab

1. Sequential vs parallel timing (measure).
2. try/catch around fetch.

---

## Homework

1. Written: when not to parallelize.
2. Code: all.

---

## Quiz (10 min)

1. async function return (3)
2. await in loop smell (4)
3. try/catch (3)

## Snippet

```js
const [a,b] = await Promise.all([fetch(u1), fetch(u2)]);
```

---

## Common mistakes

- await in map without all.
- empty catch.

---

## Board drawings

1. Timeline.

