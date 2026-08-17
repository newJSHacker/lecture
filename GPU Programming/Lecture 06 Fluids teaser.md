# Lecture 6 — Fluids teaser

**Course:** GPU Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** divergence-free idea  
**Board first:** advect → diffuse → project

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

1. Stable fluids names (Stam).
2. Advect a dye.
3. Why projection (pressure).
4. Don't write a research solver.
5. A 2D dye in an FBO is enough.

---

## 1. Idea

Velocity field in a texture. Advect. Pressure solve makes it incompressible — Jacobi iteration name.

## 2. Scope

A dye blob that swirls is the lab. 3D Navier–Stokes is a thesis.

## 3. Refs

GPU Gems / Stam. Cite.

## Live coding (60 min)

2D dye advected by a mouse-drawn velocity or a vortex field.

---

## Lab

1. one Jacobi extra or a note why skipped.
2. dissipation.

---

## Homework

1. Written: why project.
2. screenshot.

---

## Quiz (10 min)

1. advect (3)
2. incompressible (4)
3. 3D this week? (3)

## Snippet

```glsl
vec2 p = uv - dt * vel; vec4 dye = texture(u_dye, p);
```

---

## Common mistakes

- Unity Visual Effect Graph as the homework.
- unstable huge dt.

---

## Board drawings

1. Velocity + dye.

