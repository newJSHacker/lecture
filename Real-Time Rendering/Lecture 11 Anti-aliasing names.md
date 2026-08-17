# Lecture 11 — Anti-aliasing names

**Course:** Real-Time Rendering  
**Time:** 75 min lecture + 60 min live coding  
**This week:** MSAA, TAA, FXAA  
**Board first:** table: where / cost / blur

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

1. MSAA: samples at geometry edges, limited on deferred.
2. FXAA: post, cheap, blurry.
3. TAA: history, ghosting.
4. Don't implement TAA in a week.
5. Pick one for the project and say why.

---

## 1. Why aliasing

Edges, specular sparkle, thin geometry, alpha test.

## 2. Deferred vs MSAA

MSAA hates deferred. That's a reason for FXAA/TAA.

## 3. Alpha

Alpha-to-coverage name. Hair is hard.

## Live coding (60 min)

Screenshot the same edge with AA off vs renderer antialias on vs a cheap FXAA-ish blur extra.

---

## Lab

1. written table.
2. ghosting description from a video still extra.

---

## Homework

1. Written: choose AA for a product viewer.
2. screenshots.

---

## Quiz (10 min)

1. MSAA idea (3)
2. TAA risk (4)
3. FXAA (3)

## Snippet

```js
new THREE.WebGLRenderer({ antialias: true }); // MSAA-ish on forward
```

---

## Common mistakes

- TAA as required homework.
- supersample 8× on a laptop as the lab.

---

## Board drawings

1. AA table.

