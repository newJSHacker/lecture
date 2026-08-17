# Lecture 2 — Radiosity idea

**Course:** Advanced Computer Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** patches, form factors  
**Board first:** F_ij = fraction of energy i→j

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

1. Discretize a room into patches.
2. Form factor as a fraction.
3. Gather vs shoot names.
4. Don't require a GPU radiosity engine.
5. Color bleeding on two patches by hand.

---

## 1. Classic

Goral et al. Diffuse-only. View-independent. Great for interiors; bad for mirrors.

## 2. Teaching math

A 4-patch room: students compute a tiny linear system **or** iterate gather with made-up F_ij. Honesty: F_ij from hemicube is named, not coded in full.

## 3. Realtime cousins

Lightmaps baked in Blender. Probes.

## Live coding (60 min)

Two-quad color bleed: iterate `B_i = E_i + ρ_i Σ F_ij B_j` with a 2×2 made-up F.

---

## Lab

1. Blender lightmap bake extra as oracle.
2. plot convergence.

---

## Homework

1. Written: why diffuse-only.
2. spreadsheet or JS of the 2×2.

---

## Quiz (10 min)

1. form factor (4)
2. view independent (3)
3. mirrors (3)

## Snippet

```js
for (let k=0;k<20;k++) for (let i=0;i<n;i++) B[i] = E[i] + rho[i]*dotF(i,B);
```

---

## Common mistakes

- full hemicube as required lab.
- radiosity on a mirror sphere.

---

## Board drawings

1. Patches + arrows.

