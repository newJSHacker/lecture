# Lecture 7 — GSAP intro

**Week 7 of 15** · Interactive Web Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** gsap.to tween; timeline sequence; local vendor file, no CDN  
**Success check:** they play a 3-step timeline from a click and skip it when reduced-motion is on

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `Interactive Web/code/09-gsap.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: one timeline you can kill | Invariant: GSAP is for UI stories; the renderer loop stays rAF; no CDN`

## Board at the end (they photograph this)

```
<script src="../vendor/gsap.min.js"></script>   /* local */

gsap.to(el, { x: 80, duration: 0.6 });
gsap.timeline().to(…).to(…).to(…);

reduced-motion  →  skip timeline
kill()  when leaving the scene
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** Timelines beat ad-hoc rAF for a three-beat UI story. Games still need week 2’s loop. Course: two weeks of taste, not certification. Loading GSAP from a CDN is a fail — vendor/gsap.min.js is in the repo.

**Ask:** If the motion is one hover lift, do you need GSAP? Wait. Want: no — CSS was week 5.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *tweens, timelines*.

**Do not:** GSAP for every pixel of a renderer.

### Minutes 10–12 — Frame

**Say:** Why a library: sequence, stagger, kill. Bundle cost: know it, do not invent KB. Reduced motion: skip. Do not tween every particle of a sim.

**Ask:** tween vs timeline in one sentence?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Local script tag. If gsap is undefined, the path is wrong — not ‘use a CDN’.

**Board:** gsap.to. Then a 3-step timeline: fade, move, color.

**Say:** Stagger extra. matchMedia reduced-motion like 09-gsap.html.

**Ask:** What does kill() prevent?

**They do:** On paper: stagger of three boxes — one timeline or three tweens?

**Do not:** Start with Three.js. Canvas 2D is the kernel.

### Minutes 35–50 — Show

**Say:** A 3-step timeline: fade, move, color. Demo Interactive Web/code/09-gsap.html (loads ../vendor/gsap.min.js). Plant a CDN URL. Remove it. Plant running the timeline when reduced-motion is on.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Stagger extra. Respect reduced motion: skip timeline. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: stagger + reduced-motion skip. Homework: when not to GSAP; timeline. Quiz: tween vs timeline, kill, CSS enough? Midterm next week: weeks 1–7.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | local vendor script | Plant CDN. Fix relative path. |
| 10–30 | 3-step timeline | Play on button, not autoplay. |
| 30–45 | reduced-motion skip | They toggle and re-click. |
| 45–60 | They stagger | Circulate. No particle GSAP. |

Point them at `Interactive Web/code/09-gsap.html` as the after-class check, not as the lecture.

---

## Lab

1. Stagger extra.
2. Respect reduced motion: skip timeline.

---

## Homework

1. Written: when not to GSAP.
2. Code: timeline.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```html
<script src="../vendor/gsap.min.js"></script>
<script>
gsap.to('.box', { x: 80, duration: 0.6 });
</script>
```

---

## Extra exercises

See [[Interactive Web/exercises/Week 07]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. GSAP for every pixel of a renderer.
2. no reduced motion.

## If we run long, cut

Bundle-size talk. Keep local GSAP + timeline + reduced-motion.

## If we run short, add

Respect reduced motion: skip timeline.
