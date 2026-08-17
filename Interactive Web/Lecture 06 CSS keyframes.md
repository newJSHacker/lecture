# Lecture 6 — CSS keyframes

**Week 6 of 15** · Interactive Web Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** @keyframes; animation-iteration; steps() for a sprite; playState from JS  
**Success check:** they write a spinner (or bounce) in CSS and can pause it on hover without a rAF loop

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `Interactive Web/code/06-hud.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: a loop the stylesheet owns | Invariant: keyframes are declarative UI motion, not a physics engine`

## Board at the end (they photograph this)

```
@keyframes spin { to { transform: rotate(360deg); } }
.spinner { animation: spin 0.8s linear infinite; }

steps(4)  +  background-position   sprite strip

el.style.animationPlayState = 'paused';
physics in keyframes  =  fail
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** Transitions are A→B. Loaders and idle UI loop. That is keyframes. A bouncing rigid body still belongs in rAF. Heavy infinite filters are a tax we will not invent numbers for — we just do not ship them.

**Ask:** Can @keyframes replace dt integration for a game? Wait. Want: no.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *loops, steps*.

**Do not:** Physics in keyframes.

### Minutes 10–12 — Frame

**Say:** Declarative motion. steps() + background-position for a 4-frame sprite extra. JS control: animationPlayState. Reduced motion still applies — 05-css.html already shows the query.

**Ask:** linear vs ease-in-out on a continuous spinner — which hides the seam?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Name the animation, attach it, decide infinite or forwards.

**Board:** @keyframes spin. Then steps(4) sprite strip.

**Say:** Pause on hover via CSS or playState. Sequence two animations extra if short.

**Ask:** Who owns time here — rAF or CSS?

**They do:** On paper: pause-on-hover rule. One selector.

**Do not:** Start with Three.js. Canvas 2D is the kernel.

### Minutes 35–50 — Show

**Say:** A spinner; then a 4-frame sprite extra. Demo Interactive Web/code/05-css.html (bounce + reduced motion). 06-hud.html is the overlay demo for week 10 — not today’s kernel.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Pause on hover. Eight minutes. Two animations sequenced extra if they finish.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: pause on hover; sequence extra. Homework: CSS vs rAF; spinner. Quiz: @keyframes, steps, physics in CSS?

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | @keyframes spin | Plant a rAF spinner ‘because we can’. |
| 10–30 | infinite + reduced-motion | Respect the query. |
| 30–45 | steps sprite extra | Plant physics in keyframes. |
| 45–60 | They pause on hover | Circulate. |

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

None this meeting.


## Snippet

```css
@keyframes spin { to { transform: rotate(360deg); } }
```

---

## Extra exercises

See [[Interactive Web/exercises/Week 06]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. physics in keyframes.
2. infinite heavy filters.

## If we run long, cut

JS playState. Keep @keyframes + infinite + reduced-motion.

## If we run short, add

Two animations sequenced extra.
