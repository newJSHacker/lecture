# Lecture 6 — Lights and cameras

**Course:** Blender for Real-Time Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** area vs sun; exposure  
**Board first:** sun for dir light; area for studio

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

1. Add Sun and Area lights.
2. Set camera focal length.
3. Exposure / filmic name.
4. Don't light with 12 suns.
5. Match a product-shot mood.

---

## 1. Real-time vs Cycles

This course previews in Eevee or Material Preview so students see what a game-ish engine can do. Cycles caustics are not the learning goal.

## 2. Light types

Sun ≈ directional. Point ≈ omni. Spot. Area. Three.js has the same names.

## 3. Camera

35–50 mm product. 24 mm archviz. Sensor fit. This becomes `PerspectiveCamera.fov`.

## Live coding (60 min)

Light a crate on a plane; one sun + one fill. Camera frame.

---

## Lab

1. Disable extra lights.
2. FOV vs dolly extra.

---

## Homework

1. Written: sun vs point in Three.js.
2. Turntable screenshot.

---

## Quiz (10 min)

1. sun maps to (3)
2. why one key light (4)
3. fov (3)

## Snippet

```
Light → Sun  |  Camera → 50 mm
```

---

## Common mistakes

- Lighting with emission meshes only and calling it PBR.
- ISO 6400 noise as style.

---

## Board drawings

1. Key/fill.
2. Frustum.

