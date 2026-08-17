# Lecture 7 — PCF and filter

**Week 7 of 15** · Real-Time Rendering  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** tap neighbors  
**Success check:** Percentage closer filtering.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `Real-Time Rendering/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: tap neighbors | Invariant: a frame is a budget; name the pass`

## Board at the end (they photograph this)

```
3×3 compare average
9 taps.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** PCF. Average binary tests in a kernel.

**Ask:** Percentage closer filtering? Wait seven seconds. Take two answers.

**Board:** parked strip. Then 3×3 compare average.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *tap neighbors*.

**Do not:** Blurring the depth texture and calling it PCF.

### Minutes 10–12 — Frame

**Say:** Today’s question: tap neighbors. Kernel: tap neighbors. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: blurring the depth texture and calling it PCF.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** PCF. Average binary tests in a kernel.

**Say:** VSM name. Advanced CG / week later.

**Say:** API. sampler2DShadow / compare mode names.

**Ask:** Percentage closer filtering? Wait seven seconds. Take two answers.

**They do:** On paper: count taps in comments.

**Do not:** invent fps numbers. Measure or omit.

### Minutes 35–50 — Show

**Say:** Live demo: Toggle hard vs 3×3 PCF; screenshot.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** count taps in comments.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: count taps in comments.; acne still possible — say why.. Homework: Written: PCF vs blur the depth (wrong).; Code.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: tap neighbors | Plant the first common mistake. |
| 10–30 | Toggle hard vs 3×3 PCF; screenshot. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. PCF (4)
2. why not blur depth (3)
3. tap count (3)


## Snippet

```glsl
float s=0.0; for(int i=0;i<9;i++) s += compare(uv+off[i]); s/=9.0;
```

---

## Extra exercises

See [[Real-Time Rendering/exercises/Week 07]].

---

## Notes you may still need (from the outline)

**1. PCF.** Average binary tests in a kernel. Soft-looking edges, still a 2D map.

**2. VSM name.** Advanced CG / week later. Moments. Light leak.

**3. API.** sampler2DShadow / compare mode names.

---

## Common mistakes

1. blurring the depth texture and calling it PCF.
2. PCSS as required lab.

## If we run long, cut

API

## If we run short, add

acne still possible — say why.
