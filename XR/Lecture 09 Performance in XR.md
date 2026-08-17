# Lecture 9 — Performance in XR

**Course:** Virtual and Augmented Reality  
**Time:** 75 min lecture + 60 min live coding  
**This week:** fill rate, foveation name  
**Board first:** two views = ~2×

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

1. Stereo is two draws or multiview name.
2. Fixed foveated rendering name.
3. Don't 4k shadows.
4. Measure on device.
5. dpr / framebuffer scale.

---

## 1. Cost

Two eyes. MSAA expensive. Overdraw hurts more.

## 2. Three.js

`renderer.xr.setFramebufferScaleFactor`.

## 3. Quest

Documented targets. Student table: device, scale factor, what they cut.

## Live coding (60 min)

Scale factor 1.0 vs 0.7; note the look vs cost (headset or video).

---

## Lab

1. cut bloom in VR.
2. shadow map 512.

---

## Homework

1. Written: stereo cost.
2. table.

---

## Quiz (10 min)

1. why two views (3)
2. foveation (4)
3. scale factor (3)

## Snippet

```js
renderer.xr.setFramebufferScaleFactor(0.8);
```

---

## Common mistakes

- desktop bloom stack unchanged in VR.
- invented fps.

---

## Board drawings

1. Two frustums.

