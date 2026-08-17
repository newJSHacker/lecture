# Lecture 8 — Midterm and types preview

**Course:** Modern JavaScript Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** midterm; TS optional  
**Board first:** x: number

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

1. Sit midterm on ES6/modules/async.
2. Why types.
3. JSDoc or TS optional.
4. any as a smell.
5. Not a TS course.

---

## 1. Midterm

bindings, modules, promises, fetch, npm.

## 2. TS

Optional homework. Interface for a Point. Skip advanced generics.

## 3. JSDoc

Allowed as the typed path without a build.

## Live coding (60 min)

Add JSDoc to lerp; or a .ts Point if the lab has vite+ts.

---

## Lab

1. Typed clamp.
2. Midterm reflection.

---

## Homework

1. Optional TS Point tests.

---

## Quiz (10 min)

1. None.

## Snippet

```ts
export function lerp(a: number, b: number, t: number): number {
  return a + (b - a) * t;
}
```

---

## Common mistakes

- any everywhere.
- Claiming TS mastery after one lab.

---

## Board drawings

1. Point type.

