# Lecture 10 — Post stack

**Week 10 of 15** · Real-Time Rendering  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** freeze a stack: shade HDR → shadow → bloom → tonemap → sRGB → grain/LUT  
**Success check:** they can write the order, toggle three passes, and document it in README

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `Real-Time Rendering/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: order of operations on the board | Invariant: a product shot is a named stack, not eight Instagram filters`

## Board at the end (they photograph this)

```
shade(HDR) + shadow compare
  → bloom (HDR)
  → tonemap
  → sRGB encode
  → grain
  → LUT   (last or before grain — pick)

kill switch per pass
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** Order matters. Bloom on HDR. Tonemap before 8-bit. Grain after. LUT last or before grain — pick and freeze. Undocumented order is a grading zero for the stack graph.

**Ask:** Bloom after tonemap — what did you lose? Wait. Want: leftover HDR energy.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *order of operations*.

**Do not:** Eight Instagram filters as 'RTR'.

### Minutes 10–12 — Frame

**Say:** Look-dev is a stack. Kill switches for grading and for perf. If they claim a pass is cheap, they measure next week — not today with a fantasy number.

**Ask:** What is a kill switch for?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Graph top to bottom. One box per pass.

**Board:** the frozen order. Circle bloom vs tonemap.

**Say:** Three toggles live: bloom, grain, vignette.

**Ask:** LUT in one sentence?

**They do:** On paper: their order and one why.

**Do not:** Invent fps numbers. Measure or omit.

### Minutes 35–50 — Show

**Say:** Three toggles; freeze order in README. Plant eight Instagram filters. Tiny LUT extra (16³ or 2D strip) — local file.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** One LUT extra or a screenshot matrix of toggles. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: LUT or screenshot matrix. Homework: order and why; graph figure. Quiz: tonemap vs bloom order, LUT, kill switch.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Draw the graph | Plant undocumented order. |
| 10–30 | Three kill switches | Plant Instagram soup. |
| 30–45 | README freeze | One policy. |
| 45–60 | They screenshot the matrix | Circulate. No fps. |

Point them at `Real-Time Rendering/code/` as the after-class check, not as the lecture.

---

## Lab

1. one LUT extra (tiny 16³ or 2D strip).
2. screenshot matrix.

---

## Homework

1. Written: your order and why.
2. graph figure.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```
shade(HDR) → bloom → tonemap → sRGB → grain
```

---

## Extra exercises

See [[Real-Time Rendering/exercises/Week 10]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. eight Instagram filters as 'RTR'.
2. undocumented order.

## If we run long, cut

Color-grade product. Keep named order + toggles.

## If we run short, add

Vignette as an extra named pass.
