# Lecture 8 — Midterm and WebGPU intro

**Course:** GPU Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** midterm; device/queue  
**Board first:** adapter → device → queue

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

1. Sit midterm: ping-pong, particles, Euler, fluids names, reduce.
2. Request adapter/device.
3. Why WGSL.
4. Don't port the whole particle system this week.
5. CanIUse / HTTPS.

---

## 1. Midterm

FBO swap, packing, dt, Stam names.

## 2. WebGPU

Modern API. Explicit pipelines, bind groups, compute. Chrome. Not a Safari-only lab without a fallback plan.

## 3. Mental map

WebGL program ≈ pipeline. Uniforms ≈ bind group. FBO ≈ texture views.

## Live coding (60 min)

Hello triangle in WebGPU **or** a documented fallback WebGL triangle plus a WGSL reading.

---

## Lab

1. feature detect.
2. error popup.

---

## Homework

1. Reflection + adapter name screenshot.

---

## Quiz (10 min)

1. None.

## Snippet

```js
const adapter = await navigator.gpu.requestAdapter();
const device = await adapter.requestDevice();
```

---

## Common mistakes

- requiring WebGPU on machines that lack it with no fallback story.
- WebGL slander without a triangle.

---

## Board drawings

1. Adapter box.

