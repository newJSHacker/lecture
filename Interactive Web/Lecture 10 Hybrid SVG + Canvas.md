# Lecture 10 — Hybrid SVG + Canvas

**Week 10 of 15** · Interactive Web Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** overlay UI  
**Success check:** Position HTML over canvas.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `Interactive Web/code/09-gsap.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: overlay UI | Invariant: time is rAF; input is events; draw is a function`

## Board at the end (they photograph this)

```
html overlay on canvas
Sandwich.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** HUD. Configurators: WebGL + DOM labels.

**Ask:** Position HTML over canvas? Wait seven seconds. Take two answers.

**Board:** parked strip. Then html overlay on canvas.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *overlay UI*.

**Do not:** All UI painted in canvas with no keyboard.

### Minutes 10–12 — Frame

**Say:** Today’s question: overlay UI. Kernel: overlay UI. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: all UI painted in canvas with no keyboard.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** HUD. Configurators: WebGL + DOM labels.

**Say:** pointer-events. none on overlay except controls.

**Say:** State. One object.

**Ask:** Position HTML over canvas? Wait seven seconds. Take two answers.

**They do:** On paper: SVG overlay extra.

**Do not:** start with Three.js. Canvas 2D is the kernel.

### Minutes 35–50 — Show

**Say:** Live demo: Canvas scene + HTML button that adds a shape.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** SVG overlay extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: SVG overlay extra.; a11y: button not only canvas click.. Homework: Written: why HUD in DOM.; Code: overlay.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: overlay UI | Plant the first common mistake. |
| 10–30 | Canvas scene + HTML button that adds a shape. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Interactive Web/code/09-gsap.html` as the after-class check, not as the lecture.

---

## Lab

1. SVG overlay extra.
2. a11y: button not only canvas click.

---

## Homework

1. Written: why HUD in DOM.
2. Code: overlay.

---

## Quiz next meeting (they hear this now)

1. pointer-events none (3)
2. why DOM HUD (4)
3. one state (3)


## Snippet

```css
.hud { position: absolute; inset: 0; pointer-events: none; }
.hud button { pointer-events: auto; }
```

---

## Extra exercises

See [[Interactive Web/exercises/Week 10]].

---

## Notes you may still need (from the outline)

**1. HUD.** Configurators: WebGL + DOM labels. This week 2D canvas + HTML.

**2. pointer-events.** none on overlay except controls.

**3. State.** One object. Same as Modern JS Week 13.

---

## Common mistakes

1. all UI painted in canvas with no keyboard.

## If we run long, cut

State

## If we run short, add

a11y: button not only canvas click.
