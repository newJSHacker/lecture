# Lecture 4 — SVG

**Week 4 of 15** · Interactive Web Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** SVG as DOM; viewBox as the coordinate system; pick SVG vs Canvas on purpose  
**Success check:** they build a small SVG (chart or icon) with a viewBox and can say when Canvas is the better kernel

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `Interactive Web/code/04-svg.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: a graphic you can inspect in Elements | Invariant: SVG retains nodes; Canvas retains pixels; 10k SVG particles is the wrong tool`

## Board at the end (they photograph this)

```
<svg viewBox="0 0 100 100" width="200">
  <circle cx="50" cy="50" r="40"/>
</svg>

viewBox  =  user space     CSS width = paint size
Canvas   =  bitmap         SVG = DOM (hover, a11y)
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** Last week the hit was math on a bitmap. Today the hit can be a DOM node. Icons, charts, overlays: SVG. Particles and per-pixel: Canvas. We do not use SVG as a fake WebGL.

**Ask:** What does viewBox='0 0 100 100' mean if the SVG is 400px wide? Wait. Want: user unit 1 is 4 CSS px — coordinates stay 0..100.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *DOM graphics, viewBox*.

**Do not:** 10k SVG particles.

### Minutes 10–12 — Frame

**Say:** Retained vs immediate. viewBox decouples coordinates from CSS size. Interop: HUD icons later. 3D stays Canvas/WebGL next semester — name only.

**Ask:** Why is a 10k-particle sim a bad SVG?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Elements: circle, rect, polygon, text. You can addEventListener on a node.

**Board:** viewBox 0 0 100 100. Stretch without viewBox = mess.

**Say:** Bar chart from an array: createElementNS, set attributes. Namespace is not optional.

**Ask:** createElement('circle') vs createElementNS — why NS?

**They do:** On paper: hover fill — CSS :hover or a pointer listener on a rect.

**Do not:** Start with Three.js. Canvas 2D is the kernel.

### Minutes 35–50 — Show

**Say:** An SVG bar chart from an array. Demo Interactive Web/code/04-svg.html. Plant missing viewBox stretch. Plant createElement without NS (silent fail).

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Interactive hover fill. Eight minutes. Export SVG extra if short.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: hover fill; export extra. Homework: SVG vs Canvas paragraph; chart. Quiz: viewBox, when canvas, DOM node cost.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | svg + viewBox circle | Plant no viewBox, CSS stretch. |
| 10–30 | bars from array | Plant HTML namespace. |
| 30–45 | hover fill | DOM, not a pixel test. |
| 45–60 | They add one bar | Circulate. No 10k nodes. |

Point them at `Interactive Web/code/04-svg.html` as the after-class check, not as the lecture.

---

## Lab

1. Interactive hover fill.
2. export SVG extra.

---

## Homework

1. Written: SVG vs Canvas.
2. Code: chart.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```html
<svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="40"/></svg>
```

---

## Extra exercises

See [[Interactive Web/exercises/Week 04]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. 10k SVG particles.
2. no viewBox stretch mess.

## If we run long, cut

Interop lecture. Keep viewBox + one chart.

## If we run short, add

Export SVG extra (serialize or copy markup).
