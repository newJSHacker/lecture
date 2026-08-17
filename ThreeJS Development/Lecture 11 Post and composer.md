# Lecture 11 — Post and composer

**Course:** Three.js Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** EffectComposer name  
**Board first:** render → pass → screen

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

1. EffectComposer.
2. RenderPass + one pass (e.g. output).
3. bloom name.
4. Cost of full-screen.
5. Don't stack 8 passes blindly.

---

## 1. RTR course

Bloom/HDR labs live there. Here: the plumbing.

## 2. sRGB

output pass color space.

## 3. Demo

post if any.

## Live coding (60 min)

Composer with a cheap pass or gamma output.

---

## Lab

1. toggle composer vs raw render.
2. cost sentence.

---

## Homework

1. Written: extra fill rate.
2. Code: composer.

---

## Quiz (10 min)

1. RenderPass (3)
2. why not 8 passes (4)
3. output color (3)

## Snippet

```js
composer.addPass(new RenderPass(scene, camera));
```

---

## Common mistakes

- composer without understanding framebuffer.

---

## Board drawings

1. Passes.

