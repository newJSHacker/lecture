# Lecture 4 — Locomotion

**Course:** Virtual and Augmented Reality  
**Time:** 75 min lecture + 60 min live coding  
**This week:** teleport vs smooth  
**Board first:** arc teleport; vignette optional

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

1. Teleport to a nav mesh or plane.
2. Smooth locomotion name and **comfort cost**.
3. Snap turn.
4. Don't force smooth on everyone.
5. Sitting vs standing.

---

## 1. Comfort

Vection makes people sick. Teleport + snap turn is the default student policy unless they document otherwise.

## 2. Nav

A plane is enough. Navmesh name.

## 3. Blink

Fade on teleport extra.

## Live coding (60 min)

Teleport on select-hit a floor; snap turn 30°.

---

## Lab

1. disable smooth or hide behind a setting.
2. vignette extra.

---

## Homework

1. Written: why teleport default.
2. demo.

---

## Quiz (10 min)

1. vection (4)
2. snap turn (3)
3. navmesh (3)

## Snippet

```js
// raycast floor → on select, camera-parent to hit point
```

---

## Common mistakes

- smooth locomotion only, no option.
- flying by default.

---

## Board drawings

1. Arc + fade.

