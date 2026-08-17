# Lecture 10 — Hybrid SVG + Canvas

**Course:** Interactive Web Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** overlay UI  
**Board first:** html overlay on canvas

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

1. Position HTML over canvas.
2. pointer-events.
3. Keep HUD in DOM for a11y.
4. One source of camera state.
5. Don't duplicate hit-tests unsynced.

---

## 1. HUD

Configurators: WebGL + DOM labels. This week 2D canvas + HTML.

## 2. pointer-events

none on overlay except controls.

## 3. State

One object. Same as Modern JS Week 13.

## Live coding (60 min)

Canvas scene + HTML button that adds a shape.

---

## Lab

1. SVG overlay extra.
2. a11y: button not only canvas click.

---

## Homework

1. Written: why HUD in DOM.
2. Code: overlay.

---

## Quiz (10 min)

1. pointer-events none (3)
2. why DOM HUD (4)
3. one state (3)

## Snippet

```css
.hud { position: absolute; inset: 0; pointer-events: none; }
.hud button { pointer-events: auto; }
```

---

## Common mistakes

- all UI painted in canvas with no keyboard.

---

## Board drawings

1. Sandwich.

