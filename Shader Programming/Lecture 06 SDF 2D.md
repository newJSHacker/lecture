# Lecture 6 — SDF 2D

**Course:** Shader Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** circle, union, smooth  
**Board first:** d = length(p)-r

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

1. Circle and box SDF.
2. Union/intersection/subtract.
3. smoothmin name.
4. Fill with smoothstep.
5. [[WebGL/14 SDF and Ray Marching]].

---

## 1. Distance fields

A function that returns signed distance to a shape. Rendering is `smoothstep` on d, or later sphere tracing in 3D.

## 2. CSG

min = union, max = intersection. Smoothmin blends.

## 3. Why

Logos, HUDs, 2D games, 3D modeling (Blender) all meet here. IQ's tables are the encyclopedia — students implement three primitives, not fifty.

## Live coding (60 min)

A boolean logo (two circles minus a box).

---

## Lab

1. onion (abs(d)-t) extra.
2. AA with fwidth.

---

## Homework

1. Written: why signed.
2. Code: sdCircle + sdBox.

---

## Quiz (10 min)

1. union op (2)
2. smoothmin idea (4)
3. inside sign (4)

## Snippet

```glsl
float sdCircle(vec2 p, float r){ return length(p) - r; }
```

---

## Common mistakes

- polygon meshes for a 2D logo in a shader course.
- unsigned distance only.

---

## Board drawings

1. CSG tree.

