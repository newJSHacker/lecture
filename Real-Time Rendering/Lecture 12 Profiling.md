# Lecture 12 — Profiling

**Course:** Real-Time Rendering  
**Time:** 75 min lecture + 60 min live coding  
**This week:** GPU vs CPU, budgets  
**Board first:** draw calls, overdraw, ms

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

1. Use renderer.info / Spector.js name / Chrome GPU.
2. Measure before optimizing.
3. Overdraw.
4. Don't invent 60 fps.
5. A budget sheet.

---

## 1. Two clocks

CPU: JS, draw calls. GPU: fill rate, bandwidth, shader cost.

## 2. Tools

Spector.js, RenderDoc (desktop), three.js info, timestamp queries name.

## 3. Student rule

A table with **device, resolution, what changed, ms**. No fantasy.

## Live coding (60 min)

Profile a scene: one change (shadow map size or pixel ratio); record two rows.

---

## Lab

1. overdraw viz extra (additive white).
2. cut one pass.

---

## Homework

1. Written: budget for *your* project device.
2. measured table.

---

## Quiz (10 min)

1. CPU vs GPU bound (4)
2. overdraw (3)
3. why measure (3)

## Snippet

```js
console.table(renderer.info.render);
```

---

## Common mistakes

- 'it's 60 on my machine' with no numbers.
- optimizing textures last when they are 8k.

---

## Board drawings

1. Budget sheet.

