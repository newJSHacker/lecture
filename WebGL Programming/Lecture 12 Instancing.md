# Lecture 12 — Instancing

**Course:** WebGL Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** divisor, one draw  
**Board first:** gl.drawArraysInstanced

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

1. instance attribute.
2. divisor 1.
3. offset per instance.
4. When to instance.
5. Don't instance n=3.

---

## 1. GPU repetition

Forest, particles, bolts. Demo 14.

## 2. CPU

Still upload instance buffer when it changes.

## 3. Limits

Attribute slots.

## Live coding (60 min)

100 cubes instanced vs 100 draw calls (measure).

---

## Lab

1. color per instance.
2. measured table.

---

## Homework

1. Written: when instancing wins.
2. Code: instanced.

---

## Quiz (10 min)

1. divisor (4)
2. drawInstanced (3)
3. n=3 (3)

## Snippet

```js
gl.vertexAttribDivisor(loc, 1);
```

---

## Common mistakes

- instancing without measuring.
- divisor on the wrong attrib.

---

## Board drawings

1. Forest.

