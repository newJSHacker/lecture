# Lecture 3 — IBL idea

**Week 3 of 15** · Real-Time Rendering  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** IBL: irradiance (diffuse) + prefiltered spec; mip LOD ≈ roughness  
**Success check:** they can treat a blurred env as diffuse IBL and roughness as mip, and toggle background vs lighting

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `Real-Time Rendering/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: env as the other light | Invariant: the environment is a named light; a 500MB HDR is not a lab asset`

## Board at the end (they photograph this)

```
PASS: IBL lookup  (after or with direct shade)

diffuse  ←  irradiance (blurred env)
spec     ←  prefiltered cubemap, lod = roughness

split-sum  Karis  (name)
HDR env  —  IBL without HDR is a lie
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** A studio product has environment lighting. A single dir light is a lecture, not a catalog shot. Cubemap size is a budget — we do not invent fps; we pick a small local env.

**Ask:** Is the background the same texture as the lighting? Wait. Want: often related, not always the same pass.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *irradiance + prefiltered spec*.

**Do not:** 500MB HDR.

### Minutes 10–12 — Frame

**Say:** Split-sum named. Implementation can be env + mip. PMREM is the Three.js name after the picture. Cost: cubemap resolution, especially mobile.

**Ask:** What does a higher mip mean for roughness?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Cubemap + sphere. Two arrows: irradiance, spec.

**Board:** lod = roughness. Circle HDR.

**Say:** Intensity slider is a uniform on this lookup pass.

**Ask:** Irradiance in one sentence?

**They do:** On paper: IBL vs dir light — two bullets.

**Do not:** Invent fps numbers. Measure or omit.

### Minutes 35–50 — Show

**Say:** Metallic sphere in a local env; roughness 0 vs 1. Plant 500MB HDR. Background vs lighting toggle.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Intensity slider. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: intensity + background/lighting toggle. Homework: IBL vs dir; screenshot pair. Quiz: irradiance, mip as roughness, PMREM name.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Name IBL lookups | Plant IBL without HDR. |
| 10–30 | Roughness 0 vs 1 | Plant huge HDR. |
| 30–45 | Background vs lighting | Two toggles. |
| 45–60 | They write the intensity uniform | Circulate. |

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

None this meeting.


## Snippet

```js
scene.environment = env; // Three.js oracle after the picture
```

---

## Extra exercises

See [[Real-Time Rendering/exercises/Week 03]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. 500MB HDR.
2. IBL without mentioning HDR.

## If we run long, cut

Convolve an env from scratch. Keep names + small local env.

## If we run short, add

PMREM as oracle name.
