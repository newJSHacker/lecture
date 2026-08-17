# Lecture 12 — Performance

**Week 12 of 15** · Three.js Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** draw calls, instancing, LOD name  
**Success check:** Count draw calls.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `ThreeJS Development/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: draw calls, instancing, LOD name | Invariant: Three.js is an engine, not the algorithm`

## Board at the end (they photograph this)

```
stats.js
Budget.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** Budgets. Blender course polycounts.

**Ask:** Count draw calls? Wait seven seconds. Take two answers.

**Board:** parked strip. Then stats.js.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *draw calls, instancing, LOD name*.

**Do not:** Invented fps.

### Minutes 10–12 — Frame

**Say:** Today’s question: draw calls, instancing, LOD name. Kernel: draw calls, instancing, LOD name. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: invented fps.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Budgets. Blender course polycounts.

**Say:** Instancing. WebGL week 12 in engine form.

**Say:** Profiling. renderer.info.

**Ask:** Count draw calls? Wait seven seconds. Take two answers.

**They do:** On paper: pixelRatio 1 vs 2.

**Do not:** treat the inspector as the renderer. Local vendor only.

### Minutes 35–50 — Show

**Say:** Live demo: 200 meshes vs InstancedMesh; log info.render.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** pixelRatio 1 vs 2.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: pixelRatio 1 vs 2.; stats.. Homework: Written: a budget table (invented numbers forbidden — measure).; Code: instanced.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: draw calls, instancing, LOD name | Plant the first common mistake. |
| 10–30 | 200 meshes vs InstancedMesh; log info.render. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `ThreeJS Development/code/` as the after-class check, not as the lecture.

---

## Lab

1. pixelRatio 1 vs 2.
2. stats.

---

## Homework

1. Written: a budget table (invented numbers forbidden — measure).
2. Code: instanced.

---

## Quiz next meeting (they hear this now)

1. draw call (3)
2. InstancedMesh (4)
3. info.render (3)


## Snippet

```js
console.log(renderer.info.render);
```

---

## Extra exercises

See [[ThreeJS Development/exercises/Week 12]].

---

## Notes you may still need (from the outline)

**1. Budgets.** Blender course polycounts. Mobile vs desktop.

**2. Instancing.** WebGL week 12 in engine form.

**3. Profiling.** renderer.info.

---

## Common mistakes

1. invented fps.
2. 8k textures on a cube.

## If we run long, cut

Profiling

## If we run short, add

stats.
