# Lecture 6 — Lights and cameras

**Week 6 of 15** · Blender for Real-Time Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** Sun ≈ directional; Area vs Point; one key light; camera FOV → PerspectiveCamera  
**Success check:** they add Sun and Area, can disable extras, and map sun to DirectionalLight

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `Blender/code/03-budget.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: lights that have engine names | Invariant: preview in Eevee / Material Preview; Cycles caustics are not the goal; no invented exposure numbers as fps`

## Board at the end (they photograph this)

```
Sun    ≈  DirectionalLight
Point  ≈  PointLight
Spot   ≈  SpotLight
Area   ≈  RectAreaLight (name)

one key light     disable extras to debug

camera 35–50 mm product     →  PerspectiveCamera.fov
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** Real-time vs Cycles: we preview what a game-ish engine can do. Lighting with emission meshes only is not PBR. ISO 6400 noise is not a style goal.

**Ask:** Sun in Blender maps to which Three.js light? Wait. Want: DirectionalLight.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *area vs sun; exposure*.

**Do not:** Lighting with emission meshes only and calling it PBR.

### Minutes 10–12 — Frame

**Say:** Why one key light. FOV vs dolly extra. Turntable screenshot for homework. Exposure named; do not invent device fps.

**Ask:** Why one key light when debugging a material?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Light type table. Same names in Three.js.

**Board:** sun vs point. Camera mm → fov.

**Say:** Disable extras. The material becomes readable.

**Ask:** Does an Area light become a directional in glTF punctual lights?

**They do:** On paper: three light types and Three.js names.

**Do not:** Model at unknown scale. Skip apply rotation.

### Minutes 35–50 — Show

**Say:** Sun + Area on the crate; disable extras. Plant emission-only lighting. Plant ISO-as-style.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Disable extra lights. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: disable extras; FOV vs dolly extra. Homework: sun vs point in Three.js; turntable screenshot. Quiz: sun maps to, why one key, fov.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Sun as key | Plant 8 area lights. |
| 10–30 | Area fill | They see softness as a name. |
| 30–45 | Camera 50 mm | Plant 8 mm cartoon. |
| 45–60 | They disable extras | Circulate. |

Point them at `Blender/code/03-budget.html` as the after-class check, not as the lecture.

---

## Lab

1. Disable extra lights.
2. FOV vs dolly extra.

---

## Homework

1. Written: sun vs point in Three.js.
2. Turntable screenshot.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```
Light → Sun  |  Camera → 50 mm
```

---

## Extra exercises

See [[Blender/exercises/Week 06]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Lighting with emission meshes only and calling it PBR.
2. ISO 6400 noise as style.

## If we run long, cut

Cycles caustics. Keep type table + one key.

## If we run short, add

FOV vs dolly extra.
