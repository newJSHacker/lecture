# Lecture 5 — Volumes idea

**Week 5 of 15** · Advanced Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** homogeneous fog: Beer–Lambert T = exp(−σ t); emission/absorption/scatter named  
**Success check:** they can march a homogeneous fog toward a sun disk and move a density slider

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `Advanced Computer Graphics/code/02-tracer.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: transmittance along a ray | Invariant: local lighting is bounce 0; GI is the rest`

## Board at the end (they photograph this)

```
emission · absorption · scatter
T = exp(−σ t)     Beer–Lambert

Henyey–Greenstein named
OpenVDB / 3D tex inhomogeneous  ≠  week 5 required
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** Participating media: fog, smoke, clouds, SSS as a name. Homogeneous fog is the lab. OpenVDB as required fails. Inhomogeneous 3D tex as week 5 required fails.

**Ask:** If σ doubles, what happens to T? Wait. Want: it decays faster.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *emission, absorption, scatter*.

**Do not:** OpenVDB as required.

### Minutes 10–12 — Frame

**Say:** Phase function named. Height fog / volumetric lighting as realtime names. Emission extra.

**Ask:** What is scatter vs absorb?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Media. Three verbs.

**Board:** Beer–Lambert. Sun disk through fog.

**Say:** Homogeneous first. Heterogeneous next week.

**Ask:** Why is OpenVDB a cut?

**They do:** On paper: T at two σ values.

**Do not:** Start with a production path tracer.

### Minutes 35–50 — Show

**Say:** Ray march homogeneous fog toward a sun disk. Plant OpenVDB required. Density slider.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** exp(-sigma*t) along a ray. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: density slider; emission extra. Homework: Beer–Lambert. Quiz: T, three verbs, homogeneous.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Three verbs | Plant OpenVDB. |
| 15–40 | Beer–Lambert march | Plant inhomogeneous required. |
| 40–55 | Density slider | They move σ. |
| 55–60 | Emission extra if time | Circulate. |

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

None this meeting.


## Snippet

```glsl
float T = exp(-sigma * t);
```

---

## Extra exercises

See [[Advanced Computer Graphics/exercises/Week 05]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. OpenVDB as required.
2. inhomogeneous 3D tex as week 5 required.

## If we run long, cut

HG phase impl. Keep homogeneous T.

## If we run short, add

Emission extra.
