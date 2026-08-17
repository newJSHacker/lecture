# Lecture 12 — A mini 2D engine

**Course:** Interactive Web Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** entities, loop, input  
**Board first:** entity list update render

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

1. Entity {update,render}.
2. Input map.
3. Spawn/despawn.
4. Don't invent Unity.
5. Cap entity count.

---

## 1. Architecture

Enough to later map onto Three.js scenes.

## 2. Input

keys set.

## 3. Bounds

n=200 circles fine; n=200000 not.

## Live coding (60 min)

Bouncers with WASD player.

---

## Lab

1. spawn on click.
2. pause.

---

## Homework

1. Written: entity table.
2. Code: mini engine.

---

## Quiz (10 min)

1. update vs render (4)
2. input map (3)
3. cap n (3)

## Snippet

```js
entities.forEach(e => e.update(dt));
entities.forEach(e => e.render(ctx));
```

---

## Common mistakes

- god object 800 lines.
- physics in render.

---

## Board drawings

1. Boxes.

