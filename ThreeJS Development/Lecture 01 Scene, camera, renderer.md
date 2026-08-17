# Lecture 1 — Scene, camera, renderer

**Week 1 of 15** · Three.js Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** the three objects  
**Success check:** Construct Scene/PerspectiveCamera/WebGLRenderer.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `ThreeJS/demos/01-hello-cube.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: the three objects | Invariant: Three.js is an engine, not the algorithm`

## Board at the end (they photograph this)

```
scene.add(mesh)
Three boxes.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** Engine as a map. Scene is a graph.

**Ask:** Construct Scene/PerspectiveCamera/WebGLRenderer? Wait seven seconds. Take two answers.

**Board:** parked strip. Then scene.add(mesh).

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *the three objects*.

**Do not:** Starting IGWT in Three.js semester 2.

### Minutes 8–12 — Frame

**Say:** Today’s question: the three objects. Kernel: the three objects. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: starting IGWT in Three.js semester 2.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Engine as a map. Scene is a graph.

**Say:** Demos. [[08 Three.js Snippets]] · [[ThreeJS/demos/index.html]] 01.

**Say:** After WebGL. Students should point to uniforms they already wrote.

**Ask:** Construct Scene/PerspectiveCamera/WebGLRenderer? Wait seven seconds. Take two answers.

**They do:** On paper: resize handler.

**Do not:** treat the inspector as the renderer. Local vendor only.

### Minutes 35–50 — Show

**Say:** Live demo: A cube, orbit from demo 01–02.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** resize handler.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: resize handler.; color background.. Homework: Written: Scene vs WebGL program.; Code: cube.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: the three objects | Plant the first common mistake. |
| 10–30 | A cube, orbit from demo 01–02. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. three objects (3)
2. domElement (3)
3. why WebGL first (4)


## Snippet

```js
const renderer = new THREE.WebGLRenderer({ antialias: true });
```

---

## Extra exercises

See [[ThreeJS Development/exercises/Week 01]].

---

## Notes you may still need (from the outline)

**1. Engine as a map.** Scene is a graph. Camera has P and V. Renderer is the WebGL path.

**2. Demos.** [[08 Three.js Snippets]] · [[ThreeJS/demos/index.html]] 01.

**3. After WebGL.** Students should point to uniforms they already wrote.

---

## Common mistakes

1. starting IGWT in Three.js semester 2.
2. pixelRatio unbounded.

## If we run long, cut

After WebGL

## If we run short, add

color background.
