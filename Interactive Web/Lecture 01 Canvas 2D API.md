# Lecture 1 — Canvas 2D API

**Week 1 of 15** · Interactive Web Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** getContext, paths  
**Success check:** getContext('2d').

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `Interactive Web/code/01-canvas.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: getContext, paths | Invariant: time is rAF; input is events; draw is a function`

## Board at the end (they photograph this)

```
beginPath moveTo lineTo stroke
Path.
State stack.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** A drawing API. Not a renderer with a z-buffer.

**Ask:** getContext('2d')? Wait seven seconds. Take two answers.

**Board:** parked strip. Then beginPath moveTo lineTo stroke.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *getContext, paths*.

**Do not:** WebGL + 2d on one canvas.

### Minutes 8–12 — Frame

**Say:** Today’s question: getContext, paths. Kernel: getContext, paths. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: WebGL + 2d on one canvas.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** A drawing API. Not a renderer with a z-buffer.

**Say:** State. fillStyle, lineWidth.

**Say:** DPI. backing store vs CSS.

**Ask:** getContext('2d')? Wait seven seconds. Take two answers.

**They do:** On paper: smiley.

**Do not:** start with Three.js. Canvas 2D is the kernel.

### Minutes 35–50 — Show

**Say:** Live demo: House from paths; then a circle arc.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** smiley.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: smiley.; save/restore color bug fix.. Homework: Written: ImageData vs path API.; Code: flag.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: getContext, paths | Plant the first common mistake. |
| 10–30 | House from paths; then a circle arc. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. getContext 2d (2)
2. save restore (4)
3. two contexts (4)


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

**1. A drawing API.** Not a renderer with a z-buffer. Immediate-ish mode. CG I uses ImageData; this week is the 2D path API.

**2. State.** fillStyle, lineWidth. save/restore stacks.

**3. DPI.** backing store vs CSS. Same bug as CG I Week 1.

---

## Common mistakes

1. WebGL + 2d on one canvas.
2. 0×0 canvas.

## If we run long, cut

DPI

## If we run short, add

save/restore color bug fix.
