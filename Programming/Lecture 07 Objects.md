# Lecture 7 — Objects

**Course:** Introduction to Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** records, nested data  
**Board first:** dot vs bracket

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

1. Create an object literal.
2. Read/write fields.
3. Nest a point `{x,y}`.
4. JSON.parse/stringify name.
5. Do not use objects as arrays.

---

## 1. Records

A point is `{x, y}`. A student is `{name, scores: []}`. This is the mesh vertex of Semester 2.

## 2. Dot and bracket

`p.x` vs `p['x']`. Brackets when the key is in a variable.

## 3. JSON

Show stringify of a point. Mention that JSON cannot store functions or NaN. File I/O waits; clipboard paste is enough.

## Live coding (60 min)

An array of `{x,y}` points; compute centroid.

---

## Lab

1. Address book of 3 people.
2. Deep vs shallow copy discussion in comments.

---

## Homework

1. Parse a JSON string of points, sum x.
2. Written: when to use array vs object.

---

## Quiz (10 min)

1. Access y of {x:1,y:2} (2)
2. JSON of a point (4)
3. Why not object as list (4)

## Snippet

```js
const p = { x: 1, y: 2 };
```

---

## Common mistakes

- `p[x]` without quotes.
- Circular JSON.

---

## Board drawings

1. Point record.
2. Tiny JSON.

