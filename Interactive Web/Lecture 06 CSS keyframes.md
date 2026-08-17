# Lecture 6 — CSS keyframes

**Course:** Interactive Web Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** loops, steps  
**Board first:** @keyframes spin

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

1. @keyframes.
2. animation-duration/iteration.
3. steps() for sprites.
4. pause animation-play-state.
5. Don't replace a game loop with CSS for physics.

---

## 1. Declarative motion

Loaders, idle UI. Not a physics engine.

## 2. Sprite sheets

steps() + background-position.

## 3. JS control

element.style.animationPlayState.

## Live coding (60 min)

A spinner; then a 4-frame sprite extra.

---

## Lab

1. Pause on hover.
2. Two animations sequenced extra.

---

## Homework

1. Written: CSS vs rAF.
2. Code: spinner.

---

## Quiz (10 min)

1. @keyframes (3)
2. steps (4)
3. physics in CSS? (3)

## Snippet

```css
@keyframes spin { to { transform: rotate(360deg); } }
```

---

## Common mistakes

- physics in keyframes.
- infinite heavy filters.

---

## Board drawings

1. Spinner.
2. sprite strip.

