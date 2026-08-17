# Lecture 3 — HTML overlay HUD

**Week 3 of 15** · Interactive Experience Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** HTML overlay HUD; pointer-events none except controls  
**Success check:** a button changes a mesh and the canvas still receives orbit except on the button

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `Interactive Experience/code/02-two-clocks.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: a HUD that is HTML, not WebGL text | Invariant: 3D and DOM are two clocks`

## Board at the end (they photograph this)

```
DOM HUD  (labels, buttons, focus)
   ↕  pointer-events
<canvas>  Three / R3F

.hud { position:absolute; inset:0; pointer-events:none; }
.hud button { pointer-events:auto; }
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** Web Technologies already painted this stack. The canvas is a layer; HTML on top is the product UI. All-UI-as-WebGL-text fails keyboard and labels.

**Ask:** If the overlay is inset 0, why can I not orbit? Wait. Want: it ate pointer-events.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *Dom, portals*.

**Do not:** All UI as WebGL text.

### Minutes 10–12 — Frame

**Say:** Price tag + one mesh. Button sets color through React state (clock 1). drei Html is a pin, not the whole HUD — cost is extra DOM.

**Ask:** When is drei Html the right tool vs a page HUD?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Layers. Canvas then HUD. Labels live in HTML.

**Board:** pointer-events split. Circle auto on the button.

**Say:** Focus-visible on buttons. 3D picking vs button clicks — do not mix silently.

**Ask:** Why not draw the price with a canvas texture this week?

**They do:** On paper: HUD CSS plus one button → material.color.

**Do not:** Fight React state with the frame loop silently.

### Minutes 35–50 — Show

**Say:** Price tag HUD; button recolors a mesh. Plant overlay eating all clicks. Then add pointer-events. Demo 01-hud.html.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** HUD button + orbit still works around it. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: follow-label extra; focus-visible. Homework: pointer-events paragraph. Quiz: none vs auto, why HTML HUD, focus.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Absolute HUD | Plant WebGL text. |
| 10–30 | pointer-events split | Plant overlay eating orbit. |
| 30–45 | Button → color | State clock, not useFrame. |
| 45–60 | They add focus-visible | Circulate. |

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

None this meeting.


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

_none_

---

## Common mistakes

1. all UI as WebGL text.
2. overlay eating all clicks.

## If we run long, cut

drei Html tour. Keep page HUD + pointer-events.

## If we run short, add

One pinned drei Html label, then say the cost.
