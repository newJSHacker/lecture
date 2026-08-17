# Lecture 11 — Particles in WebGPU

**Course:** GPU Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** buffer of structs  
**Board first:** compute update + render

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

1. Struct Particle.
2. Compute updates.
3. Vertex pull or instance.
4. Don't keep CPU as the source of truth every frame.
5. Reset compute.

---

## 1. Two passes

Compute: physics. Render: draw points/triangles.

## 2. When stay WebGL

If the audience is Safari-old or the feature is a textured cube, WebGL is enough. Honesty in the README.

## 3. Limits

Buffer sizes. Workgroup limits.

## Live coding (60 min)

N particles in WGSL compute; draw as points.

---

## Lab

1. WebGL fallback note.
2. dt uniform.

---

## Homework

1. Written: when you would not use WebGPU.
2. demo.

---

## Quiz (10 min)

1. source of truth (4)
2. two passes (3)
3. Safari (3)

## Snippet

```wgsl
struct P { pos: vec2f, vel: vec2f }
```

---

## Common mistakes

- uploading 100k positions from JS every frame.
- no fallback story for the course project if required to run in the lab.

---

## Board drawings

1. Compute then draw.

