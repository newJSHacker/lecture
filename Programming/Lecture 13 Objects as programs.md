# Lecture 13 — Objects as programs

**Course:** Introduction to Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** tiny OOP, methods  
**Board first:** object with a method arrow

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

1. Write a method that uses this.
2. Know this pitfalls in callbacks (name).
3. Prefer functions plus records if this confuses.
4. A class is optional sugar.
5. Do not require inheritance.

---

## 1. Methods

`counter.inc()` mutates. this is the receiver. Losing this in a callback is a later JS course topic — demo once.

## 2. class

`class Point { constructor(x,y){...} dist(){...} }`. Optional. Records + functions are enough for IGWT math kernels.

## 3. Inheritance

Skip. Composition: a sprite has a point.

## Live coding (60 min)

A `BankAccount` with deposit/withdraw; then a `Point.dist`.

---

## Lab

1. Vector object with add (returns new).
2. Do not use inheritance.

---

## Homework

1. Written: this in one paragraph.
2. Code: Point class or record+functions, your choice, tests.

---

## Quiz (10 min)

1. What is this (3)
2. Why inheritance is skipped (3)
3. dist of two points (4)

## Snippet

```js
class Point {
  constructor(x,y){ this.x=x; this.y=y; }
  dist(q){ return Math.hypot(this.x-q.x, this.y-q.y); }
}
```

---

## Common mistakes

- Deep inheritance for a homework.
- this unbound.

---

## Board drawings

1. Point method.
2. Has-a vs is-a.

