# Lecture 10 — Optimization as a method

**Week 10 of 15** · Advanced Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** profile → cut → measure on a named device; before row required  
**Success check:** they can show a two-row table (before/after) without a fantasy fps

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `Advanced Computer Graphics/code/02-tracer.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: optimization as a method | Invariant: local lighting is bounce 0; GI is the rest`

## Board at the end (they photograph this)

```
before  |  device  |  spp or dt or lights  |  (fps only if measured)
after   |  same    |  the cut              |

algorithm cuts: BVH, roulette, tile cull
asset cuts:  resolution, instances
a cut that changes the image needs a screenshot
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** Advanced CG is also engineering. Same rule as RTR: measure or omit. Optimizing without a before row fails. Fantasy 200 fps fails. Heavier scene: tracer spp, volume steps, or lights.

**Ask:** If you have no before row, did you optimize? Wait. Want: you guessed.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *profile, cut, measure*.

**Do not:** Optimizing without a before row.

### Minutes 10–12 — Frame

**Say:** Paper vs product: screenshot if the image changes. BVH from geometry course as a named cut.

**Ask:** What is an algorithm cut vs an asset cut?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Method. Before first.

**Board:** two-row table. Empty fps if unmeasured.

**Say:** One algorithm cut or one asset cut today — named.

**Ask:** Why screenshot a cut that changes the image?

**They do:** Empty two-row table; they fill device + metric.

**Do not:** Start with a production path tracer.

### Minutes 35–50 — Show

**Say:** Two-row table on a named device. Plant no before. Plant 200 fps. One cut.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Fill before row for their scene. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: one algorithm cut; one asset cut. Homework: table. Quiz: before row, measure-or-omit, screenshot.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Before row | Plant no baseline. |
| 15–40 | One named cut | Plant 200 fps. |
| 40–55 | After still / number | They write device. |
| 55–60 | Screenshot if image changed | Circulate. |

Point them at `Advanced Computer Graphics/code/02-tracer.html` as the after-class check, not as the lecture.

---

## Lab

1. one algorithm cut.
2. one asset cut.

---

## Homework

1. Written: what you would not cut.
2. table.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Extra exercises

See [[Advanced Computer Graphics/exercises/Week 10]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. optimizing without a before row.
2. fantasy 200 fps.

## If we run long, cut

Paper vs product sermon. Keep two rows.

## If we run short, add

One asset cut.
