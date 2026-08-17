# Lecture 11 — glTF export

**Week 11 of 15** · Blender for Real-Time Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** glb, transform, extras  
**Success check:** Export .glb.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `Blender/code/02-export.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: glb, transform, extras | Invariant: units, facing, and budget travel with the asset`

## Board at the end (they photograph this)

```
File → Export → glTF 2.0
Export checklist.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** Why glTF. Khronos standard.

**Ask:** Export .glb? Wait seven seconds. Take two answers.

**Board:** parked strip. Then File → Export → glTF 2.0.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *glb, transform, extras*.

**Do not:** Exporting .blend to the web.

### Minutes 10–12 — Frame

**Say:** Today’s question: glb, transform, extras. Kernel: glb, transform, extras. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Exporting .blend to the web.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Why glTF. Khronos standard.

**Say:** Settings. +Y up.

**Say:** Validate. Load the crate in `ThreeJS/demos/10-gltf-pattern.html` (or a tiny local loader using `ThreeJS/vendor/`).

**Ask:** Export .glb? Wait seven seconds. Take two answers.

**They do:** On paper: With and without Draco extra.

**Do not:** model at unknown scale. Do not skip apply rotation.

### Minutes 35–50 — Show

**Say:** Live demo: Export the crate; view in a glTF viewer; screenshot.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** With and without Draco extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: With and without Draco extra.; Log triangle count vs blend.. Homework: Written: glb vs gltf.; The .glb in the repo (small).. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: glb, transform, extras | Plant the first common mistake. |
| 10–30 | Export the crate; view in a glTF viewer; screenshot. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Blender/code/02-export.html` as the after-class check, not as the lecture.

---

## Lab

1. With and without Draco extra.
2. Log triangle count vs blend.

---

## Homework

1. Written: glb vs gltf.
2. The .glb in the repo (small).

---

## Quiz next meeting (they hear this now)

1. glb vs gltf (3)
2. apply modifiers (3)
3. why viewer first (4)


## Snippet

```
Export glTF 2.0 → Format: glTF Binary (.glb) → +Y Up
```

---

## Extra exercises

See [[Blender/exercises/Week 11]].

---

## Notes you may still need (from the outline)

**1. Why glTF.** Khronos standard. Three.js `GLTFLoader`. One file (glb) vs json+bin+png.

**2. Settings.** +Y up. Apply modifiers. UVs. Normals. Punctual lights optional. Unused materials off.

**3. Validate.** Load the crate in `ThreeJS/demos/10-gltf-pattern.html` (or a tiny local loader using `ThreeJS/vendor/`). If it is wrong here, a website viewer will not save you. No CDN.

---

## Common mistakes

1. Exporting .blend to the web.
2. FBX as the only pipeline 'because Unity'.

## If we run long, cut

Validate

## If we run short, add

Log triangle count vs blend.
