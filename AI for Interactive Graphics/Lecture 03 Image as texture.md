# Lecture 3 — Image as texture

**Course:** AI for Interactive Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** gen → glTF/Three  
**Board first:** png → TextureLoader

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

1. Generate or mock an albedo.
2. sRGB color space.
3. Don't gen a normal map and treat as sRGB.
4. License/ToS of the image model.
5. Size budgets (1k).

---

## 1. Pipeline

Prompt → image → Three.js map. This is look-dev with a dice roll. Students still know PBR slots from RTR/Blender.

## 2. Control

Seed, size, retries. A human picks among 4, not first-output-wins for the report.

## 3. Cite

Prompt + model + date in README.

## Live coding (60 min)

Apply a generated/mock albedo to a sphere; second sphere with a hand-made color for comparison.

---

## Lab

1. reject 3 images.
2. budget 1024.

---

## Homework

1. Written: what you still had to fix by hand.
2. screenshots.

---

## Quiz (10 min)

1. sRGB (3)
2. why pick among 4 (4)
3. normal map space (3)

## Snippet

```js
map.colorSpace = THREE.SRGBColorSpace;
```

---

## Common mistakes

- 8k gens.
- claiming PBR from one diffuse.

---

## Board drawings

1. Prompt → map.

