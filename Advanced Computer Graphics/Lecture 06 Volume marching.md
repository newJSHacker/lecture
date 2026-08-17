# Lecture 6 — Volume marching

**Week 6 of 15** · Advanced Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** heterogeneous regular tracking: step, sample density, accumulate; Woodcock named  
**Success check:** they can march an fBm density ball and compare two step sizes with screenshots

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `Advanced Computer Graphics/code/02-tracer.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: step size is a bias/cost choice | Invariant: local lighting is bounce 0; GI is the rest`

## Board at the end (they photograph this)

```
for t=0..far step dt:
  d = density(p)
  acc += emit * d * dt * T
  T  *= exp(−d * dt)

dt=0 is a bug
Woodcock / delta tracking     named
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** σ varies. Shadertoy clouds energy. Research cloud as the lab fails. Cost vs step size — measure stills, do not invent fps. Shadow in volume extra.

**Ask:** If dt is huge, what happens to the ball? Want: banding / missed density.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *heterogeneous, woodcock name*.

**Do not:** Research cloud as the lab.

### Minutes 10–12 — Frame

**Say:** Delta tracking unbiased for some media — name, optional code. Froxels / slice volumes named. Realtime names only.

**Ask:** What do you screenshot?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Heterogeneous. Sample density.

**Board:** the loop. Circle dt.

**Say:** Two screenshots, two dt. Honesty about bias.

**Ask:** What is Woodcock tracking in one sentence?

**They do:** Loop in words; mark where T updates.

**Do not:** Start with a production path tracer.

### Minutes 35–50 — Show

**Say:** fBm density ball; cheap emission. Plant research cloud. Plant dt=0. Two step-size stills.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** March with a dt they can name. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: two screenshots; shadow extra. Homework: dt paragraph. Quiz: regular tracking, dt, Woodcock name.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Density(p) | Plant dt=0. |
| 15–40 | Accumulate + T | Plant research cloud. |
| 40–55 | Two dt stills | No invented fps. |
| 55–60 | They compare | Circulate. |

Point them at `Advanced Computer Graphics/code/02-tracer.html` as the after-class check, not as the lecture.

---

## Lab

1. step size compare 2 screenshots.
2. shadow in volume extra.

---

## Homework

1. Written: bias vs step.
2. GLSL or JS.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```glsl
for(float t=0.; t<far; t+=dt){ float d = density(p); acc += emit*d*dt*T; T *= exp(-d*dt); }
```

---

## Extra exercises

See [[Advanced Computer Graphics/exercises/Week 06]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. research cloud as the lab.
2. dt=0.

## If we run long, cut

Realtime froxel impl. Keep march + two dt.

## If we run short, add

Shadow in volume extra.
