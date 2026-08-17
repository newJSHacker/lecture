# Lecture 11 — Terrain

**Course:** Shader Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** heightmap fBm, lod name  
**Board first:** y = fbm(xz)

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

1. Height = fBm(xz).
2. Normal from neighbors.
3. Cheap fog.
4. Don't march 256 steps if 64 works.
5. Color by slope/height.

---

## 1. Terrain

The classic IQ scene. One sun, fog, height color.

## 2. LOD

Step size can grow with t. Name only unless they implement.

## 3. Textures

Optional triplanar name. Not required.

## Live coding (60 min)

Fullscreen terrain march; fog.

---

## Lab

1. snow line extra.
2. shadow extra if time.

---

## Homework

1. Written: height vs mesh terrain.
2. GLSL.

---

## Quiz (10 min)

1. height fbm (3)
2. normal from height (4)
3. fog (3)

## Snippet

```glsl
float h = fbm(p.xz * 0.25);
```

---

## Common mistakes

- DEM downloads as the week.
- unlimited steps.

---

## Board drawings

1. Slice of hills.

