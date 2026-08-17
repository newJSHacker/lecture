# Lecture 3 — HTML overlay HUD

**Week 3 of 15** · Interactive Experience Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** Dom, portals  
**Success check:** A HUD with buttons.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `Interactive Experience/code/02-two-clocks.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: Dom, portals | Invariant: 3D and DOM are two clocks`

## Board at the end (they photograph this)

```
div over canvas; pointer events
Sandwich.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** Layers. Web Technologies pipeline: the canvas is a layer; HTML on top is the product UI.

**Ask:** A HUD with buttons? Wait seven seconds. Take two answers.

**Board:** parked strip. Then div over canvas; pointer events.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *Dom, portals*.

**Do not:** All UI as WebGL text.

### Minutes 10–12 — Frame

**Say:** Today’s question: Dom, portals. Kernel: Dom, portals. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: all UI as WebGL text.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Layers. Web Technologies pipeline: the canvas is a layer; HTML on top is the product UI.

**Say:** Pointer. `pointer-events: none` on overlay except controls.

**Say:** Html from drei. Pinned labels.

**Ask:** A HUD with buttons? Wait seven seconds. Take two answers.

**They do:** On paper: label that follows extra (drei Html).

**Do not:** fight React state with the frame loop silently.

### Minutes 35–50 — Show

**Say:** Live demo: Price tag HUD + one mesh; button changes color.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** label that follows extra (drei Html).

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: label that follows extra (drei Html).; focus visible on buttons.. Homework: Written: why HUD is DOM.; app.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: Dom, portals | Plant the first common mistake. |
| 10–30 | Price tag HUD + one mesh; button changes color. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Interactive Experience/code/02-two-clocks.html` as the after-class check, not as the lecture.

---

## Lab

1. label that follows extra (drei Html).
2. focus visible on buttons.

---

## Homework

1. Written: why HUD is DOM.
2. app.

---

## Quiz next meeting (they hear this now)

1. pointer-events (4)
2. Html cost (3)
3. who gets the click (3)


## Snippet

```css
.hud { position: absolute; inset: 0; pointer-events: none; }
.hud button { pointer-events: auto; }
```

---

## Extra exercises

See [[Interactive Experience/exercises/Week 03]].

---

## Notes you may still need (from the outline)

**1. Layers.** Web Technologies pipeline: the canvas is a layer; HTML on top is the product UI.

**2. Pointer.** `pointer-events: none` on overlay except controls. 3D picking vs button clicks.

**3. Html from drei.** Pinned labels. Cost: extra DOM. Use sparingly.

---

## Common mistakes

1. all UI as WebGL text.
2. overlay eating all clicks.

## If we run long, cut

Html from drei

## If we run short, add

focus visible on buttons.
