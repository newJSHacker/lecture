# Lecture 1 — Coordinates and why math

**Week 1 of 15** · Mathematics for Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** plot a point with y flipped; `deg * Math.PI / 180`  
**Success check:** they can point at math +y up and canvas +y down on the same figure

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `Mathematics for Computer Graphics/code/01-axes.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: put a point on an axis and not lie about y | Invariant: Math.cos takes radians; canvas y is down; say it every plot`

## Board at the end (they photograph this)

```
math:     +x right, +y up
canvas:   +x right, +y down     (CG I flips in the viewport)

180° = π rad
rad = deg * Math.PI / 180

a cube is vertices; a camera is a matrix
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Optional: a canvas plot with y unflipped, labels upside-down | the bug is a photo |

---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** A cube is vertices. A camera is a matrix. This course is the algebra Computer Graphics I will spend on pictures. Today: axes, points, radians.

**Ask:** If you plot y = x on a canvas without flipping, which way does the line go? Wait.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *plot a point with y flipped; `deg * Math.PI / 180`*.

**Do not:** Degrees in cos.

### Minutes 8–12 — Frame

**Say:** High-school algebra is enough. We freeze conventions: right-handed, Y-up on paper. Canvas is the exception we name.

**Ask:** Does `Math.cos` want degrees or radians?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Graphics is numbers. Preview the CG I space chain as five boxes — do not derive P.

**Board:** two y-axes side by side. Unit circle preview (cos, sin).

**Say:** Convert on the board. Store radians in code. Degrees in `cos` is the professional disease.

**Ask:** π radians in degrees? Want: 180.

**They do:** Table: 30°, 45°, 90° → radians. Leave 45° as π/4, not a decimal they invent.

**Do not:** Start with eigenvalues. Mix row-vector formulas.

### Minutes 35–50 — Show

**Say:** Plot 8 points on a canvas with y flipped; label axes. Demo `Mathematics for Computer Graphics/code/01-axes.html`.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Distance between two points on paper, then in code. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: degree table + distance. Homework: why radians; plot y=sin(x) with the flip. Quiz: π in degrees, canvas y, point vs pixel.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Axes + one point | Plant y unflipped. |
| 15–35 | Radian conversion | Plant `Math.cos(90)`. |
| 35–50 | 8 points | Labels. |
| 50–60 | They add distance | Circulate. |

Point them at `Mathematics for Computer Graphics/code/01-axes.html` as the after-class check, not as the lecture.

---

## Lab

1. Convert 30°, 45°, 90° to radians in a table.
2. Distance between two points.

---

## Homework

1. Written: why radians.
2. Code: plot y=sin(x).

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
const rad = deg * Math.PI / 180;
```

---

## Extra exercises

See [[Mathematics for Computer Graphics/exercises/Week 01]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Degrees in cos.
2. Forgetting y-flip.

## If we run long, cut

Space-chain preview. Keep two y’s and radians.

## If we run short, add

A third axis named only.
