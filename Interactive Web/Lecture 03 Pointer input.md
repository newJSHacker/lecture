# Lecture 3 — Pointer input

**Week 3 of 15** · Interactive Web Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** map clientX/Y through getBoundingClientRect onto the backing store; Pointer Events  
**Success check:** they drag a circle that tracks the pointer when CSS size ≠ canvas.width

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `Interactive Web/code/03-pointer.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: the click lands on the path | Invariant: CSS pixels are not canvas pixels until you scale; listen, don’t poll`

## Board at the end (they photograph this)

```
const r = canvas.getBoundingClientRect();
x = (ev.clientX - r.left) * canvas.width  / r.width;
y = (ev.clientY - r.top)  * canvas.height / r.height;

pointerdown / move / up     setPointerCapture
clientX as a pixel index    =  fail
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** A geometry visualizer is a drag. WebGL picking later is the same mapping idea. If they use clientX as a backing-store index, every HiDPI or CSS-scaled canvas lies.

**Ask:** If the canvas is drawn 640 wide but CSS-styled to 320px, where is a click at the right edge in canvas space? Wait. Want: ~640, not 320.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *offset, buttons, touch*.

**Do not:** Using clientX as pixel index.

### Minutes 10–12 — Frame

**Say:** Pointer Events unify mouse and touch. Capture so drag is not lost. preventDefault on contextmenu if a right-drag is the lab. Hit-test: distance to circle centers.

**Ask:** Why setPointerCapture on down?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Bounding rect + scale. Write the two lines every time until they are muscle.

**Board:** client vs canvas. Circle the multiply by width/r.width.

**Say:** Dragging is down → move (if captured) → up. CG visualizer pattern.

**Ask:** offsetX vs the rect formula — when does offsetX lie? (CSS / border teaching-level.)

**They do:** On paper: hit two circles — formula for ‘which disk contains (x,y)’.

**Do not:** Start with Three.js. Canvas 2D is the kernel.

### Minutes 35–50 — Show

**Say:** Drag a circle. Right-click prevent menu if needed. Demo Interactive Web/code/03-pointer.html. Plant clientX as pixel index. Stretch the CSS and show the miss, then the scale fix.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Hit two circles. Multitouch extra if the first mapping works. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: hit two circles; multitouch extra. Homework: client vs canvas; drag. Quiz: bounding rect, pointer vs mouse, capture.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | dots at clientX | Plant. Stretch CSS. Miss. |
| 10–30 | rect scale mapping | They match 03-pointer.html. |
| 30–45 | drag + capture | Plant lost drag off canvas. |
| 45–60 | They hit two circles | Circulate. |

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

None this meeting.


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

_none_

---

## Common mistakes

1. using clientX as pixel index.
2. no capture, drag lost.

## If we run long, cut

Multitouch. Keep mapping + one drag.

## If we run short, add

Hit two circles.
