# Lecture 12 — Browser rendering pipeline

**Course:** Web Technologies  
**Time:** 75 min lecture + 60 min live coding  
**This week:** DOM CSSOM layout paint composite  
**Board first:** the six-stage stack from Course 2 advice

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

1. Name DOM, CSSOM, layout, paint, composite.
2. Force layout as a performance smell.
3. Use transform for animation preview.
4. DevTools performance name.
5. Connect to Canvas/WebGL layers.

---

## 1. How a pixel gets there

Parse HTML → DOM. CSS → CSSOM. Layout boxes. Paint. Composite layers. Same spirit as CG I's space chain: named stages.

## 2. Jank

Reading offsetWidth in a loop forces layout. Animate transform/opacity when possible.

## 3. Layers

A WebGL canvas is often its own layer. UI HTML sits on top. That is Interactive Web + R3F later.

## Live coding (60 min)

Animate a box with transform vs top/left; feel the difference (or show paint flashing).

---

## Lab

1. Paint flashing experiment.
2. One forced-layout bug in a starter to fix.

---

## Homework

1. Written: pipeline boxes.
2. Code: CSS transform animation.

---

## Quiz (10 min)

1. Order of layout and paint (4)
2. Why transform (3)
3. Name composite (3)

## Snippet

```css
.box { transform: translateX(20px); }
```

---

## Common mistakes

- Animating left/top for everything.
- No DevTools.

---

## Board drawings

1. Pipeline stack.
2. Layer sandwich.

