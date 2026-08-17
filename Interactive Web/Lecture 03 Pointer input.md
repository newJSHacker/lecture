# Lecture 3 — Pointer input

**Course:** Interactive Web Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** offset, buttons, touch  
**Board first:** client vs canvas coords

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

1. Map client to canvas.
2. pointerdown/move/up.
3. setPointerCapture.
4. Touch as pointer events.
5. Hit-test a circle.

---

## 1. Coordinates

getBoundingClientRect + scale to backing store.

## 2. Pointer Events

Unify mouse and touch.

## 3. Dragging

CG geometry visualizer pattern.

## Live coding (60 min)

Drag a circle. Right-click prevent menu if needed.

---

## Lab

1. Multitouch extra.
2. Hit two circles.

---

## Homework

1. Written: client vs canvas.
2. Code: drag.

---

## Quiz (10 min)

1. bounding rect (4)
2. pointer vs mouse (3)
3. capture (3)

## Snippet

```js
const r = c.getBoundingClientRect();
const x = (ev.clientX - r.left) * c.width / r.width;
```

---

## Common mistakes

- using clientX as pixel index.
- no capture, drag lost.

---

## Board drawings

1. Mapping.

