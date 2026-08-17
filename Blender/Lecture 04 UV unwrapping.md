# Lecture 4 — UV unwrapping

**Week 4 of 15** · Blender for Real-Time Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** seams, islands, texel density; checker grid as the judge  
**Success check:** they mark seams on a crate, unwrap, pack with margin, and can read stretch on a checker

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `Blender/code/03-budget.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: islands a texture can use | Invariant: UVs are the fragment-shader map; stretch is blur; Smart UV is not a character pipeline`

## Board at the end (they photograph this)

```
seam  =  cut where the island splits
island  =  connected UV chart
checker: even squares = good; skinny = stretch

pack + margin     overlap = shared texels
texel density: same pixel size on crate faces
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** The fragment shader samples a 2D image. That is why this week exists. Lightmaps hate overlap; albedo sometimes shares trim. Do not Smart-UV a character as the only method.

**Ask:** If the checker is long rectangles, is that a 4k texture problem? Wait. Want: no — stretch in the unwrap.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *seams, islands, texel*.

**Do not:** Smart UV project on a character as the only method.

### Minutes 10–12 — Frame

**Say:** Cylinders: one side seam + caps. Pack with margin. Tiny islands / giant waste is a packing bug.

**Ask:** What is an island?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Why UVs. Seams where they hide.

**Board:** checker judgment.

**Say:** One overlap bug then fix.

**Ask:** Why a margin when packing?

**They do:** Sketch seams on a crate (six faces).

**Do not:** Model at unknown scale. Skip apply rotation.

### Minutes 35–50 — Show

**Say:** Mark seams; unwrap; checker. Plant Smart UV as the only method. Plant tiny islands.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Pack with a margin. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: pack + margin; overlap bug then fix. Homework: what a seam is; UV screenshot. Quiz: island, stretch symptom, why checker.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Checker material | Plant judging in solid view. |
| 10–30 | Seams on crate | Plant seam on the hero face. |
| 30–45 | Pack margin | Bleed named. |
| 45–60 | They fix overlap | Circulate. |

Point them at `Blender/code/03-budget.html` as the after-class check, not as the lecture.

---

## Lab

1. Pack with a margin.
2. One overlap bug then fix.

---

## Homework

1. Written: what a seam is.
2. UV screenshot.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```
U → Unwrap  |  UV editor → Pack Islands
```

---

## Extra exercises

See [[Blender/exercises/Week 04]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Smart UV project on a character as the only method.
2. Tiny islands, giant waste.

## If we run long, cut

UDIM speeches. Keep crate seams + checker.

## If we run short, add

One overlap bug then fix.
