# Lecture 3 — Materials and geometries

**Week 3 of 15** · Three.js Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** BoxGeometry / Sphere / Plane; MeshBasicMaterial vs MeshStandardMaterial  
**Success check:** they can say Basic is unlit, Standard needs lights, and dispose geometry they recreate in a loop

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `ThreeJS Development/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: three meshes, two lighting models | Invariant: geometry is the VBO; material is the program + uniforms; leaking geo is a VRAM leak`

## Board at the end (they photograph this)

```
Geometry  →  attributes (position, normal, uv)
Material  →  program + uniforms
Mesh      →  draw call

Basic     unlit / debug
Standard  PBR-ish  (needs light + later env)

geo.dispose()  if you replace it in a loop
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** Last week the cube was a Mesh. Today we split geometry and material. Demo 04-materials.html. ShaderMaterial is the shader course — name only.

**Ask:** Why is a Standard cube black? Wait. Want: no light (or metal+no env, later).

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *BoxGeometry, Standard vs Basic*.

**Do not:** Leaking geometries in a loop.

### Minutes 10–12 — Frame

**Say:** Share one BoxGeometry across meshes. Wireframe toggle. Standard metalness/roughness knobs. Do not leak new BoxGeometry every frame.

**Ask:** Is Standard physically correct PBR?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Basic = unlit debug. Standard = lit.

**Board:** three meshes, three materials.

**Say:** dispose. Custom ShaderMaterial parked.

**Ask:** What GPU object is Geometry?

**They do:** On paper: Basic vs Standard one sentence each.

**Do not:** Treat the inspector as the renderer. Load Three from a CDN.

### Minutes 35–50 — Show

**Say:** Three meshes, three materials. Demo 04-materials.html. Plant new Geometry in rAF. Plant Standard with no light.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** wireframe toggle. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: wireframe; shared geometry. Homework: Basic vs Standard; trio. Quiz: unlit material, dispose, Standard is PBR?.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Box Sphere Plane | Same scene. |
| 10–30 | Basic vs Standard | Plant no light. |
| 30–45 | dispose plant | Loop leak. |
| 45–60 | They share geometry | Circulate. |

Point them at `ThreeJS Development/code/` as the after-class check, not as the lecture.

---

## Lab

1. wireframe toggle.
2. shared geometry.

---

## Homework

1. Written: Basic vs Standard.
2. Code: trio.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
new THREE.MeshStandardMaterial({ color: 0x8899aa, metalness: 0.1, roughness: 0.6 });
```

---

## Extra exercises

See [[ThreeJS Development/exercises/Week 03]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. leaking geometries in a loop.

## If we run long, cut

ShaderMaterial. Keep Basic vs Standard.

## If we run short, add

Shared geometry, two materials.
