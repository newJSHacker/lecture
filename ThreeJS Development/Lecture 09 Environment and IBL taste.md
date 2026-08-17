# Lecture 9 — Environment and IBL taste

**Week 9 of 15** · Three.js Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** scene.environment; PMREM name; background vs env  
**Success check:** they put a small local env on a metallic sphere and can toggle background vs environment

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `ThreeJS Development/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: IBL as a taste, not a thesis | Invariant: Standard looks like clay without an env; 500MB HDR is not a lab`

## Board at the end (they photograph this)

```
scene.environment = envTex     // lighting
scene.background  = envTex     // picture (optional)

PMREM  (name)  —  prefilter for IBL
RGBE / EXR     (names)

budget: tiny HDR or a PMREM from a cube
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** Standard needs an env to look 'PBR'. Demo 13-environment.html. Real-Time Rendering owns the integrals. Today: the knob and the cost.

**Ask:** Is scene.background the same as scene.environment? Wait. Want: no — one is the picture, one is the lighting.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *envMap, PMREM name*.

**Do not:** 500MB HDR as the lab.

### Minutes 10–12 — Frame

**Say:** RGBELoader name. PMREMGenerator name. Intensity. Do not download a 500MB HDR. Local vendor.

**Ask:** Why is a metal sphere black in a black scene?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Environment lights Standard. Background is optional wallpaper.

**Board:** two assignments. PMREM name.

**Say:** Cost: big HDR. Budget sentence, no invented fps.

**Ask:** What does PMREM stand for as a teaching expansion?

**They do:** On paper: background vs environment one line each.

**Do not:** Treat the inspector as the renderer. Load Three from a CDN.

### Minutes 35–50 — Show

**Say:** Metallic sphere in an env. Demo 13-environment.html. Plant 500MB HDR. Plant only background, no environment.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Toggle background vs env. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: toggle; intensity. Homework: env vs background; env. Quiz: environment, PMREM, budget.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | metal roughness 0.1 | Black. Plant. |
| 10–30 | environment = tex | It wakes up. |
| 30–45 | background off | They see the split. |
| 45–60 | They toggle | Circulate. Tiny HDR. |

Point them at `ThreeJS Development/code/` as the after-class check, not as the lecture.

---

## Lab

1. background vs env toggle.
2. intensity.

---

## Homework

1. Written: env vs background.
2. Code: env.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
scene.environment = envTex;
```

---

## Extra exercises

See [[ThreeJS Development/exercises/Week 09]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. 500MB HDR as the lab.

## If we run long, cut

Write a split-sum IBL. Keep env knob + budget.

## If we run short, add

envMapIntensity slider.
