# Lecture 11 — Post and composer

**Week 11 of 15** · Three.js Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** EffectComposer name  
**Success check:** EffectComposer.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `ThreeJS Development/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: EffectComposer name | Invariant: Three.js is an engine, not the algorithm`

## Board at the end (they photograph this)

```
render → pass → screen
Passes.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** RTR course. Bloom/HDR labs live there.

**Ask:** EffectComposer? Wait seven seconds. Take two answers.

**Board:** parked strip. Then render → pass → screen.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *EffectComposer name*.

**Do not:** Composer without understanding framebuffer.

### Minutes 10–12 — Frame

**Say:** Today’s question: EffectComposer name. Kernel: EffectComposer name. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: composer without understanding framebuffer.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** RTR course. Bloom/HDR labs live there.

**Say:** sRGB. output pass color space.

**Say:** Demo. post if any.

**Ask:** EffectComposer? Wait seven seconds. Take two answers.

**They do:** On paper: toggle composer vs raw render.

**Do not:** treat the inspector as the renderer. Local vendor only.

### Minutes 35–50 — Show

**Say:** Live demo: Composer with a cheap pass or gamma output.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** toggle composer vs raw render.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: toggle composer vs raw render.; cost sentence.. Homework: Written: extra fill rate.; Code: composer.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: EffectComposer name | Plant the first common mistake. |
| 10–30 | Composer with a cheap pass or gamma output. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `ThreeJS Development/code/` as the after-class check, not as the lecture.

---

## Lab

1. toggle composer vs raw render.
2. cost sentence.

---

## Homework

1. Written: extra fill rate.
2. Code: composer.

---

## Quiz next meeting (they hear this now)

1. RenderPass (3)
2. why not 8 passes (4)
3. output color (3)


## Snippet

```js
composer.addPass(new RenderPass(scene, camera));
```

---

## Extra exercises

See [[ThreeJS Development/exercises/Week 11]].

---

## Notes you may still need (from the outline)

**1. RTR course.** Bloom/HDR labs live there. Here: the plumbing.

**2. sRGB.** output pass color space.

**3. Demo.** post if any.

---

## Common mistakes

1. composer without understanding framebuffer.

## If we run long, cut

Demo

## If we run short, add

cost sentence.
