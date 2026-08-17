# Lecture 9 — Performance in XR

**Week 9 of 15** · Virtual and Augmented Reality  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** fill rate, foveation name  
**Success check:** Stereo is two draws or multiview name.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `XR/code/02-safety.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: fill rate, foveation name | Invariant: comfort and tracking beat extra polygons`

## Board at the end (they photograph this)

```
two views = ~2×
Two frustums.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** Cost. Two eyes.

**Ask:** Stereo is two draws or multiview name? Wait seven seconds. Take two answers.

**Board:** parked strip. Then two views = ~2×.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *fill rate, foveation name*.

**Do not:** Desktop bloom stack unchanged in VR.

### Minutes 10–12 — Frame

**Say:** Today’s question: fill rate, foveation name. Kernel: fill rate, foveation name. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: desktop bloom stack unchanged in VR.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Cost. Two eyes.

**Say:** Three.js. `renderer.xr.setFramebufferScaleFactor`.

**Say:** Quest. Documented targets.

**Ask:** Stereo is two draws or multiview name? Wait seven seconds. Take two answers.

**They do:** On paper: cut bloom in VR.

**Do not:** require a headset to pass week 1. Desktop fallback.

### Minutes 35–50 — Show

**Say:** Live demo: Scale factor 1.0 vs 0.7; note the look vs cost (headset or video).. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** cut bloom in VR.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: cut bloom in VR.; shadow map 512.. Homework: Written: stereo cost.; table.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: fill rate, foveation name | Plant the first common mistake. |
| 10–30 | Scale factor 1.0 vs 0.7; note the look vs cost (headset or video). | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `XR/code/02-safety.html` as the after-class check, not as the lecture.

---

## Lab

1. cut bloom in VR.
2. shadow map 512.

---

## Homework

1. Written: stereo cost.
2. table.

---

## Quiz next meeting (they hear this now)

1. why two views (3)
2. foveation (4)
3. scale factor (3)


## Snippet

```js
renderer.xr.setFramebufferScaleFactor(0.8);
```

---

## Extra exercises

See [[XR/exercises/Week 09]].

---

## Notes you may still need (from the outline)

**1. Cost.** Two eyes. MSAA expensive. Overdraw hurts more.

**2. Three.js.** `renderer.xr.setFramebufferScaleFactor`.

**3. Quest.** Documented targets. Student table: device, scale factor, what they cut.

---

## Common mistakes

1. desktop bloom stack unchanged in VR.
2. invented fps.

## If we run long, cut

Quest

## If we run short, add

shadow map 512.
