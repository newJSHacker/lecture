# Lecture 7 — Textures and color space

**Course:** Three.js Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** map, colorSpace  
**Board first:** SRGBColorSpace

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

1. TextureLoader.
2. colorSpace sRGB for albedo.
3. wrap/repeat.
4. normalMap name.
5. Don't sRGB a normal map.

---

## 1. Color

CG I gamma. three r152+ colorSpace.

## 2. Maps

albedo vs normal vs roughness.

## 3. Demo

textures.

## Live coding (60 min)

Albedo on a sphere; wrong colorSpace toggle if you can.

---

## Lab

1. repeat 4.
2. normal extra.

---

## Homework

1. Written: which maps are sRGB.
2. Code: texture.

---

## Quiz (10 min)

1. albedo space (4)
2. normal sRGB? (3)
3. repeat (3)

## Snippet

```js
tex.colorSpace = THREE.SRGBColorSpace;
```

---

## Common mistakes

- sRGB normals.
- uncapped anisotropy always.

---

## Board drawings

1. Maps.

