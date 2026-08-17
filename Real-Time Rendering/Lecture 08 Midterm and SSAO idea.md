# Lecture 8 — Midterm and SSAO idea

**Course:** Real-Time Rendering  
**Time:** 75 min lecture + 60 min live coding  
**This week:** midterm; AO as post  
**Board first:** sample hemisphere in view space

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

1. Sit midterm: PBR knobs, HDR, bloom, shadow map, PCF.
2. SSAO: sample neighbors in depth.
3. It's a fake.
4. Don't require a production HBAO.
5. Noise + blur.

---

## 1. Midterm

metal-rough, IBL idea, tonemap, bloom chain, shadow compare.

## 2. SSAO

Darken where depth neighbors are occluders. View-space. Horizon-based names only.

## 3. Artifacts

Dark rims, noise, missing on sky.

## Live coding (60 min)

A corner of two planes with a cheap SSAO or a Three.js SAO pass **explained**.

---

## Lab

1. toggle.
2. radius slider.

---

## Homework

1. Reflection + AO screenshot.

---

## Quiz (10 min)

1. None.

## Snippet

```glsl
// sample n offsets in a hemisphere, count closer depths
```

---

## Common mistakes

- SSAO as GI.
- full VXGI.

---

## Board drawings

1. Hemisphere samples.

