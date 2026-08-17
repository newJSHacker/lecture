# Lecture 5 — Volumes idea

**Course:** Advanced Computer Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** emission, absorption, scatter  
**Board first:** T = exp(-σ t); in-scatter

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

1. Beer–Lambert absorption.
2. Emission in a volume.
3. Single scatter name.
4. Don't a production cloud.
5. Fog as homogeneous volume.

---

## 1. Participating media

Fog, smoke, clouds, skin (SSS name). Homogeneous fog is the lab: transmittance along a ray.

## 2. Phase

Henyey–Greenstein name. Isotropic extra.

## 3. Realtime

Height fog, volumetric lighting names in games.

## Live coding (60 min)

Ray march a homogeneous fog toward a sun disk; Beer–Lambert.

---

## Lab

1. density slider.
2. emission extra.

---

## Homework

1. Written: T = exp(-σt).
2. demo (Canvas or shader).

---

## Quiz (10 min)

1. Beer-Lambert (4)
2. scatter vs absorb (3)
3. HG name (3)

## Snippet

```glsl
float T = exp(-sigma * t);
```

---

## Common mistakes

- OpenVDB as required.
- inhomogeneous 3D tex as week 5 required.

---

## Board drawings

1. Ray through fog.

