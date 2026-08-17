# Lecture 10 — Multiple objects

**Week 10 of 15** · WebGL Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** scene loop: for each mesh bind, set M, draw; one program  
**Success check:** they draw three cubes with different M from one program and a mesh record

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `WebGL Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: many objects, one pipeline | Invariant: a Mesh is a draw call; compiling per cube is the anti-pattern Three.js will hide`

## Board at the end (they photograph this)

```
for (const o of objects) {
  bind VAO
  uniform u_m = o.matrix     // world
  drawElements
}

ONE program     many M
parent:  M_child = M_parent * M_local
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** Three.js Object3D is this loop with more. If they compile a program per cube they will not understand instancing next. Naive loop this week; demo 14 is next week.

**Ask:** What changes per object — the program or M? Wait. Want: M (and maybe material uniforms), not a new program.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *scene loop, many uniforms*.

**Do not:** New program per cube.

### Minutes 10–12 — Frame

**Say:** Mesh record: {vao, count, matrix}. Shared geometry: same vao, different M. State leaks: leftover binds. Parenting: multiply local onto parent.

**Ask:** Is a VAO per mesh or per layout?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** CPU loop. Bind, uniform, draw.

**Board:** the for-each. Circle u_m.

**Say:** Shared geometry for three cubes. New program per cube is the plant.

**Ask:** Why one program?

**They do:** On paper: fields of a mesh record.

**Do not:** Wrap the first triangle in Three.js. Unfreeze conventions.

### Minutes 35–50 — Show

**Say:** Three cubes different M. Plant new program per cube. Plant leaking ELEMENT_ARRAY binds.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Parent a second cube (local offset). Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: parented cube; shared geometry. Homework: why one program; loop. Quiz: what changes per object, compile per mesh?, VAO name.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Mesh record | They copy fields. |
| 10–30 | Three cubes | Plant compile in the loop. |
| 30–45 | Parent multiply | Forgot update order. |
| 45–60 | They parent | Circulate. |

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

None this meeting.


## Snippet

```js
for (const o of objects) { setM(o.m); gl.drawElements(...); }
```

---

## Extra exercises

See [[WebGL Programming/exercises/Week 10]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. new program per cube.
2. leaking binds.

## If we run long, cut

Instancing. Keep the naive loop.

## If we run short, add

Shared geometry, two materials via uniforms.
