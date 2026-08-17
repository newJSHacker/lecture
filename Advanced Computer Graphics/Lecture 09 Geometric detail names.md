# Lecture 9 — Geometric detail names

**Course:** Advanced Computer Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** LOD, tessellation, Nanite idea  
**Board first:** error in pixels

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

1. LOD: swap meshes by distance.
2. Tessellation name.
3. Nanite-style: visibility buffer / clustered software raster **names**.
4. Don't claim Nanite in WebGL.
5. Measure polycount vs distance.

---

## 1. Why

Budgets from Blender/RTR meet **algorithm** names here.

## 2. Virtualized geometry

UE5 Nanite: cut only when you can explain visibility buffers at cartoon level. Not a lab port.

## 3. Web

drei `Detailed` / Three.js LOD. That's the lab.

## Live coding (60 min)

Three LOD meshes (or simplified boxes); switch; log tri count.

---

## Lab

1. hysteresis extra.
2. pixel error sentence.

---

## Homework

1. Written: Nanite in 8 honest sentences.
2. LOD demo.

---

## Quiz (10 min)

1. LOD (3)
2. visibility buffer name (4)
3. why not in WebGL lab (3)

## Snippet

```js
lod.addLevel(high, 0); lod.addLevel(low, 20);
```

---

## Common mistakes

- 'we used Nanite' on a glTF.
- popping without hysteresis talk.

---

## Board drawings

1. LOD rings.

