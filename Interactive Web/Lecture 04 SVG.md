# Lecture 4 — SVG

**Week 4 of 15** · Interactive Web Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** DOM graphics, viewBox  
**Success check:** svg + viewBox.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `Interactive Web/code/04-svg.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: DOM graphics, viewBox | Invariant: time is rAF; input is events; draw is a function`

## Board at the end (they photograph this)

```
svg viewBox 0 0 100 100
viewBox.
chart.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** Retained vs immediate. SVG is DOM.

**Ask:** svg + viewBox? Wait seven seconds. Take two answers.

**Board:** parked strip. Then svg viewBox 0 0 100 100.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *DOM graphics, viewBox*.

**Do not:** 10k SVG particles.

### Minutes 10–12 — Frame

**Say:** Today’s question: DOM graphics, viewBox. Kernel: DOM graphics, viewBox. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: 10k SVG particles.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Retained vs immediate. SVG is DOM.

**Say:** viewBox. Coordinate system independent of CSS size.

**Say:** Interop. UI overlays; icons.

**Ask:** svg + viewBox? Wait seven seconds. Take two answers.

**They do:** On paper: Interactive hover fill.

**Do not:** start with Three.js. Canvas 2D is the kernel.

### Minutes 35–50 — Show

**Say:** Live demo: An SVG bar chart from an array.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Interactive hover fill.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Interactive hover fill.; export SVG extra.. Homework: Written: SVG vs Canvas.; Code: chart.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: DOM graphics, viewBox | Plant the first common mistake. |
| 10–30 | An SVG bar chart from an array. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Interactive Web/code/04-svg.html` as the after-class check, not as the lecture.

---

## Lab

1. Interactive hover fill.
2. export SVG extra.

---

## Homework

1. Written: SVG vs Canvas.
2. Code: chart.

---

## Quiz next meeting (they hear this now)

1. viewBox (4)
2. when canvas (3)
3. DOM nodes cost (3)


## Snippet

```html
<svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="40"/></svg>
```

---

## Extra exercises

See [[Interactive Web/exercises/Week 04]].

---

## Notes you may still need (from the outline)

**1. Retained vs immediate.** SVG is DOM. Canvas is a bitmap. Charts vs particles.

**2. viewBox.** Coordinate system independent of CSS size.

**3. Interop.** UI overlays; icons. 3D stays Canvas/WebGL.

---

## Common mistakes

1. 10k SVG particles.
2. no viewBox stretch mess.

## If we run long, cut

Interop

## If we run short, add

export SVG extra.
