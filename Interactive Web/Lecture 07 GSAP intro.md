# Lecture 7 — GSAP intro

**Week 7 of 15** · Interactive Web Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** tweens, timelines  
**Success check:** A tween.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `Interactive Web/code/09-gsap.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: tweens, timelines | Invariant: time is rAF; input is events; draw is a function`

## Board at the end (they photograph this)

```
gsap.to(el,{x:80})
Timeline.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** Why a library. Timelines beat ad-hoc rAF for UI stories.

**Ask:** A tween? Wait seven seconds. Take two answers.

**Board:** parked strip. Then gsap.to(el,{x:80}).

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *tweens, timelines*.

**Do not:** GSAP for every pixel of a renderer.

### Minutes 10–12 — Frame

**Say:** Today’s question: tweens, timelines. Kernel: tweens, timelines. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: GSAP for every pixel of a renderer.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Why a library. Timelines beat ad-hoc rAF for UI stories.

**Say:** GSAP. Industry UI.

**Say:** Bundle. Know the cost.

**Ask:** A tween? Wait seven seconds. Take two answers.

**They do:** On paper: Stagger extra.

**Do not:** start with Three.js. Canvas 2D is the kernel.

### Minutes 35–50 — Show

**Say:** Live demo: A 3-step timeline: fade, move, color.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Stagger extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Stagger extra.; Respect reduced motion: skip timeline.. Homework: Written: when not to GSAP.; Code: timeline.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: tweens, timelines | Plant the first common mistake. |
| 10–30 | A 3-step timeline: fade, move, color. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. tween vs timeline (4)
2. kill (3)
3. CSS enough? (3)


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

**1. Why a library.** Timelines beat ad-hoc rAF for UI stories. Games still need a loop.

**2. GSAP.** Industry UI. Course: 2 weeks of taste, not certification.

**3. Bundle.** Know the cost. Prefer CSS if one hover.

---

## Common mistakes

1. GSAP for every pixel of a renderer.
2. no reduced motion.

## If we run long, cut

Bundle

## If we run short, add

Respect reduced motion: skip timeline.
