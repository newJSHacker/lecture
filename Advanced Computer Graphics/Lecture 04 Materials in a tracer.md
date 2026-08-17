# Lecture 4 — Materials in a tracer

**Course:** Advanced Computer Graphics  
**Time:** 75 min lecture + 60 min live coding  
**This week:** metal, glass names  
**Board first:** reflect; refract; TIR

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

1. Perfect mirror bounce.
2. Schlick name.
3. Refract + TIR.
4. Don't a full spectral renderer.
5. Dielectric vs metal in paths.

---

## 1. BXDF teaching

Mirror is easy. Glass: `refract`, ior 1.5, Schlick mix. Microfacet in a tracer is RTR+this — optional extra.

## 2. Recursion

Max depth. Russian roulette name.

## 3. Three.js

WebGLPathTracer / similar as **oracle** after theirs looks like noise.

## Live coding (60 min)

A mirror sphere and a glass sphere (or fake glass with reflect-only if refract slips); still Lambert floor.

---

## Lab

1. ior slider extra.
2. depth 2 vs 5.

---

## Homework

1. Written: TIR.
2. screenshots.

---

## Quiz (10 min)

1. Schlick (3)
2. TIR (4)
3. max depth (3)

## Snippet

```js
const k = schlick(cos, 0.04); // mix reflect/refract
```

---

## Common mistakes

- dispersion as required.
- unbounded recursion.

---

## Board drawings

1. Reflect / refract.

