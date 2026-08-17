# Lecture 13 — Debug and a mini engine

**Week 13 of 15** · WebGL Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** black-screen 10-point checklist; a 40-line renderer, not Engine.js  
**Success check:** they can walk the checklist on a black screen and map Mesh → program/VAO/M/draw

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 12 (10 min, paper or LMS).
- Demo: `WebGL Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 13 | Goal: debug, then a mini engine | Invariant: abstraction after a cube; a 500-line engine with no cube is failure`

## Board at the end (they photograph this)

```
1 canvas size   2 compile+link   3 camera looks
4 near plane    5 winding/cull   6 depth
7 attribs       8 texture ready  9 clear   10 uniforms

debug: n as color · uv as color · depth gray

Mesh → bind program, VAO, u_p u_v u_m, draw
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 12 quiz. Mark one item together. Then:

**Say:** The 10-point list in WebGL/01 Conventions is the course. Mini engine: program, mesh, camera, light. Next course is Three.js — homework is a name map, not a rewrite.

**Ask:** Name one black-screen cause. Wait. Take three.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *checklist, abstraction*.

**Do not:** 500-line Engine.js with no cube.

### Minutes 10–12 — Frame

**Say:** Debug key modes: 1 n, 2 uv, 3 depth. README how to serve. Do not start the Three.js project tonight.

**Ask:** Three.js Mesh is which WebGL objects?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Walk the checklist on a planted black screen.

**Board:** ten items. Then Mesh → draw.

**Say:** 40-line renderer drawing two meshes. Not 500 lines.

**Ask:** Why is texture async on the checklist?

**They do:** On paper: the ten items from memory.

**Do not:** Wrap the first triangle in Three.js. Unfreeze conventions.

### Minutes 35–50 — Show

**Say:** A 40-line renderer, two meshes. Plant a 500-line Engine.js sketch. Plant 0×0 canvas. Read logs.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Debug-mode keys. README. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: debug keys; README. Homework: name map to Three.js; mini engine. Quiz: one black-screen cause, debug n, Mesh is?. Studio next.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Plant black screen | Walk 1–10 out loud. |
| 10–30 | 40-line two meshes | Keep it tiny. |
| 30–45 | Debug n/uv/depth keys | They toggle. |
| 45–60 | They write README serve | Circulate. No CDN. |

Point them at `WebGL Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. debug modes keys.
2. README.

---

## Homework

1. Written: name map to Three.js.
2. Code: mini engine.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
// 1 canvas size 2 compile 3 camera 4 near 5 winding 6 depth 7 attribs 8 texture 9 clear 10 uniforms
```

---

## Extra exercises

See [[WebGL Programming/exercises/Week 13]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. 500-line Engine.js with no cube.

## If we run long, cut

Full scene-graph editor. Keep checklist + 40 lines.

## If we run short, add

README: python -m http.server in WebGL/demos.
