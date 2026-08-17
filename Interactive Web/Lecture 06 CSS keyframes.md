# Lecture 6 — CSS keyframes

**Week 6 of 15** · Interactive Web Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** loops, steps  
**Success check:** @keyframes.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `Interactive Web/code/06-hud.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: loops, steps | Invariant: time is rAF; input is events; draw is a function`

## Board at the end (they photograph this)

```
@keyframes spin
Spinner.
sprite strip.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** Declarative motion. Loaders, idle UI.

**Ask:** @keyframes? Wait seven seconds. Take two answers.

**Board:** parked strip. Then @keyframes spin.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *loops, steps*.

**Do not:** Physics in keyframes.

### Minutes 10–12 — Frame

**Say:** Today’s question: loops, steps. Kernel: loops, steps. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: physics in keyframes.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Declarative motion. Loaders, idle UI.

**Say:** Sprite sheets. steps() + background-position.

**Say:** JS control. element.style.animationPlayState.

**Ask:** @keyframes? Wait seven seconds. Take two answers.

**They do:** On paper: Pause on hover.

**Do not:** start with Three.js. Canvas 2D is the kernel.

### Minutes 35–50 — Show

**Say:** Live demo: A spinner; then a 4-frame sprite extra.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Pause on hover.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Pause on hover.; Two animations sequenced extra.. Homework: Written: CSS vs rAF.; Code: spinner.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: loops, steps | Plant the first common mistake. |
| 10–30 | A spinner; then a 4-frame sprite extra. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Interactive Web/code/06-hud.html` as the after-class check, not as the lecture.

---

## Lab

1. Pause on hover.
2. Two animations sequenced extra.

---

## Homework

1. Written: CSS vs rAF.
2. Code: spinner.

---

## Quiz next meeting (they hear this now)

1. @keyframes (3)
2. steps (4)
3. physics in CSS? (3)


## Snippet

```css
@keyframes spin { to { transform: rotate(360deg); } }
```

---

## Extra exercises

See [[Interactive Web/exercises/Week 06]].

---

## Notes you may still need (from the outline)

**1. Declarative motion.** Loaders, idle UI. Not a physics engine.

**2. Sprite sheets.** steps() + background-position.

**3. JS control.** element.style.animationPlayState.

---

## Common mistakes

1. physics in keyframes.
2. infinite heavy filters.

## If we run long, cut

JS control

## If we run short, add

Two animations sequenced extra.
