# Lecture 13 — R3F teaser

**Week 13 of 15** · Three.js Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** R3F is declarative Three; same scene graph; not this course's project  
**Success check:** they can map <mesh> to Mesh/draw call and say useFrame is rAF; they do not abandon the vanilla project

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 12 (10 min, paper or LMS).
- Demo: `ThreeJS Development/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 13 | Goal: a map, not a rewrite | Invariant: JSX does not replace WebGL; wait for Interactive Experience`

## Board at the end (they photograph this)

```
<Canvas>                 WebGLRenderer + rAF
  <mesh>                 Mesh  →  draw call
    <boxGeometry />      BoxGeometry
    <meshStandardMaterial />

useFrame  ≈  the rAF callback
position={[x,y,z]}  ≈  object.position

Semester 5 · Interactive Experience
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Optional 20-line R3F cube if a bundler exists | otherwise the board is the demo |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 12 quiz. Mark one item together. Then:

**Say:** Semester 5 will do this for real. Today: the map so they are not frightened later. Do not npm-install a new stack into the week-14 project.

**Ask:** Does <mesh> skip the draw call? Wait. Want: no — it still is one.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *declarative three*.

**Do not:** Abandoning the Three.js project to start R3F overnight.

### Minutes 10–12 — Frame

**Say:** Same graph. If the lab has no bundler, stay on the board. No full app.

**Ask:** What is useFrame?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Declarative = same objects, different syntax.

**Board:** Canvas > mesh > geometry/material.

**Say:** Table: R3F prop → Object3D.

**Ask:** Why wait until semester 5?

**They do:** On paper: five-row map R3F → Three → WebGL.

**Do not:** Treat the inspector as the renderer. Load Three from a CDN.

### Minutes 35–50 — Show

**Say:** Optional 20-line R3F cube if a bundler exists; else board mapping. Plant abandoning the Three.js project overnight. No CDN.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Table: R3F prop → Object3D. No full app. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: the table; no full app. Homework: when R3F. Quiz: R3F sits on, useFrame is, why wait. Studio next.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Map Mesh → draw again | They still know it. |
| 10–30 | JSX tree on the board | No install required. |
| 30–45 | useFrame = rAF | dt still exists. |
| 45–60 | They fill the table | Circulate. Freeze vanilla project. |

Point them at `ThreeJS Development/code/` as the after-class check, not as the lecture.

---

## Lab

1. table: R3F prop → Object3D.
2. no full app.

---

## Homework

1. Written: when R3F.
2. none.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```jsx
<mesh><boxGeometry/><meshStandardMaterial/></mesh>
```

---

## Extra exercises

See [[ThreeJS Development/exercises/Week 13]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. abandoning the Three.js project to start R3F overnight.

## If we run long, cut

drei helpers tour. Keep the map.

## If we run short, add

No full app — write that on the parked strip.
