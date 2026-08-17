# Lecture 3 — HTML overlay HUD

**Course:** Interactive Experience Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** Dom, portals  
**Board first:** div over canvas; pointer events

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

1. A HUD with buttons.
2. pointer-events CSS.
3. drei Html name.
4. Don't put all text in Sprite unless needed.
5. a11y: HUD is real DOM.

---

## 1. Layers

Web Technologies pipeline: the canvas is a layer; HTML on top is the product UI.

## 2. Pointer

`pointer-events: none` on overlay except controls. 3D picking vs button clicks.

## 3. Html from drei

Pinned labels. Cost: extra DOM. Use sparingly.

## Live coding (60 min)

Price tag HUD + one mesh; button changes color.

---

## Lab

1. label that follows extra (drei Html).
2. focus visible on buttons.

---

## Homework

1. Written: why HUD is DOM.
2. app.

---

## Quiz (10 min)

1. pointer-events (4)
2. Html cost (3)
3. who gets the click (3)

## Snippet

```css
.hud { position: absolute; inset: 0; pointer-events: none; }
.hud button { pointer-events: auto; }
```

---

## Common mistakes

- all UI as WebGL text.
- overlay eating all clicks.

---

## Board drawings

1. Sandwich.

