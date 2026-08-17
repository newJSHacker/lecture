# Lecture 4 — Value noise

**Course:** Shader Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** hash, lerp  
**Board first:** grid corners → bilinear

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

1. Hash a lattice point.
2. Bilinear interpolate.
3. See the grid.
4. Don't call random() in GLSL (it does not exist).
5. 1:1 with [[WebGL/13 Noise]].

---

## 1. Why noise

Fire, water, terrain, film grain. Deterministic: same uv → same value.

## 2. Hash

sin/dot hacks are OK for teaching. They are not crypto. Artifacts exist — show them.

## 3. Value vs gradient

Value noise interpolates scalars. Perlin interpolates gradients — next week fBm can use either.

## Live coding (60 min)

Fullscreen value noise; slider for scale.

---

## Lab

1. Animate z as time extra.
2. Show lattice overlay.

---

## Homework

1. Written: why hash.
2. Code: noise(vec2).

---

## Quiz (10 min)

1. why no Math.random (3)
2. bilinear (4)
3. artifact (3)

## Snippet

```glsl
float hash(vec2 p){ return fract(sin(dot(p, vec2(127.1,311.7))) * 43758.5453); }
```

---

## Common mistakes

- true random per frame (fireflies).
- copying a 200-line library unread.

---

## Board drawings

1. Lattice.
2. Lerp.

