# Lecture 6 — Grid

**Course:** Web Technologies  
**Time:** 75 min lecture + 60 min live coding  
**This week:** rows, columns, areas  
**Board first:** 12-ish tracks, not Bootstrap required

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

1. Define columns with fr.
2. Place an item by line or area.
3. Build a 2-column layout.
4. Combine with flex inside cells.
5. Know Grid is 2D.

---

## 1. Two-dimensional layout

Magazine pages, dashboards, thesis-program sites.

## 2. fr units

`1fr 2fr` is a ratio. minmax for overflow.

## 3. Named areas

Optional. Line numbers are enough for the lab.

## Live coding (60 min)

A gallery of 6 cells; one featured spanning two columns.

---

## Lab

1. Dashboard: sidebar + main.
2. Do not pull a UI kit.

---

## Homework

1. Written: flex vs grid, when.
2. Code: responsive 1-col mobile / 3-col desktop (media query preview OK).

---

## Quiz (10 min)

1. fr meaning (3)
2. span 2 columns (4)
3. flex vs grid one sentence (3)

## Snippet

```css
.g { display: grid; grid-template-columns: 1fr 2fr; gap: 1rem; }
```

---

## Common mistakes

- Bootstrap as the lab.
- Grid on every span.

---

## Board drawings

1. Tracks.
2. Spanning cell.

