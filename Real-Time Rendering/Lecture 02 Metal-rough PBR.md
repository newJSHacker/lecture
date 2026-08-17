# Lecture 2 — Metal-rough PBR

**Course:** Real-Time Rendering  
**Time:** 75 min lecture + 60 min live coding  
**This week:** Cook-Torrance names  
**Board first:** D F G; spec + diff

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

1. Name D, F, G at teaching level.
2. Metalness tints F0.
3. Roughness widens D.
4. Don't implement a 400-line BRDF from scratch unread.
5. Use a known small kernel or Three.js Standard as oracle after writing Lambert-metal.

---

## 1. Idea

Microfacets. Rough = more spread. Metal = no dielectric diffuse, F0 = albedo.

## 2. Split

Students write a **tiny** GGX or use a provided 30-line kernel. Three.js Standard is the oracle to compare, not the lab substitute in the first hour.

## 3. Maps

Blender pack from [[19 Blender for Real-Time Graphics]].

## Live coding (60 min)

Two spheres: gold-ish metal vs plastic; roughness slider.

---

## Lab

1. compare to MeshStandardMaterial extra.
2. F0 chart.

---

## Homework

1. Written: metal vs dielectric in 8 sentences.
2. Code or shader.

---

## Quiz (10 min)

1. F0 of plastic ~ (3)
2. what roughness does (4)
3. D F G (3)

## Snippet

```glsl
vec3 F0 = mix(vec3(0.04), albedo, metallic);
```

---

## Common mistakes

- metalness 0.5 'for look'.
- roughness as a gray albedo.

---

## Board drawings

1. Microfacet cartoon.

