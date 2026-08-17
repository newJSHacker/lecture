# Lecture 2 — Mesh modeling

**Course:** Blender for Real-Time Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** verts edges faces  
**Board first:** quad vs triangle vs n-gon

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

1. Extrude, inset, loop cut.
2. Keep quads where you can.
3. Name the mesh.
4. Don't boolean everything.
5. Count triangles.

---

## 1. Topology

Real-time cares about **triangle count** and **deformation**. Film cares about subdivision beauty. Prefer quads on deforming surfaces; triangles are what glTF stores anyway.

## 2. Operators

E extrude, I inset, Ctrl+R loop cut, G/S/R. Merge by distance. Face orientation overlay (blue/red).

## 3. Ngons

Allowed on flat caps. Dangerous on curves. Overlay: Face orientation + statistics.

## Live coding (60 min)

Model a simple mug or crate from a cube. Show face orientation. Report triangle count.

---

## Lab

1. A table with 4 legs (keep them separate objects or one mesh — justify).
2. Screenshot statistics.

---

## Homework

1. Written: quad vs tri in real-time.
2. Blend file + triangle count.

---

## Quiz (10 min)

1. extrude (2)
2. why face orientation (4)
3. n-gon risk (4)

## Snippet

```
Viewport overlays → Statistics, Face Orientation
```

---

## Common mistakes

- Sculpting a hero as week-2 homework.
- Inverted normals shipped to Three.js.

---

## Board drawings

1. Quad grid.
2. Red/blue faces.

