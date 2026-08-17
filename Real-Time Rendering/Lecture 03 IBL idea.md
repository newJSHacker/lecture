# Lecture 3 — IBL idea

**Course:** Real-Time Rendering  
**Time:** 75 min lecture + 60 min live coding  
**This week:** irradiance + prefiltered spec  
**Board first:** env as the other light

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

1. Diffuse IBL as a blurred env.
2. Spec IBL as mip by roughness.
3. Split-sum name.
4. Don't require baking a cubemap pipeline from zero.
5. Three.js PMREM as oracle after a teaching slide.

---

## 1. Why IBL

A studio product has *environment* lighting. A single dir light is a lecture, not a catalog shot.

## 2. Split sum

Karis. Name. Implementation can be an env texture + mip LOD = roughness.

## 3. Cost

Cubemap size. Mobile.

## Live coding (60 min)

Metallic sphere in an env; roughness 0 vs 1.

---

## Lab

1. intensity slider.
2. background vs lighting toggle.

---

## Homework

1. Written: IBL vs dir light.
2. screenshot pair.

---

## Quiz (10 min)

1. irradiance (3)
2. mip as roughness (4)
3. PMREM (3)

## Snippet

```js
scene.environment = env; // Three.js oracle after the picture
```

---

## Common mistakes

- 500MB HDR.
- IBL without mentioning HDR.

---

## Board drawings

1. Cubemap + sphere.

