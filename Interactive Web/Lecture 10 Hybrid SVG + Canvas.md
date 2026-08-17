# Lecture 10 — Hybrid SVG + Canvas

**Week 10 of 15** · Interactive Web Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** HTML overlay HUD on a Canvas 2D scene; pointer-events none except controls  
**Success check:** they position a labeled button over the canvas and add a shape without painting the UI in pixels

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `Interactive Web/code/09-gsap.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: a sandwich: canvas below, UI above | Invariant: HUD is DOM for keyboard and labels; the bitmap is the scene; one state object`

## Board at the end (they photograph this)

```
.stage { position: relative; }
canvas { display: block; }
.hud { position: absolute; inset: 0; pointer-events: none; }
.hud button { pointer-events: auto; }

all UI painted in canvas  =  no keyboard  =  fail
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** Configurators later are WebGL + DOM labels. This week the scene is Canvas 2D. If the score is only pixels, Tab cannot reach it. pointer-events is the sandwich.

**Ask:** If the overlay is inset 0 and pointer-events is auto, can you drag the canvas? Wait. Want: no — the HUD ate the hits.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *overlay UI*.

**Do not:** All UI painted in canvas with no keyboard.

### Minutes 10–12 — Frame

**Say:** HUD: position absolute over the canvas. none on the overlay, auto on controls. SVG overlay extra is the same sandwich. State: one object, same as Modern JS week 13.

**Ask:** Why is a <button> better than a canvas hit-rect for ‘Add shape’?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Two clocks: DOM events and rAF. One state. The button writes state; the loop draws it.

**Board:** sandwich. pointer-events none / auto.

**Say:** a11y: do not ship canvas-only UI. Week 11 will add audio on a gesture — also a DOM control.

**Ask:** Who owns the score text — ctx.fillText or a DOM node?

**They do:** On paper: SVG overlay extra — same absolute layer, pointer-events.

**Do not:** Start with Three.js. Canvas 2D is the kernel.

### Minutes 35–50 — Show

**Say:** Canvas scene + HTML button that adds a shape. Demo Interactive Web/code/06-hud.html. Plant all UI in fillText. Plant overlay blocking pointer mapping from week 3.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** SVG overlay extra. a11y: button, not only canvas click. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: SVG overlay + button. Homework: why HUD in DOM; overlay. Quiz: pointer-events none, why DOM HUD, one state.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | relative stage + overlay | Plant overlay eating clicks. |
| 10–30 | button adds a shape | State++, loop draws. |
| 30–45 | pointer-events none/auto | They drag canvas again. |
| 45–60 | They replace fillText score with DOM | Circulate. |

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

None this meeting.


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

_none_

---

## Common mistakes

1. all UI painted in canvas with no keyboard.

## If we run long, cut

State sermon. Keep sandwich + one button.

## If we run short, add

a11y: button not only canvas click.
