# Lecture 10 — Baking and maps

**Course:** Blender for Real-Time Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** normal, AO names  
**Board first:** high → low bake idea

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

1. Know what a normal map stores.
2. Bake a simple high-to-low **or** paint a roughness variation.
3. AO name.
4. Don't bake 8k for a crate.
5. sRGB vs non-color.

---

## 1. Maps

BaseColor sRGB. Normal / Roughness / Metal non-color. Same as Three.js `colorSpace` week.

## 2. Bake

Cage, ray distance. A subdivided bevelled cube onto a low cube is enough. Substance is optional, not required.

## 3. Size

512–1k for student crates. 4k is a budget lecture, not a flex.

## Live coding (60 min)

Bake or paint roughness dirt on the crate; show in Principled.

---

## Lab

1. Normal map on a flat plane from a high bevel extra.
2. Color space check.

---

## Homework

1. Written: which maps are sRGB.
2. Map list in README.

---

## Quiz (10 min)

1. normal map channels (4)
2. AO (3)
3. 4k on a mug? (3)

## Snippet

```
Image Texture → Color Space: sRGB (albedo) / Non-Color (normal, rough)
```

---

## Common mistakes

- Baking every map at 8k.
- sRGB normals.

---

## Board drawings

1. High-low arrows.
2. Map slots.

