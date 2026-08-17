# Lecture 2 — Object3D and transforms

**Week 2 of 15** · Three.js Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** Object3D: position, quaternion/euler, scale; parent.add(child); matrixWorld is M  
**Success check:** they parent a cube, spin the parent, and can say matrixWorld is the model matrix

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `ThreeJS Development/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: a tree of transforms | Invariant: the graph multiplies M; scale −1 is a winding bug unless you mean it`

## Board at the end (they photograph this)

```
local  position  rotation  scale
world  matrixWorld  =  parent.matrixWorld * local

parent.add(child)
AxesHelper     Euler.order     gimbal named

scale −1 'to flip'  →  winding / normals talk
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** CG I scene graph with a nicer API. Demo 06-solar-system.html. matrixWorld is the M they uploaded last semester.

**Ask:** If the parent spins, does the child's position vector in local space change? Wait. Want: no — world does.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *position rotation scale*.

**Do not:** Scale -1 'to flip' without winding talk.

### Minutes 10–12 — Frame

**Say:** Euler order property. Quaternion under the hood. lookAt extra. Units: 1 = 1 meter if the Blender course did its job.

**Ask:** What is matrixWorld in WebGL?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Graph. Local vs world.

**Board:** matrixWorld product. AxesHelper.

**Say:** Plant scale −1. Faces invert. CCW from WebGL still applies.

**Ask:** Why AxesHelper this week?

**They do:** On paper: parent/child boxes and one product.

**Do not:** Treat the inspector as the renderer. Load Three from a CDN.

### Minutes 35–50 — Show

**Say:** Parent a cube to another; spin parent. Demo 06-solar-system.html. Plant scale −1 to flip.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** AxesHelper on parent and child. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: axesHelper; lookAt extra. Homework: matrixWorld is M; parent. Quiz: position units, matrixWorld, euler order.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | position.set meters | Plant 100-unit cube. |
| 10–30 | parent.add + spin | They see the orbit. |
| 30–45 | scale −1 plant | Winding talk. |
| 45–60 | They add AxesHelper | Circulate. |

Point them at `ThreeJS Development/code/` as the after-class check, not as the lecture.

---

## Lab

1. axesHelper.
2. lookAt extra.

---

## Homework

1. Written: matrixWorld is M.
2. Code: parent.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
parent.add(child);
```

---

## Extra exercises

See [[ThreeJS Development/exercises/Week 02]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. scale -1 'to flip' without winding talk.

## If we run long, cut

Full quaternion SLERP lecture. Keep graph + matrixWorld.

## If we run short, add

lookAt extra on a child.
