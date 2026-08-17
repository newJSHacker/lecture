# Lecture 6 — Grid

**Week 6 of 15** · Web Technologies  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** rows, columns, areas  
**Success check:** Define columns with fr.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `Web Technologies/code/05-grid.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: rows, columns, areas | Invariant: the browser requests, parses, then paints`

## Board at the end (they photograph this)

```
12-ish tracks, not Bootstrap required
Tracks.
Spanning cell.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** Two-dimensional layout. Magazine pages, dashboards, thesis-program sites.

**Ask:** columns with fr? Wait seven seconds. Take two answers.

**Board:** parked strip. Then 12-ish tracks, not Bootstrap required.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *rows, columns, areas*.

**Do not:** Bootstrap as the lab.

### Minutes 10–12 — Frame

**Say:** Today’s question: rows, columns, areas. Kernel: rows, columns, areas. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Bootstrap as the lab.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Two-dimensional layout. Magazine pages, dashboards, thesis-program sites.

**Say:** fr units. `1fr 2fr` is a ratio.

**Say:** Named areas. Optional.

**Ask:** columns with fr? Wait seven seconds. Take two answers.

**They do:** On paper: Dashboard: sidebar + main.

**Do not:** lecture HTML as a visual design tool. No CDN.

### Minutes 35–50 — Show

**Say:** Live demo: A gallery of 6 cells; one featured spanning two columns.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Dashboard: sidebar + main.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Dashboard: sidebar + main.; Do not pull a UI kit.. Homework: Written: flex vs grid, when.; Code: responsive 1-col mobile / 3-col desktop (media query preview OK).. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: rows, columns, areas | Plant the first common mistake. |
| 10–30 | A gallery of 6 cells; one featured spanning two columns. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. fr meaning (3)
2. span 2 columns (4)
3. flex vs grid one sentence (3)


## Snippet

```css
.g { display: grid; grid-template-columns: 1fr 2fr; gap: 1rem; }
```

---

## Extra exercises

See [[Web Technologies/exercises/Week 06]].

---

## Notes you may still need (from the outline)

**1. Two-dimensional layout.** Magazine pages, dashboards, thesis-program sites.

**2. fr units.** `1fr 2fr` is a ratio. minmax for overflow.

**3. Named areas.** Optional. Line numbers are enough for the lab.

---

## Common mistakes

1. Bootstrap as the lab.
2. Grid on every span.

## If we run long, cut

Named areas

## If we run short, add

Do not pull a UI kit.
