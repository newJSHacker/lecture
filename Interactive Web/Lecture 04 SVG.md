# Lecture 4 — SVG

**Course:** Interactive Web Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** DOM graphics, viewBox  
**Board first:** svg viewBox 0 0 100 100

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

1. svg + viewBox.
2. circle/path in DOM.
3. CSS SVG.
4. When SVG vs Canvas.
5. Don't animate 10k SVG nodes.

---

## 1. Retained vs immediate

SVG is DOM. Canvas is a bitmap. Charts vs particles.

## 2. viewBox

Coordinate system independent of CSS size.

## 3. Interop

UI overlays; icons. 3D stays Canvas/WebGL.

## Live coding (60 min)

An SVG bar chart from an array.

---

## Lab

1. Interactive hover fill.
2. export SVG extra.

---

## Homework

1. Written: SVG vs Canvas.
2. Code: chart.

---

## Quiz (10 min)

1. viewBox (4)
2. when canvas (3)
3. DOM nodes cost (3)

## Snippet

```html
<svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="40"/></svg>
```

---

## Common mistakes

- 10k SVG particles.
- no viewBox stretch mess.

---

## Board drawings

1. viewBox.
2. chart.

