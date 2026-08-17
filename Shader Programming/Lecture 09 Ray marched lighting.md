# Lecture 9 — Ray marched lighting

**Course:** Shader Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** soft shadow, AO names  
**Board first:** shadow ray toward L

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

1. Secondary march toward the light.
2. Soft shadow idea (closest approach).
3. Cheap AO from SDF.
4. Don't 128 lights.
5. Still one sun.

---

## 1. Shadows

If map(p) hits before the light, it's shadowed. Soft: track minimum d/t.

## 2. AO

Sample SDF along normal. Darken crevices. Fake, fast.

## 3. Materials

Albedo per object id from the map() return.

## Live coding (60 min)

Sphere+plane with a soft-ish shadow.

---

## Lab

1. AO toggle.
2. material id extra.

---

## Homework

1. Written: why second march.
2. Code: shadow().

---

## Quiz (10 min)

1. hit before light (4)
2. soft idea (3)
3. AO (3)

## Snippet

```glsl
float shadow(vec3 p, vec3 l){ /* march toward l, return 0 if blocked */ }
```

---

## Common mistakes

- stencil shadows speech.
- AO as SSAO from RTR without saying so.

---

## Board drawings

1. Two rays.

