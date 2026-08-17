# Lecture 4 — Lights and shadows intro

**Course:** Three.js Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** dir/point/ambient  
**Board first:** shadow map size

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

1. Ambient + directional.
2. cast/receive shadow.
3. shadow.mapSize.
4. Helper.
5. Don't add 12 lights.

---

## 1. Energy

Too many lights is a later clustered topic.

## 2. Shadows

Shadow mapping course in RTR. Here: enable and see acne.

## 3. Demo

lights demo.

## Live coding (60 min)

Lit cube + plane; toggle shadow.

---

## Lab

1. light helper.
2. mapSize 512 vs 2048 extra measure.

---

## Homework

1. Written: acne.
2. Code: shadows.

---

## Quiz (10 min)

1. castShadow (3)
2. ambient purpose (3)
3. mapSize (4)

## Snippet

```js
dir.castShadow = true; renderer.shadowMap.enabled = true;
```

---

## Common mistakes

- 10 point lights as the aesthetic.
- mapSize 8192 on integrated GPU.

---

## Board drawings

1. Light + plane.

