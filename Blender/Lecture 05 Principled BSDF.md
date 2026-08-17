# Lecture 5 — Principled BSDF

**Week 5 of 15** · Blender for Real-Time Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** base color, metal, roughness  
**Success check:** Assign Principled.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `Blender/code/03-budget.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: base color, metal, roughness | Invariant: units, facing, and budget travel with the asset`

## Board at the end (they photograph this)

```
metalness 0 or 1; roughness slider
Three spheres.
Knob table.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** PBR teaching. Same knobs as Three.js `MeshStandardMaterial` and later the RTR course.

**Ask:** Assign Principled? Wait seven seconds. Take two answers.

**Board:** parked strip. Then metalness 0 or 1; roughness slider.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *base color, metal, roughness*.

**Do not:** Metalness 0.5 on everything.

### Minutes 10–12 — Frame

**Say:** Today’s question: base color, metal, roughness. Kernel: base color, metal, roughness. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: metalness 0.5 on everything.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** PBR teaching. Same knobs as Three.js `MeshStandardMaterial` and later the RTR course.

**Say:** Metalness. Dielectric 0, metal 1.

**Say:** Preview. Material Preview vs Rendered.

**Ask:** Assign Principled? Wait seven seconds. Take two answers.

**They do:** On paper: A crate with two materials.

**Do not:** model at unknown scale. Do not skip apply rotation.

### Minutes 35–50 — Show

**Say:** Live demo: Three spheres: plastic, brushed metal, rubber. Same HDRI.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** A crate with two materials.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: A crate with two materials.; Emission as a tiny LED extra.. Homework: Written: map to MeshStandardMaterial.; Blend + screenshot.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: base color, metal, roughness | Plant the first common mistake. |
| 10–30 | Three spheres: plastic, brushed metal, rubber. Same HDRI. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Blender/code/03-budget.html` as the after-class check, not as the lecture.

---

## Lab

1. A crate with two materials.
2. Emission as a tiny LED extra.

---

## Homework

1. Written: map to MeshStandardMaterial.
2. Blend + screenshot.

---

## Quiz next meeting (they hear this now)

1. metalness of painted wood (3)
2. roughness meaning (4)
3. three.js names (3)


## Snippet

```
Principled: Base Color, Metallic, Roughness, Normal
```

---

## Extra exercises

See [[Blender/exercises/Week 05]].

---

## Notes you may still need (from the outline)

**1. PBR teaching.** Same knobs as Three.js `MeshStandardMaterial` and later the RTR course. BaseColor, Metallic, Roughness, Normal. Specular workflow is legacy.

**2. Metalness.** Dielectric 0, metal 1. 0.4 'because it looked nice' is usually wrong.

**3. Preview.** Material Preview vs Rendered. Use an HDRI for preview; students judge metal under a gray clay viewport and think PBR is broken.

---

## Common mistakes

1. metalness 0.5 on everything.
2. Judging in solid view.

## If we run long, cut

Preview

## If we run short, add

Emission as a tiny LED extra.
