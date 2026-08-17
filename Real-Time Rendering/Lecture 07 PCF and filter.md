# Lecture 7 — PCF and filter

**Week 7 of 15** · Real-Time Rendering  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** PCF: average binary depth compares in a 3×3 kernel — still the shadow pass  
**Success check:** they can 3×3 PCF, count taps, and say why blurring the depth texture is not PCF

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `Real-Time Rendering/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: soft-looking edges on a 2D map | Invariant: PCF averages tests, not the depth values`

## Board at the end (they photograph this)

```
PASS: shadow compare  (same map as week 6)

3×3:  9 binary tests  →  average
not:  blur(depthTex) then compare once

VSM / PCSS  names only
sampler2DShadow  name
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Hard vs 3×3 edge crop | photograph |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** Percentage closer filtering: average the tests. Blurring depth and calling it PCF is the classic fail. PCSS is not the required lab. We do not invent how many ms nine taps cost.

**Ask:** If I blur the depth texture first, is that PCF? Wait. Want: no.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *tap neighbors*.

**Do not:** Blurring the depth texture and calling it PCF.

### Minutes 10–12 — Frame

**Say:** Soft-looking edges, still a 2D map. Acne can remain — say why. API: compare mode names.

**Ask:** How many taps in 3×3?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Nine samples around uv. Average 0/1.

**Board:** 3×3. Circle 'tests, not blur depth'.

**Say:** Count taps in comments. Toggle hard vs PCF.

**Ask:** Why can acne survive PCF?

**They do:** On paper: one tap vs nine — what is averaged?

**Do not:** Invent fps numbers. Measure or omit.

### Minutes 35–50 — Show

**Say:** Toggle hard vs 3×3; screenshot. Plant blur-the-depth. Do not quote fps.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Count taps in comments. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: tap count + acne sentence. Homework: PCF vs blur depth; code. Quiz: PCF, why not blur depth, tap count. Midterm next week.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Hard compare | They still have week 6. |
| 10–30 | 3×3 PCF | Plant blur depth. |
| 30–45 | Toggle + screenshot | No invented timings. |
| 45–60 | They comment 9 taps | Circulate. |

Point them at `Real-Time Rendering/code/` as the after-class check, not as the lecture.

---

## Lab

1. count taps in comments.
2. acne still possible — say why.

---

## Homework

1. Written: PCF vs blur the depth (wrong).
2. Code.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```glsl
float s=0.0; for(int i=0;i<9;i++) s += compare(uv+off[i]); s/=9.0;
```

---

## Extra exercises

See [[Real-Time Rendering/exercises/Week 07]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. blurring the depth texture and calling it PCF.
2. PCSS as required lab.

## If we run long, cut

PCSS lab. Keep 9 taps + the wrong blur.

## If we run short, add

sampler2DShadow as a name.
