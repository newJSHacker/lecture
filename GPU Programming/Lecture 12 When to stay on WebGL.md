# Lecture 12 — When to stay on WebGL

**Course:** GPU Programming  
**Time:** 75 min lecture + 60 min live coding  
**This week:** compatibility, tools  
**Board first:** table: feature → API

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

1. Feature detect.
2. Team skill.
3. Spector vs WebGPU tools.
4. A product viewer can stay WebGL.
5. Don't rewrite CG I in WebGPU.

---

## 1. Decision

IGWT is web. WebGL2 still ships the catalog. WebGPU is the future compute/graphics API — teach it without stranding labs.

## 2. Porting

Shaders rewrite. Pipelines are more verbose. Gain: compute, less driver magic.

## 3. Project rule

Pick one API for the final unless you explicitly demo both.

## Live coding (60 min)

A one-page decision for *your* capstone-shaped idea.

---

## Lab

1. canIuse screenshot.
2. risk list.

---

## Homework

1. Written: decision memo 1 page.
2. none.

---

## Quiz (10 min)

1. one reason WebGL (3)
2. one reason WebGPU (4)
3. detect (3)

---

## Common mistakes

- rewriting the semester in three APIs.

---

## Board drawings

1. Decision tree.

