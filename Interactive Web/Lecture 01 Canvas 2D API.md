# Lecture 1 — Canvas 2D API

**Week 1 of 15** · Interactive Web Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** canvas.getContext('2d'); beginPath / moveTo / lineTo / arc / fill / stroke; save/restore  
**Success check:** they draw a path (house or smiley) and can restore fillStyle after a nested color change

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `Interactive Web/code/01-canvas.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: a first picture from paths | Invariant: Canvas 2D is a drawing API, not a z-buffer renderer; one context kind per canvas`

## Board at the end (they photograph this)

```
const ctx = canvas.getContext('2d');   // not webgl today

beginPath  moveTo  lineTo  arc  fill / stroke
save() / restore()     state stack: fillStyle, lineWidth

CSS size ≠ backing store   (DPI name)
0×0 canvas  =  nothing
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** Computer Graphics I puts pixels. This course draws paths in Canvas 2D. WebGL and Three.js are later courses — not the kernel. If getContext('2d') is a mystery, every animation week collapses.

**Ask:** What happens if you request '2d' and 'webgl' on the same canvas? Wait. Want: you don’t — one context; mixing is a plant.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *getContext, paths*.

**Do not:** WebGL + 2d on one canvas.

### Minutes 8–12 — Frame

**Say:** Immediate-ish mode: you issue draws; the bitmap is what remains. State: fillStyle, lineWidth, transform. save/restore is a stack. DPI / backing store vs CSS named — same bug as CG I week 1.

**Ask:** Does fill() consume the current path? Want: yes — next shape needs beginPath.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** A drawing API. Not a scene graph. Not Three.js.

**Board:** beginPath → move/line/arc → fill/stroke. save/restore box.

**Say:** Width/height attributes are the backing store. CSS can stretch — we name it, we may cut DPI if long.

**Ask:** Why call beginPath before a second shape?

**They do:** On paper: smiley as three arcs + a path mouth. Indent the calls.

**Do not:** Start with Three.js. Canvas 2D is the kernel.

### Minutes 35–50 — Show

**Say:** House from paths; then a circle arc. Demo Interactive Web/code/01-canvas.html. Plant 0×0 canvas. Plant fillStyle leak without restore.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Smiley. Then save/restore color bug fix. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: smiley + save/restore. Homework: ImageData vs path API; flag. Quiz: getContext 2d, save/restore, two contexts. No CDN.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | getContext('2d') + fillRect | Plant 0×0. Fix width/height. |
| 10–30 | House paths + arc | Plant missing beginPath. |
| 30–45 | save/restore fillStyle | Plant color leak. |
| 45–60 | They draw smiley | Circulate. No WebGL. |

Point them at `Interactive Web/code/01-canvas.html` as the after-class check, not as the lecture.

---

## Lab

1. smiley.
2. save/restore color bug fix.

---

## Homework

1. Written: ImageData vs path API.
2. Code: flag.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
const ctx = c.getContext('2d');
ctx.beginPath(); ctx.arc(80,80,40,0,Math.PI*2); ctx.fill();
```

---

## Extra exercises

See [[Interactive Web/exercises/Week 01]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. WebGL + 2d on one canvas.
2. 0×0 canvas.

## If we run long, cut

DPI. Keep paths + save/restore.

## If we run short, add

save/restore color bug fix as a second pass.
