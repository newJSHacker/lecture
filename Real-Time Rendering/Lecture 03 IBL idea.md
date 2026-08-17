# Lecture 3 — IBL idea

**Week 3 of 15** · Real-Time Rendering  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** irradiance + prefiltered spec  
**Success check:** Diffuse IBL as a blurred env.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `Real-Time Rendering/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: irradiance + prefiltered spec | Invariant: a frame is a budget; name the pass`

## Board at the end (they photograph this)

```
env as the other light
Cubemap + sphere.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** Why IBL. A studio product has *environment* lighting.

**Ask:** Diffuse IBL as a blurred env? Wait seven seconds. Take two answers.

**Board:** parked strip. Then env as the other light.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *irradiance + prefiltered spec*.

**Do not:** 500MB HDR.

### Minutes 10–12 — Frame

**Say:** Today’s question: irradiance + prefiltered spec. Kernel: irradiance + prefiltered spec. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: 500MB HDR.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Why IBL. A studio product has *environment* lighting.

**Say:** Split sum. Karis.

**Say:** Cost. Cubemap size.

**Ask:** Diffuse IBL as a blurred env? Wait seven seconds. Take two answers.

**They do:** On paper: intensity slider.

**Do not:** invent fps numbers. Measure or omit.

### Minutes 35–50 — Show

**Say:** Live demo: Metallic sphere in an env; roughness 0 vs 1.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** intensity slider.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: intensity slider.; background vs lighting toggle.. Homework: Written: IBL vs dir light.; screenshot pair.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: irradiance + prefiltered spec | Plant the first common mistake. |
| 10–30 | Metallic sphere in an env; roughness 0 vs 1. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Real-Time Rendering/code/` as the after-class check, not as the lecture.

---

## Lab

1. intensity slider.
2. background vs lighting toggle.

---

## Homework

1. Written: IBL vs dir light.
2. screenshot pair.

---

## Quiz next meeting (they hear this now)

1. irradiance (3)
2. mip as roughness (4)
3. PMREM (3)


## Snippet

```js
scene.environment = env; // Three.js oracle after the picture
```

---

## Extra exercises

See [[Real-Time Rendering/exercises/Week 03]].

---

## Notes you may still need (from the outline)

**1. Why IBL.** A studio product has *environment* lighting. A single dir light is a lecture, not a catalog shot.

**2. Split sum.** Karis. Name. Implementation can be an env texture + mip LOD = roughness.

**3. Cost.** Cubemap size. Mobile.

---

## Common mistakes

1. 500MB HDR.
2. IBL without mentioning HDR.

## If we run long, cut

Cost

## If we run short, add

background vs lighting toggle.
