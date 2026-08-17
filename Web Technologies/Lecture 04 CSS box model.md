# Lecture 4 — CSS box model

**Course:** Web Technologies  
**Time:** 75 min lecture + 60 min live coding  
**This week:** margin border padding content  
**Board first:** box with four layers

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

1. Draw the box model.
2. Use box-sizing: border-box.
3. Set display block vs inline.
4. Inspect computed box in DevTools.
5. Avoid !important.

---

## 1. Everything is a box

Layout is boxes. Graphics people who skip this fight later UI overlays on WebGL canvases.

## 2. border-box

Course policy: `* { box-sizing: border-box; }` in the reset.

## 3. Cascade intro

Specificity later. This week: one stylesheet, class selectors.

## Live coding (60 min)

Color the content/padding/border/margin of one box using outlines.

---

## Lab

1. A card with padding and a border.
2. Two boxes side by side with inline-block or flex preview.

---

## Homework

1. Written: content-box vs border-box.
2. Code: a priced product card.

---

## Quiz (10 min)

1. Four layers (4)
2. What border-box includes (3)
3. Inspect where (3)

## Snippet

```css
* { box-sizing: border-box; }
```

---

## Common mistakes

- !important everywhere.
- Mixing units randomly.

---

## Board drawings

1. Box model.
2. Computed panel.

