# Lecture 6 — Grid

**Week 6 of 15** · Web Technologies  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** grid-template-columns and grid-area; a two-column page  
**Success check:** they can place header / nav / main / footer on a grid without nested flex hacks

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `Web Technologies/code/05-grid.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: a page of areas | Invariant: grid is two axes at once; flex is one`

## Board at the end (they photograph this)

```
display: grid
grid-template-columns: 1fr 3fr
grid-template-areas:
  "head head"
  "nav  main"
  "foot foot"
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** A portfolio and a configurator chrome are grids. Flex for a row; grid for the page.

**Ask:** When would you still use flex inside a grid cell? Wait. Want: the nav links.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *rows, columns, areas*.

**Do not:** Bootstrap as the lab.

### Minutes 10–12 — Frame

**Say:** fr units. Gap. Named areas optional but we use them once so they see the map.

**Ask:** 1fr 3fr means?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Two-dimensional. Rows and columns.

**Board:** areas diagram.

**Say:** Repeat() name. Auto-fit later — not required.

**Ask:** Grid vs flex in one sentence?

**They do:** On paper: label areas for a docs site.

**Do not:** Lecture HTML as a visual design tool. Use a CDN.

### Minutes 35–50 — Show

**Say:** Two-column layout. Demo 05-grid.html. Plant 1fr 1fr when they wanted sidebar.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Holy-grail: header, nav, main, footer. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: areas. Homework: grid vs flex paragraph. Quiz: fr, areas, when flex.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Columns | Plant flex-only page. |
| 15–40 | Areas | Typo in area name. |
| 40–55 | Sidebar 1fr 3fr | They see the ratio. |
| 55–60 | They place footer | Circulate. |

Point them at `Web Technologies/code/05-grid.html` as the after-class check, not as the lecture.

---

## Lab

1. Dashboard: sidebar + main.
2. Do not pull a UI kit.

---

## Homework

1. Written: flex vs grid, when.
2. Code: responsive 1-col mobile / 3-col desktop (media query preview OK).

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```css
.g { display: grid; grid-template-columns: 1fr 2fr; gap: 1rem; }
```

---

## Extra exercises

See [[Web Technologies/exercises/Week 06]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Bootstrap as the lab.
2. Grid on every span.

## If we run long, cut

Masonry. Keep 2-column + areas.

## If we run short, add

minmax() name.
