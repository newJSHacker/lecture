# Lecture 13 — Patterns for graphics apps

**Course:** Modern JavaScript Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** game loop, modules, state  
**Board first:** update vs render

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

1. Separate update(dt) and render().
2. State object.
3. Don't put physics in the shader this course.
4. rAF loop.
5. Pause flag.

---

## 1. Loop

Interactive Web and CG I already; now as architecture.

## 2. State

One object. Serialize later.

## 3. Dirty flags

Name for editors.

## Live coding (60 min)

A bouncing ball with dt, pause, reset.

---

## Lab

1. State to JSON extra.
2. Cap dt.

---

## Homework

1. Written: update vs render.
2. Code: loop.

---

## Quiz (10 min)

1. rAF (3)
2. dt (4)
3. pause (3)

## Snippet

```js
function frame(t){ const dt=t-last; last=t; update(dt); render(); requestAnimationFrame(frame); }
```

---

## Common mistakes

- setInterval(16) as the loop.
- Uncapped dt spikes.

---

## Board drawings

1. Loop box.

