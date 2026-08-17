# Lecture 3 — Pointer input

**Week 3 of 15** · Interactive Web Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** offset, buttons, touch  
**Success check:** Map client to canvas.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `Interactive Web/code/03-pointer.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: offset, buttons, touch | Invariant: time is rAF; input is events; draw is a function`

## Board at the end (they photograph this)

```
client vs canvas coords
Mapping.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** Coordinates. getBoundingClientRect + scale to backing store.

**Ask:** Map client to canvas? Wait seven seconds. Take two answers.

**Board:** parked strip. Then client vs canvas coords.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *offset, buttons, touch*.

**Do not:** Using clientX as pixel index.

### Minutes 10–12 — Frame

**Say:** Today’s question: offset, buttons, touch. Kernel: offset, buttons, touch. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: using clientX as pixel index.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Coordinates. getBoundingClientRect + scale to backing store.

**Say:** Pointer Events. Unify mouse and touch.

**Say:** Dragging. CG geometry visualizer pattern.

**Ask:** Map client to canvas? Wait seven seconds. Take two answers.

**They do:** On paper: Multitouch extra.

**Do not:** start with Three.js. Canvas 2D is the kernel.

### Minutes 35–50 — Show

**Say:** Live demo: Drag a circle. Right-click prevent menu if needed.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Multitouch extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Multitouch extra.; Hit two circles.. Homework: Written: client vs canvas.; Code: drag.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: offset, buttons, touch | Plant the first common mistake. |
| 10–30 | Drag a circle. Right-click prevent menu if needed. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Interactive Web/code/03-pointer.html` as the after-class check, not as the lecture.

---

## Lab

1. Multitouch extra.
2. Hit two circles.

---

## Homework

1. Written: client vs canvas.
2. Code: drag.

---

## Quiz next meeting (they hear this now)

1. bounding rect (4)
2. pointer vs mouse (3)
3. capture (3)


## Snippet

```js
const r = c.getBoundingClientRect();
const x = (ev.clientX - r.left) * c.width / r.width;
```

---

## Extra exercises

See [[Interactive Web/exercises/Week 03]].

---

## Notes you may still need (from the outline)

**1. Coordinates.** getBoundingClientRect + scale to backing store.

**2. Pointer Events.** Unify mouse and touch.

**3. Dragging.** CG geometry visualizer pattern.

---

## Common mistakes

1. using clientX as pixel index.
2. no capture, drag lost.

## If we run long, cut

Dragging

## If we run short, add

Hit two circles.
