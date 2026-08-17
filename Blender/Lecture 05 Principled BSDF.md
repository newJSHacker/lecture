# Lecture 5 — Principled BSDF

**Week 5 of 15** · Blender for Real-Time Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** Principled: Base Color, Metallic 0 or 1, Roughness; maps to MeshStandardMaterial  
**Success check:** they assign Principled and can say painted wood is metalness 0; they do not judge in solid view

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `Blender/code/03-budget.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: PBR knobs that survive glTF | Invariant: same knobs as Standard; metalness 0.4 'because it looked nice' is usually wrong`

## Board at the end (they photograph this)

```
BaseColor     Metallic 0|1     Roughness     Normal
=  MeshStandardMaterial  map / metalness / roughness / normalMap

dielectric 0     metal 1
Material Preview + HDRI     not Solid

specular workflow  =  legacy
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** Same knobs as Three.js Standard and later RTR. Students judge metal under gray clay and think PBR is broken. Preview with an HDRI.

**Ask:** Metalness of painted wood? Wait. Want: 0.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *base color, metal, roughness*.

**Do not:** Metalness 0.5 on everything.

### Minutes 10–12 — Frame

**Say:** Two materials on a crate ok. Emission as a tiny LED extra. Do not set 0.5 on everything.

**Ask:** Three.js name for Base Color?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Principled slots. Write the Three.js names beside them.

**Board:** 0 or 1 metal. Roughness meaning.

**Say:** Solid view plant. Switch to Material Preview.

**Ask:** Why is metalness 0.5 usually wrong?

**They do:** On paper: crate wood vs crate metal strip — two values.

**Do not:** Model at unknown scale. Skip apply rotation.

### Minutes 35–50 — Show

**Say:** Assign Principled; HDRI preview; map names to Standard. Plant metalness 0.5. Plant judging in solid.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Crate with two materials. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: two materials; LED extra. Homework: map to MeshStandardMaterial; blend + screenshot. Quiz: painted wood, roughness meaning, three.js names.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Principled on crate | Plant Solid view. |
| 10–30 | metal 0 vs 1 | Plant 0.5. |
| 30–45 | roughness slider | They see the highlight. |
| 45–60 | They add a second material | Circulate. |

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

None this meeting.


## Snippet

```
Principled: Base Color, Metallic, Roughness, Normal
```

---

## Extra exercises

See [[Blender/exercises/Week 05]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. metalness 0.5 on everything.
2. Judging in solid view.

## If we run long, cut

Clearcoat / sheen tour. Keep three knobs + preview.

## If we run short, add

Emission as a tiny LED extra.
