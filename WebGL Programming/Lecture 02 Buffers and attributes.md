# Lecture 2 — Buffers and attributes

**Course:** WebGL Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** ARRAY_BUFFER, layout  
**Board first:** attribute loc ↔ stride

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

1. createBuffer.
2. vertexAttribPointer.
3. enableVertexAttribArray.
4. Match shader `in`.
5. Don't leave locations -1.

---

## 1. GPU memory

CPU arrays are uploaded. Changing every frame is allowed but cost.

## 2. Layout

size, type, stride, offset.

## 3. Demo

02 colored triangle, 03 indexed quad.

## Live coding (60 min)

Interleaved pos+color; draw.

---

## Lab

1. Indexed quad.
2. A wrong stride bug then fix.

---

## Homework

1. Written: stride.
2. Code: indexed quad.

---

## Quiz (10 min)

1. bindBuffer (3)
2. stride 0 meaning (4)
3. location -1 (3)

## Snippet

```js
gl.vertexAttribPointer(loc, 3, gl.FLOAT, false, 0, 0);
```

---

## Common mistakes

- never enabling the attrib.
- WebGL1 attrib vs in mix.

---

## Board drawings

1. Layout.

