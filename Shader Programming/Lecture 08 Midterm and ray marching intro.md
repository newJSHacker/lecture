# Lecture 8 — Midterm and ray marching intro

**Course:** Shader Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** midterm; sphere trace idea  
**Board first:** p += d * dir

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

1. Sit midterm: gamma, uv, noise, fBm, SDF2D.
2. Sphere tracing: step by d.
3. Escape and hit thresholds.
4. Don't start with 8 nested SDFs.
5. A sphere and a plane.

---

## 1. Midterm

patterns, noise, SDF ops, gamma.

## 2. March

From the camera, walk along the ray by the SDF distance. Safe if the field is a true SDF (Lipschitz). Blending/smoothmin can break safety — mention.

## 3. Demo

[[WebGL/demos]] raymarch if present; else Shadertoy sphere.

## Live coding (60 min)

March a sphere; color by Lambert.

---

## Lab

1. miss color.
2. max steps slider.

---

## Homework

1. Reflection + a screenshot of a hit.

---

## Quiz (10 min)

1. None.

## Snippet

```glsl
for(int i=0;i<64;i++){ float d = map(p); if(d<eps) break; p += rd*d; t+=d; if(t>far) break; }
```

---

## Common mistakes

- fixed 0.01 steps only and calling it SDF march.
- unbounded loops.

---

## Board drawings

1. Ray with disks.

