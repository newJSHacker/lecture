# Lecture 11 — glTF export

**Week 11 of 15** · Blender for Real-Time Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** glTF 2.0 Binary .glb; +Y Up; apply modifiers; viewer BEFORE Three.js  
**Success check:** they export a .glb and open it in a glTF viewer (or 10-gltf-pattern.html with local vendor) before blaming Three.js

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `Blender/code/02-export.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: a file the web can load | Invariant: if it is wrong in a glTF viewer, the engine is not the bug`

## Board at the end (they photograph this)

```
glTF 2.0 Binary (.glb)     not .blend     not 'FBX because Unity'

+Y Up     Apply modifiers     UVs + normals
unused materials off     punctual lights optional

Open in a glTF viewer BEFORE Three.js
ThreeJS/demos/10-gltf-pattern.html  +  vendor/   no CDN
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** Khronos standard. One file (glb) vs json+bin+png. Checklist Blender/code/02-export.html. Validate: if the viewer is wrong, do not debug the renderer.

**Ask:** You export .blend to the web — what happens? Wait. Want: browsers do not load .blend.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *glb, transform, extras*.

**Do not:** Exporting .blend to the web.

### Minutes 10–12 — Frame

**Say:** Draco extra named. Log triangle count vs blend. FBX is not the pipeline in this course.

**Ask:** glb vs gltf in one sentence?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Why glTF. Settings from 02-export.html.

**Board:** viewer before Three.js.

**Say:** Plant FBX-only. Plant skipping the viewer.

**Ask:** Why apply modifiers on export?

**They do:** On paper: export checklist five boxes.

**Do not:** Model at unknown scale. Skip apply rotation.

### Minutes 35–50 — Show

**Say:** Export crate.glb; open viewer; then 10-gltf-pattern.html with ThreeJS/vendor/. Plant .blend upload. Plant CDN loader.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Export; write triangle count vs blend. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: with/without Draco extra; log tris. Homework: glb vs gltf; the .glb in the repo (small). Quiz: glb vs gltf, apply modifiers, why viewer first.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Export settings +Y | Plant Z-up leftover. |
| 10–30 | Viewer first | Plant jumping to Three.js. |
| 30–45 | 10-gltf-pattern local vendor | No CDN. |
| 45–60 | They log tris vs blend | Circulate. |

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

None this meeting.


## Snippet

```
Export glTF 2.0 → Format: glTF Binary (.glb) → +Y Up
```

---

## Extra exercises

See [[Blender/exercises/Week 11]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Exporting .blend to the web.
2. FBX as the only pipeline 'because Unity'.

## If we run long, cut

Every glTF extension. Keep glb + viewer-first.

## If we run short, add

Log triangle count vs blend.
