# Lecture 6 — glTF loading

**Week 6 of 15** · Three.js Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** GLTFLoader from vendor/jsm; traverse for shadows; scale; DRACO as a name  
**Success check:** they load a local glb (or the 10-gltf-pattern stand-in), traverse castShadow, and show an error UI on failure

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `ThreeJS Development/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: a model that is a graph | Invariant: gltf.scene is a Group; load once, not in rAF; no Sketchfab hotlink without credit`

## Board at the end (they photograph this)

```
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js'
// addons → ThreeJS/vendor/jsm/     no CDN

loader.load('m.glb', (g) => scene.add(g.scene))
traverse: if (o.isMesh) o.castShadow = true
Box3.setFromObject → center / scale

DRACO   (name)   file:// fails → serve
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** Blender exports this. Demo 10-gltf-pattern.html uses local vendor. If the glTF viewer is wrong, the engine is not the bug — that sentence is the Blender course; today we still check scale.

**Ask:** Do you loader.load inside the animation loop? Wait. Want: no.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *GLTFLoader, scale, shadows*.

**Do not:** Hotlinking huge sketchfab without credit.

### Minutes 10–12 — Frame

**Say:** Loading manager + placeholder cube. Error UI. DRACO name, not a lab install. License on any third-party glb.

**Ask:** Who is gltf.scene — a Mesh or a Group?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Format. One glb vs gltf+bin+png.

**Board:** load, add g.scene, traverse.

**Say:** Box3 center. Shadows need traverse.

**Ask:** Why traverse for castShadow?

**They do:** On paper: the load callback three lines.

**Do not:** Treat the inspector as the renderer. Load Three from a CDN.

### Minutes 35–50 — Show

**Say:** Load pattern from 10-gltf-pattern.html. Plant CDN GLTFLoader. Plant load in rAF. Plant huge Sketchfab without credit.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Error UI on 404 glb. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: error UI; box3 center. Homework: why glTF; load. Quiz: who is scene, traverse, load in rAF?.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | importmap vendor + addons | Plant CDN. |
| 10–30 | load + add scene | Plant adding gltf not gltf.scene. |
| 30–45 | traverse shadows | Forgot isMesh. |
| 45–60 | They error-UI | Circulate. Serve. |

Point them at `ThreeJS Development/code/` as the after-class check, not as the lecture.

---

## Lab

1. error UI.
2. box3 center.

---

## Homework

1. Written: why glTF.
2. Code: load.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
loader.load('m.glb', (g) => scene.add(g.scene));
```

---

## Extra exercises

See [[ThreeJS Development/exercises/Week 06]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. hotlinking huge sketchfab without credit.
2. loading every frame.

## If we run long, cut

DRACO decode internals. Keep load + traverse + serve.

## If we run short, add

Box3 center / scale to meters.
