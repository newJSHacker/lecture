# Lecture 13 — Into Computer Graphics I

**Week 13 of 15** · Mathematics for Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** recite object → world → view → clip → NDC → pixels; p_clip = P V M p  
**Success check:** they can point at which weeks of this course sit in that chain and they do not claim they wrote a GPU

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 12 (10 min, paper or LMS).
- Demo: `Mathematics for Computer Graphics/code/10-pvm.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 13 | Goal: hand the baton to Computer Graphics I | Invariant: do not derive P today; this course supplied the algebra, CG I implements the picture`

## Board at the end (they photograph this)

```
object → world → view → clip → NDC → pixels

p_clip = P * V * M * p     (column vectors)

this course: vectors, matrices, frames, lerp, w
CG I: putPixel, raster, z-buffer
Comp Geo: orient, barycentric
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Optional: joint figure with CG I Week 1 six boxes | only if the board is full |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 12 quiz. Mark one item together. Then:

**Say:** Map: math week → CG I week. Homogeneous multiply chain. `orient` and barycentric are this course’s cross and areas.

**Ask:** Six spaces, in order? Wait. Fill slowly.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *recite object → world → view → clip → NDC → pixels; p_clip = P V M p*.

**Do not:** Claiming they already wrote a GPU.

### Minutes 10–12 — Frame

**Say:** What they implement next semester: a software rasterizer, not a GPU shrine. Three.js is not the weekly engine there.

**Ask:** Which course implements the z-buffer?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Walk the map table. Vectors → lighting. Matrices → M. Frames → camera. Lerp → attributes.

**Board:** pipeline. w of a point is 1.

**Say:** Numerical PVM on one point if the CG I kernel exists; else 3×3 affine only.

**Ask:** w of a direction?

**They do:** One-page map: math week → CG I week (start in class, finish in lab).

**Do not:** Start with eigenvalues. Mix row-vector formulas.

### Minutes 35–50 — Show

**Say:** Demo `10-pvm.html` or multiply one point on the board.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Three numerical PVM multiplies extra; the map is the lab.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Homework: six spaces; no new code required. Quiz: six spaces, w of a point, who implements z-buffer. Then studio.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–20 | Six boxes | Fill slowly. |
| 20–40 | One point through M then V | Skip deriving P. |
| 40–55 | Map table | They copy. |
| 55–60 | They write w=1 vs 0 | Circulate. |

Point them at `Mathematics for Computer Graphics/code/10-pvm.html` as the after-class check, not as the lecture.

---

## Lab

1. One-page map: math week → CG I week.
2. Three numerical PVM multiplies extra.

---

## Homework

1. Written: six spaces.
2. No new code required.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```
p_clip = P * V * M * p
```

---

## Extra exercises

See [[Mathematics for Computer Graphics/exercises/Week 13]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Claiming they already wrote a GPU.

## If we run long, cut

Numerical P. Keep the chain + map.

## If we run short, add

NDC range named as CG I’s job.
