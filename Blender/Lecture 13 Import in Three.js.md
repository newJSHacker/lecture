# Lecture 13 — Import in Three.js

**Week 13 of 15** · Blender for Real-Time Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** load the glb with local GLTFLoader; scale, shadows, env; viewer already passed  
**Success check:** they load in the Three.js pattern, traverse shadows, and fix black metal with env not MeshBasicMaterial

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 12 (10 min, paper or LMS).
- Demo: `Blender/code/03-budget.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 13 | Goal: the handshake | Invariant: if the viewer was wrong, stop; if Three is black, check metal+rough+env, scale 0.01, inverted N`

## Board at the end (they photograph this)

```
Blender → .glb → viewer OK → ThreeJS/vendor GLTFLoader

scale 0.01          black metal (metal+rough, no env)
inverted normals    missing UVs     clip not exported

AxesHelper to check size
Unlit to 'fix' black  =  forbidden
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 12 quiz. Mark one item together. Then:

**Say:** This week is why the course exists. Asset → [[18 Three.js Development]] loader. Local vendor. No CDN. Do not re-export 20 times without the viewer step.

**Ask:** Black metallic crate in Three, fine in Blender preview — first hypothesis? Wait. Want: no environment on Standard.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *scale, shadows, colors*.

**Do not:** Re-exporting 20 times without the viewer step.

### Minutes 10–12 — Frame

**Say:** traverse castShadow. Y-up check. file:// vs serve. AxesHelper. Unlit as a 'fix' is a plant.

**Ask:** What does traverse do here?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Handshake. Viewer already green.

**Board:** bug list. Env.

**Say:** Shadow on a plane.

**Ask:** Why might the model be 100× too small?

**They do:** On paper: five import bugs and the fix.

**Do not:** Model at unknown scale. Skip apply rotation.

### Minutes 35–50 — Show

**Say:** Load crate.glb with vendor GLTFLoader (10-gltf-pattern.html pattern). Plant unlit fix. Plant re-export without viewer. Plant CDN.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** AxesHelper to check size. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: shadow on a plane; AxesHelper. Homework: bug you hit and the fix; URL or file:// note. Quiz: traverse, black metal cause, Y-up. Studio next.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Viewer still OK? | If not, stop. |
| 10–30 | GLTFLoader vendor | Plant CDN. |
| 30–45 | black metal → env | Plant MeshBasic. |
| 45–60 | They add AxesHelper | Circulate. Serve. |

Point them at `Blender/code/03-budget.html` as the after-class check, not as the lecture.

---

## Lab

1. Shadow on a plane.
2. AxesHelper to check size.

---

## Homework

1. Written: bug you hit and the fix.
2. URL or file:// note.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
loader.load('crate.glb', (g) => scene.add(g.scene));
```

---

## Extra exercises

See [[Blender/exercises/Week 13]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Re-exporting 20 times without the viewer step.
2. Unlit material to 'fix' black.

## If we run long, cut

Animation mixer deep dive. Keep load + env + scale.

## If we run short, add

AxesHelper to check size.
