# Lecture 5 — Principled BSDF

**Course:** Blender for Real-Time Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** base color, metal, roughness  
**Board first:** metalness 0 or 1; roughness slider

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

1. Assign Principled.
2. Base color vs emission.
3. Metalness almost binary.
4. Roughness as the 'blur of spec'.
5. Not to fake metal with only a blue specular.

---

## 1. PBR teaching

Same knobs as Three.js `MeshStandardMaterial` and later the RTR course. BaseColor, Metallic, Roughness, Normal. Specular workflow is legacy.

## 2. Metalness

Dielectric 0, metal 1. 0.4 'because it looked nice' is usually wrong.

## 3. Preview

Material Preview vs Rendered. Use an HDRI for preview; students judge metal under a gray clay viewport and think PBR is broken.

## Live coding (60 min)

Three spheres: plastic, brushed metal, rubber. Same HDRI.

---

## Lab

1. A crate with two materials.
2. Emission as a tiny LED extra.

---

## Homework

1. Written: map to MeshStandardMaterial.
2. Blend + screenshot.

---

## Quiz (10 min)

1. metalness of painted wood (3)
2. roughness meaning (4)
3. three.js names (3)

## Snippet

```
Principled: Base Color, Metallic, Roughness, Normal
```

---

## Common mistakes

- metalness 0.5 on everything.
- Judging in solid view.

---

## Board drawings

1. Three spheres.
2. Knob table.

