# Lecture 5 — Flexbox

**Course:** Web Technologies  
**Time:** 75 min lecture + 60 min live coding  
**This week:** axis, wrap, alignment  
**Board first:** row of three cards

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

1. Set flex direction.
2. Align on main vs cross.
3. Grow/shrink/basis at teaching level.
4. Build a navbar.
5. Not to use flex for 12-column page grids (that's Grid week).

---

## 1. One-dimensional layout

Flex is a row or a column. Navbars, toolbars, HUD over a canvas.

## 2. Alignment

justify-content vs align-items. Students mix these every year — live-code both.

## 3. gap

Prefer gap over margin hacks.

## Live coding (60 min)

Navbar + three equal cards.

---

## Lab

1. Holy-grail header/main/footer with flex column on body.
2. A toolbar of buttons.

---

## Homework

1. Written: main vs cross axis.
2. Code: responsive wrap of chips.

---

## Quiz (10 min)

1. flex-direction column (2)
2. justify-content (4)
3. gap vs margin (4)

## Snippet

```css
.row { display: flex; gap: 1rem; }
```

---

## Common mistakes

- Nested flex until the page is soup.
- Absolute positioning instead of flex.

---

## Board drawings

1. Axes.
2. Navbar.

