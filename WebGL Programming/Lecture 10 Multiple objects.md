# Lecture 10 — Multiple objects

**Week 10 of 15** · WebGL Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** scene loop, many uniforms  
**Success check:** A mesh record.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `WebGL Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: scene loop, many uniforms | Invariant: CPU fills buffers; GPU runs the shader; P*V*M; CCW`

## Board at the end (they photograph this)

```
for each mesh: bind, uniform M, draw
Loop.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** CPU loop. Three.js Object3D is this with more.

**Ask:** A mesh record? Wait seven seconds. Take two answers.

**Board:** parked strip. Then for each mesh: bind, uniform M, draw.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *scene loop, many uniforms*.

**Do not:** New program per cube.

### Minutes 10–12 — Frame

**Say:** Today’s question: scene loop, many uniforms. Kernel: scene loop, many uniforms. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: new program per cube.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** CPU loop. Three.js Object3D is this with more.

**Say:** State. bind VAO/buffer, set M, drawArrays/elements.

**Say:** Demo. 14 instancing later; this week naive loop.

**Ask:** A mesh record? Wait seven seconds. Take two answers.

**They do:** On paper: parented second cube extra.

**Do not:** wrap the first triangle in Three.js. Freeze conventions.

### Minutes 35–50 — Show

**Say:** Live demo: Three cubes different M.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** parented second cube extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: parented second cube extra.; shared geometry.. Homework: Written: why one program.; Code: loop.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: scene loop, many uniforms | Plant the first common mistake. |
| 10–30 | Three cubes different M. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `WebGL Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. parented second cube extra.
2. shared geometry.

---

## Homework

1. Written: why one program.
2. Code: loop.

---

## Quiz next meeting (they hear this now)

1. what changes per object (4)
2. compile per mesh? (3)
3. VAO name (3)


## Snippet

```js
for (const o of objects) { setM(o.m); gl.drawElements(...); }
```

---

## Extra exercises

See [[WebGL Programming/exercises/Week 10]].

---

## Notes you may still need (from the outline)

**1. CPU loop.** Three.js Object3D is this with more.

**2. State.** bind VAO/buffer, set M, drawArrays/elements.

**3. Demo.** 14 instancing later; this week naive loop.

---

## Common mistakes

1. new program per cube.
2. leaking binds.

## If we run long, cut

Demo

## If we run short, add

shared geometry.
