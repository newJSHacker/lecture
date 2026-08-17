# Lecture 4 — Uniforms

**Course:** WebGL Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** mat4, time, colors  
**Board first:** u_time slider

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

1. uniform locations.
2. upload mat4 column-major.
3. u_time.
4. Don't upload unused every frame without measuring.
5. CPU writes, shader reads.

---

## 1. Uniforms

Constants for a draw call. PVM later.

## 2. Column-major

false in uniformMatrix4fv means already column-major — match kernel.js.

## 3. Demo

04 rotating cube.

## Live coding (60 min)

Spin with u_time; then a color uniform.

---

## Lab

1. Pause time.
2. Two objects different uniforms extra.

---

## Homework

1. Written: uniform vs attribute.
2. Code: time.

---

## Quiz (10 min)

1. uniform vs attribute (4)
2. column-major (3)
3. location of missing name (3)

## Snippet

```js
gl.uniform1f(gl.getUniformLocation(prog,'u_time'), t);
```

---

## Common mistakes

- row-major by accident.
- getUniformLocation every pixel.

---

## Board drawings

1. CPU/GPU arrow.

