# Lecture 6 — Volume marching

**Course:** Advanced Computer Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** heterogeneous, woodcock name  
**Board first:** step σ(x); accumulate

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

1. Regular tracking: step, sample density.
2. Woodcock (delta tracking) name.
3. Noise as density from fBm (shader course).
4. Don't 0.001 steps always.
5. HDR fog glow extra.

---

## 1. Heterogeneous

σ varies. Shadertoy clouds. Cost vs step size.

## 2. Tracking

Delta tracking is unbiased for some media — name, optional code.

## 3. Realtime

Slice volumes, froxels names.

## Live coding (60 min)

fBm density ball; cheap emission; screenshot.

---

## Lab

1. step size compare 2 screenshots.
2. shadow in volume extra.

---

## Homework

1. Written: bias vs step.
2. GLSL or JS.

---

## Quiz (10 min)

1. regular tracking (3)
2. cost (4)
3. froxel (3)

## Snippet

```glsl
for(float t=0.; t<far; t+=dt){ float d = density(p); acc += emit*d*dt*T; T *= exp(-d*dt); }
```

---

## Common mistakes

- research cloud as the lab.
- dt=0.

---

## Board drawings

1. Steps inside a ball.

