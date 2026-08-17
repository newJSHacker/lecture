# Lecture 7 — GSAP intro

**Course:** Interactive Web Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** tweens, timelines  
**Board first:** gsap.to(el,{x:80})

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

1. A tween.
2. A timeline.
3. fromTo.
4. Kill on unmount name.
5. Local `vendor/gsap.min.js` only; don't make GSAP the whole site.

---

## 1. Why a library

Timelines beat ad-hoc rAF for UI stories. Games still need a loop.

## 2. GSAP

Industry UI. Course: 2 weeks of taste, not certification.

## 3. Bundle

Know the cost. Prefer CSS if one hover.

## Live coding (60 min)

A 3-step timeline: fade, move, color.

---

## Lab

1. Stagger extra.
2. Respect reduced motion: skip timeline.

---

## Homework

1. Written: when not to GSAP.
2. Code: timeline.

---

## Quiz (10 min)

1. tween vs timeline (4)
2. kill (3)
3. CSS enough? (3)

## Snippet

```html
<script src="../vendor/gsap.min.js"></script>
<script>
gsap.to('.box', { x: 80, duration: 0.6 });
</script>
```

---

## Common mistakes

- GSAP for every pixel of a renderer.
- no reduced motion.

---

## Board drawings

1. Timeline.

