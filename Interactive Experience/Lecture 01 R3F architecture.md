# Lecture 1 — R3F architecture

**Week 1 of 15** · Interactive Experience Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** JSX in <Canvas> is a reconciler onto a Three.js graph; npm run dev  
**Success check:** they can run Vite, put a mesh in Canvas, and say this is not a new lighting model

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `Interactive Experience/code/01-hud.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: a cube in Canvas, not a 2018 CRA tutorial | Invariant: 3D and DOM are two clocks`

## Board at the end (they photograph this)

```
JSX tree  →  commit  →  Three.js graph

<Canvas>
  <mesh>
    <boxGeometry />
    <meshStandardMaterial />
  </mesh>
</Canvas>

npm run dev     not file://     no CDN
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** Three.js Development still owns the renderer math. R3F is how IGWT ships UI + 3D without two competing scene graphs. If the only interface is orbit-drag, it is a scene, not an experience — that fight starts at Canvas.

**Ask:** Is R3F a different renderer, or a reconciler onto Three.js? Wait seven seconds.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *Canvas, reconciler*.

**Do not:** CRA 2018 tutorials.

### Minutes 8–12 — Frame

**Say:** Vite, JSX, fast refresh. file:// will not load modules. Vanilla Three + DOM is allowed if they already have a scene — still two clocks. Cap dpr. No CDN.

**Ask:** Where does a <mesh> live after commit — the React tree, the GPU, or a Three.js Object3D?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Reconciler: React state commits become object graphs. Same cube as Three.js week 1: box, orbit, ambient+dir.

**Board:** JSX tree → graph. Circle Canvas. Color is a prop, not a CSS background.

**Say:** CRA 2018 tutorials are a plant. We freeze Vite. Resize is default; still cap dpr.

**Ask:** Why does file:// fail here?

**They do:** On paper: nest lights + mesh under Canvas and mark which node is Three.js.

**Do not:** Fight React state with the frame loop silently.

### Minutes 35–50 — Show

**Say:** Vite + a box. Plant a CDN three import. Fix: local package. Demo Interactive Experience/code/01-hud.html if Vite dies.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Color as a prop on the material. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: color prop + dpr cap. Homework: reconciler in eight sentences + repo. Quiz: Canvas, mesh maps to Object3D, why Vite.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Canvas + mesh | Plant CRA / CDN. |
| 10–30 | Orbit + lights | Plant missing Canvas. |
| 30–45 | dpr cap | Plant retina melt. |
| 45–60 | They set color as a prop | Circulate. No CDN. |

Point them at `Interactive Experience/code/01-hud.html` as the after-class check, not as the lecture.

---

## Lab

1. color as a prop.
2. resize is default — still cap dpr.

---

## Homework

1. Written: reconciler in 8 sentences.
2. repo.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```jsx
<Canvas camera={{ position: [0, 1, 4] }}>
  <mesh><boxGeometry/><meshStandardMaterial/></mesh>
</Canvas>
```

## Extra exercises

See [[Interactive Experience/exercises/Week 01]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. CRA 2018 tutorials.
2. no dpr cap.

## If we run long, cut

drei Html. Keep Canvas + reconciler.

## If we run short, add

Resize is default — still write the dpr cap.
