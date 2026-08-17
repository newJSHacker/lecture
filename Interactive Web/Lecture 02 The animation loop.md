# Lecture 2 — The animation loop

**Course:** Interactive Web Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** rAF, dt, time  
**Board first:** requestAnimationFrame ring

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

1. rAF loop.
2. dt from timestamps.
3. Clear each frame.
4. Pause.
5. Cap dt.

---

## 1. vs setInterval

rAF syncs to refresh. Tab hidden slows it — good.

## 2. Time

t in seconds. sin(t) for motion.

## 3. Clear

clearRect each frame or trails.

## Live coding (60 min)

A ball on a sine; pause key.

---

## Lab

1. dt-cap.
2. trail vs clear toggle.

---

## Homework

1. Written: why rAF.
2. Code: loop module.

---

## Quiz (10 min)

1. rAF vs interval (4)
2. dt (3)
3. hidden tab (3)

## Snippet

```js
requestAnimationFrame(frame);
```

---

## Common mistakes

- setInterval(16).
- uncapped dt.

---

## Board drawings

1. Loop.

