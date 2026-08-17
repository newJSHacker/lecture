# Lecture 13 — Debug and a mini engine

**Week 13 of 15** · WebGL Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** checklist, abstraction  
**Success check:** The 10-point checklist.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 12 (10 min, paper or LMS).
- Demo: `WebGL Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 13 | Goal: checklist, abstraction | Invariant: CPU fills buffers; GPU runs the shader; P*V*M; CCW`

## Board at the end (they photograph this)

```
black-screen 10 items
Checklist.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 12 quiz. Mark one item together. Then:

**Say:** Checklist. [[WebGL/01 Conventions]] and Teaching live-coding.

**Ask:** The 10-point checklist? Wait seven seconds. Take two answers.

**Board:** parked strip. Then black-screen 10 items.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *checklist, abstraction*.

**Do not:** 500-line Engine.js with no cube.

### Minutes 10–12 — Frame

**Say:** Today’s question: checklist, abstraction. Kernel: checklist, abstraction. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: 500-line Engine.js with no cube.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Checklist. [[WebGL/01 Conventions]] and Teaching live-coding.

**Say:** Engine. program, mesh, camera, light.

**Say:** Three.js. Next course.

**Ask:** The 10-point checklist? Wait seven seconds. Take two answers.

**They do:** On paper: debug modes keys.

**Do not:** wrap the first triangle in Three.js. Freeze conventions.

### Minutes 35–50 — Show

**Say:** Live demo: A 40-line renderer drawing two meshes.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** debug modes keys.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: debug modes keys.; README.. Homework: Written: name map to Three.js.; Code: mini engine.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: checklist, abstraction | Plant the first common mistake. |
| 10–30 | A 40-line renderer drawing two meshes. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. one black-screen cause (4)
2. debug n (3)
3. Three.js Mesh is? (3)


## Snippet

```js
// 1 canvas size 2 compile 3 camera 4 near 5 winding 6 depth 7 attribs 8 texture 9 clear 10 uniforms
```

---

## Extra exercises

See [[WebGL Programming/exercises/Week 13]].

---

## Notes you may still need (from the outline)

**1. Checklist.** [[WebGL/01 Conventions]] and Teaching live-coding.

**2. Engine.** program, mesh, camera, light. Project is this.

**3. Three.js.** Next course. Table of names.

---

## Common mistakes

1. 500-line Engine.js with no cube.

## If we run long, cut

Three.js

## If we run short, add

README.
