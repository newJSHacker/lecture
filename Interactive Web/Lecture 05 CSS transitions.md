# Lecture 5 — CSS transitions

**Course:** Interactive Web Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** hover, states  
**Board first:** transition: transform .2s

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

1. transition property.
2. transform/opacity only for perf.
3. prefers-reduced-motion.
4. Don't transition all.
5. DevTools animation.

---

## 1. States

hover, focus, class on.

## 2. Properties

transform and opacity composite. Layout-triggering props jank.

## 3. Motion

Respect reduced motion. Inclusive teaching.

## Live coding (60 min)

A button that lifts on hover; a class toggle.

---

## Lab

1. reduced-motion media query.
2. Don't transition width.

---

## Homework

1. Written: why transform.
2. Code: card.

---

## Quiz (10 min)

1. which props (4)
2. reduced motion (3)
3. transition all smell (3)

## Snippet

```css
@media (prefers-reduced-motion: reduce){ * { transition: none !important; } }
```

---

## Common mistakes

- transition: all 1s.
- ignoring reduced motion.

---

## Board drawings

1. Lift.
2. media.

