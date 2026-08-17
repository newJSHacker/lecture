# Lecture 6 — Volume marching

**Week 6 of 15** · Advanced Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** heterogeneous, woodcock name  
**Success check:** Regular tracking: step, sample density.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `Advanced Computer Graphics/code/02-tracer.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: heterogeneous, woodcock name | Invariant: local lighting is bounce 0; GI is the rest`

## Board at the end (they photograph this)

```
step σ(x); accumulate
Steps inside a ball.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** Heterogeneous. σ varies.

**Ask:** Regular tracking: step, sample density? Wait seven seconds. Take two answers.

**Board:** parked strip. Then step σ(x); accumulate.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *heterogeneous, woodcock name*.

**Do not:** Research cloud as the lab.

### Minutes 10–12 — Frame

**Say:** Today’s question: heterogeneous, woodcock name. Kernel: heterogeneous, woodcock name. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: research cloud as the lab.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Heterogeneous. σ varies.

**Say:** Tracking. Delta tracking is unbiased for some media — name, optional code.

**Say:** Realtime. Slice volumes, froxels names.

**Ask:** Regular tracking: step, sample density? Wait seven seconds. Take two answers.

**They do:** On paper: step size compare 2 screenshots.

**Do not:** start with a production path tracer.

### Minutes 35–50 — Show

**Say:** Live demo: fBm density ball; cheap emission; screenshot.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** step size compare 2 screenshots.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: step size compare 2 screenshots.; shadow in volume extra.. Homework: Written: bias vs step.; GLSL or JS.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: heterogeneous, woodcock name | Plant the first common mistake. |
| 10–30 | fBm density ball; cheap emission; screenshot. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. regular tracking (3)
2. cost (4)
3. froxel (3)


## Snippet

```glsl
for(float t=0.; t<far; t+=dt){ float d = density(p); acc += emit*d*dt*T; T *= exp(-d*dt); }
```

---

## Extra exercises

See [[Advanced Computer Graphics/exercises/Week 06]].

---

## Notes you may still need (from the outline)

**1. Heterogeneous.** σ varies. Shadertoy clouds. Cost vs step size.

**2. Tracking.** Delta tracking is unbiased for some media — name, optional code.

**3. Realtime.** Slice volumes, froxels names.

---

## Common mistakes

1. research cloud as the lab.
2. dt=0.

## If we run long, cut

Realtime

## If we run short, add

shadow in volume extra.
