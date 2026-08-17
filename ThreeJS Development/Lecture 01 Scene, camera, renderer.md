# Lecture 1 — Scene, camera, renderer

**Week 1 of 15** · Three.js Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** Scene, PerspectiveCamera, WebGLRenderer; Mesh is a draw call  
**Success check:** they boot 01-hello-cube.html from ThreeJS/vendor/three.module.js and can map Mesh to program+VAO+draw

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `ThreeJS/demos/01-hello-cube.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: the three objects, mapped to WebGL | Invariant: Three.js is an engine, not the algorithm`

## Board at the end (they photograph this)

```
Scene     = graph of Object3D
Camera    = P and V     (projectionMatrix, matrixWorldInverse)
Renderer  = clear, bind programs, draw

Mesh(geometry, material)  →  one draw call
(WebGL: VAO + program + uniforms + drawArrays/elements)

import from '../vendor/three.module.js'    no CDN
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** You already wrote gl_Position = P*V*M. Today the engine hides it. If they cannot map Mesh to a draw call, they are using a magic box. Local vendor only — ThreeJS/vendor/three.module.js. Serve the ThreeJS/ folder.

**Ask:** What WebGL call is renderer.render? Wait. Want: clear, bind program, set uniforms, draw — for each mesh.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *the three objects*.

**Do not:** Starting IGWT in Three.js semester 2.

### Minutes 8–12 — Frame

**Say:** Demo 01-hello-cube.html. Standard material needs a light. Resize: setSize false, aspect, updateProjectionMatrix. pixelRatio capped at 2. outputColorSpace SRGBColorSpace.

**Ask:** Why did we do WebGL first?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Three boxes: scene, camera, renderer. Mesh is not the GPU.

**Board:** mapping table from ThreeJS/01 Scene Camera Renderer.

**Say:** import map to vendor/. file:// will fail — python -m http.server.

**Ask:** What is camera.projectionMatrix in the shader you wrote?

**They do:** On paper: Scene / Camera / Renderer / Mesh → GL names.

**Do not:** Treat the inspector as the renderer. Load Three from a CDN.

### Minutes 35–50 — Show

**Say:** Cube from 01-hello-cube.html, then orbit from 02-orbit.html. Plant CDN script tag. Plant unbounded pixelRatio. Plant no light on Standard.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** resize handler + updateProjectionMatrix. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: resize; color background. Homework: Scene vs WebGL program; cube. Quiz: three objects, domElement, why WebGL first.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | import vendor three.module.js | Plant CDN. Delete it. |
| 10–30 | 01-hello-cube | Plant Standard without light. |
| 30–45 | resize + aspect | Plant forgot updateProjectionMatrix. |
| 45–60 | They resize | Circulate. Serve ThreeJS/. |

Point them at `ThreeJS/demos/01-hello-cube.html` as the after-class check, not as the lecture.

---

## Lab

1. resize handler.
2. color background.

---

## Homework

1. Written: Scene vs WebGL program.
2. Code: cube.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
const renderer = new THREE.WebGLRenderer({ antialias: true });
```

---

## Extra exercises

See [[ThreeJS Development/exercises/Week 01]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. starting IGWT in Three.js semester 2.
2. pixelRatio unbounded.

## If we run long, cut

OrbitControls internals. Keep three objects + Mesh→draw.

## If we run short, add

scene.background color.
