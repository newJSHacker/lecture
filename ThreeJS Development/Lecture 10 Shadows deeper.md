# Lecture 10 — Shadows deeper

**Course:** Three.js Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** types, bias  
**Board first:** bias / normalBias

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

1. PCF name.
2. bias.
3. camera helper for shadow cam.
4. Frustum of the light.
5. Acne vs peter-panning.

---

## 1. RTR later

Full shadow maps. Here: practical knobs.

## 2. Helpers

CameraHelper on shadow.camera.

## 3. CSM name

Skip implementation.

## Live coding (60 min)

Tune bias on a character-scale cube.

---

## Lab

1. helper on.
2. mapSize experiment measured.

---

## Homework

1. Written: acne vs panning.
2. Code: bias.

---

## Quiz (10 min)

1. bias (4)
2. PCF (3)
3. helper (3)

## Snippet

```js
light.shadow.bias = -0.0001;
```

---

## Common mistakes

- bias 0.1 destroying shadows.
- one huge directional covering the earth.

---

## Board drawings

1. Acne.

