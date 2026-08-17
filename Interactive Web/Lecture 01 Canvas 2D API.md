# Lecture 1 — Canvas 2D API

**Course:** Interactive Web Development  
**Time:** 75 min lecture + 60 min live coding  
**This week:** getContext, paths  
**Board first:** beginPath moveTo lineTo stroke

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

1. getContext('2d').
2. Draw a path.
3. fill vs stroke.
4. save/restore.
5. Don't mix with WebGL context on the same canvas.

---

## 1. A drawing API

Not a renderer with a z-buffer. Immediate-ish mode. CG I uses ImageData; this week is the 2D path API.

## 2. State

fillStyle, lineWidth. save/restore stacks.

## 3. DPI

backing store vs CSS. Same bug as CG I Week 1.

## Live coding (60 min)

House from paths; then a circle arc.

---

## Lab

1. smiley.
2. save/restore color bug fix.

---

## Homework

1. Written: ImageData vs path API.
2. Code: flag.

---

## Quiz (10 min)

1. getContext 2d (2)
2. save restore (4)
3. two contexts (4)

## Snippet

```js
const ctx = c.getContext('2d');
ctx.beginPath(); ctx.arc(80,80,40,0,Math.PI*2); ctx.fill();
```

---

## Common mistakes

- WebGL + 2d on one canvas.
- 0×0 canvas.

---

## Board drawings

1. Path.
2. State stack.

