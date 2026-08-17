# Lecture 4 — UV unwrapping

**Course:** Blender for Real-Time Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** seams, islands, texel  
**Board first:** cut seams, unwrap, pack

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

1. Mark seams on a crate.
2. Unwrap and pack islands.
3. Check texel density roughly.
4. Don't overlap unless intended.
5. Checker texture as debug.

---

## 1. Why UVs

The fragment shader samples a 2D image. UVs are the mapping. Stretch = blur. Overlap = two faces share texels (lightmaps hate this; albedo sometimes OK for trim).

## 2. Seams

Put seams where they hide. Cylinders: one side seam + caps.

## 3. Checker

Apply a checker grid material. Even squares = good. Skinny rectangles = stretch.

## Live coding (60 min)

Unwrap the week-2 crate; checker; screenshot UV editor + 3D.

---

## Lab

1. Pack with a margin.
2. One overlap bug then fix.

---

## Homework

1. Written: what a seam is.
2. UV screenshot.

---

## Quiz (10 min)

1. island (3)
2. stretch symptom (4)
3. why checker (3)

## Snippet

```
U → Unwrap  |  UV editor → Pack Islands
```

---

## Common mistakes

- Smart UV project on a character as the only method.
- Tiny islands, giant waste.

---

## Board drawings

1. Seams on a cube.
2. Checker.

