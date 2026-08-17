# Lecture 5 — Volumes idea

**Week 5 of 15** · Advanced Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** emission, absorption, scatter  
**Success check:** Beer–Lambert absorption.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `Advanced Computer Graphics/code/02-tracer.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: emission, absorption, scatter | Invariant: local lighting is bounce 0; GI is the rest`

## Board at the end (they photograph this)

```
T = exp(-σ t); in-scatter
Ray through fog.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** Participating media. Fog, smoke, clouds, skin (SSS name).

**Ask:** Beer–Lambert absorption? Wait seven seconds. Take two answers.

**Board:** parked strip. Then T = exp(-σ t); in-scatter.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *emission, absorption, scatter*.

**Do not:** OpenVDB as required.

### Minutes 10–12 — Frame

**Say:** Today’s question: emission, absorption, scatter. Kernel: emission, absorption, scatter. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: OpenVDB as required.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Participating media. Fog, smoke, clouds, skin (SSS name).

**Say:** Phase. Henyey–Greenstein name.

**Say:** Realtime. Height fog, volumetric lighting names in games.

**Ask:** Beer–Lambert absorption? Wait seven seconds. Take two answers.

**They do:** On paper: density slider.

**Do not:** start with a production path tracer.

### Minutes 35–50 — Show

**Say:** Live demo: Ray march a homogeneous fog toward a sun disk; Beer–Lambert.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** density slider.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: density slider.; emission extra.. Homework: Written: T = exp(-σt).; demo (Canvas or shader).. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: emission, absorption, scatter | Plant the first common mistake. |
| 10–30 | Ray march a homogeneous fog toward a sun disk; Beer–Lambert. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Advanced Computer Graphics/code/02-tracer.html` as the after-class check, not as the lecture.

---

## Lab

1. density slider.
2. emission extra.

---

## Homework

1. Written: T = exp(-σt).
2. demo (Canvas or shader).

---

## Quiz next meeting (they hear this now)

1. Beer-Lambert (4)
2. scatter vs absorb (3)
3. HG name (3)


## Snippet

```glsl
float T = exp(-sigma * t);
```

---

## Extra exercises

See [[Advanced Computer Graphics/exercises/Week 05]].

---

## Notes you may still need (from the outline)

**1. Participating media.** Fog, smoke, clouds, skin (SSS name). Homogeneous fog is the lab: transmittance along a ray.

**2. Phase.** Henyey–Greenstein name. Isotropic extra.

**3. Realtime.** Height fog, volumetric lighting names in games.

---

## Common mistakes

1. OpenVDB as required.
2. inhomogeneous 3D tex as week 5 required.

## If we run long, cut

Realtime

## If we run short, add

emission extra.
