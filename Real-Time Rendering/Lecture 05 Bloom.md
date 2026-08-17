# Lecture 5 — Bloom

**Course:** Real-Time Rendering  
**Time:** 75 min lecture + 60 min live coding  
**This week:** bright pass + blur + add  
**Board first:** threshold → blur → combine

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

1. Extract highlights.
2. Separable blur name.
3. Add back.
4. Don't bloom the whole LDR image as 'glow'.
5. FBO ping-pong.

---

## 1. Pipeline

Same as WebGL post. Threshold on HDR. Blur. Combine after tonemap or before — pick a policy and stick to it.

## 2. Artifacts

Fireflies, threshold too low, huge kernel.

## 3. Three.js

UnrealBloomPass as oracle **after** they draw the boxes.

## Live coding (60 min)

Bloom a bright sphere; toggle.

---

## Lab

1. threshold slider.
2. half-res extra.

---

## Homework

1. Written: three passes.
2. screenshots on/off.

---

## Quiz (10 min)

1. bright pass (3)
2. separable (4)
3. why HDR first (3)

## Snippet

```glsl
vec3 hi = max(c - vec3(1.0), vec3(0.0));
```

---

## Common mistakes

- bloom as a substitute for lighting.
- full-res 12-tap in all directions naive 2D.

---

## Board drawings

1. Three FBOs.

