# Lecture 1 — Forward rendering review

**Course:** Real-Time Rendering  
**Time:** 75 min lecture + 60 min live coding  
**This week:** one pass, lights in FS  
**Board first:** for each light: add

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

1. Restate the forward path.
2. Count lights vs draw calls.
3. HDR as a need (bright lights).
4. Don't start in deferred.
5. Map to last year's Phong.

---

## 1. Where we are

CG I and WebGL already light a cube. This course is **production looks**: PBR, HDR, shadows, AO names, a post stack, and how to **profile**.

## 2. Forward

Each object, for each light, add. Simple. Dies with many lights — clustered/deferred later and in Advanced CG.

## 3. Energy

Lambert + Blinn can exceed 1. HDR buffers store that; tonemap at the end.

## Live coding (60 min)

A WebGL or Three.js cube with two lights; show saturated LDR vs a fake HDR multiply.

---

## Lab

1. draw call count.
2. light loop in shader vs CPU.

---

## Homework

1. Written: forward vs 'just add another Mesh'.
2. screenshot clip vs no clip.

---

## Quiz (10 min)

1. forward path (4)
2. why HDR (3)
3. deferred this week? (3)

## Snippet

```glsl
vec3 c = albedo * (nDotL0 + nDotL1);
```

---

## Common mistakes

- 10 lights on day one.
- tonemap skipped then 'PBR looks grey'.

---

## Board drawings

1. Forward boxes.

