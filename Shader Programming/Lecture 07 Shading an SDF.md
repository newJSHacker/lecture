# Lecture 7 — Shading an SDF

**Course:** Shader Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** normals from gradient  
**Board first:** n = normalize(vec3(d(p+e)-d(p-e)))

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

1. Estimate a 2D/3D normal with tetrahedral or central differences.
2. Lambert on an extruded SDF or a 2D fake light.
3. Don't analytic-only if they cannot finite-difference.
4. Link lighting.glsl.

---

## 1. Gradient

The normal is ∇f for an SDF f. In 2D, light a 'height' or fake 3D with n.xy.

## 2. Soft shadow name

IQ's `shadow` via raymarch — week 9. This week: N·L.

## 3. Energy

Still Lambert. PBR is RTR course.

## Live coding (60 min)

Lit circle SDF; light angle slider.

---

## Lab

1. two lights extra.
2. specular blinn extra.

---

## Homework

1. Written: why finite difference.
2. Code: normal2.

---

## Quiz (10 min)

1. epsilon too big (3)
2. n from d (4)
3. Lambert (3)

## Snippet

```glsl
vec2 n = normalize(vec2(d(p+vec2(e,0))-d(p-vec2(e,0)), d(p+vec2(0,e))-d(p-vec2(0,e))));
```

---

## Common mistakes

- analytic n and finite-difference n never compared.
- e=0.1 on a tiny shape.

---

## Board drawings

1. Gradient.

