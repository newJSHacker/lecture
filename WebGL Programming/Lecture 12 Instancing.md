# Lecture 12 — Instancing

**Week 12 of 15** · WebGL Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** vertexAttribDivisor(1); drawArraysInstanced — one draw, many M  
**Success check:** they instance 100 cubes, color per instance, and compare to 100 draw calls by measuring on this machine

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `WebGL Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: one draw for a forest | Invariant: divisor 1 means the attrib advances per instance; do not invent fps`

## Board at the end (they photograph this)

```
per-vertex attrib     divisor 0
per-instance attrib   divisor 1

gl.vertexAttribDivisor(loc, 1)
gl.drawArraysInstanced(..., instanceCount)

measure 100 draws vs 1   (this machine; no invented fps)
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** Week 10 was a CPU loop. Today the GPU repeats. Forest, particles, bolts. Demo 14-instancing.html. If they do not measure, instancing is a religion.

**Ask:** Does divisor go on the position attrib of the cube? Wait. Want: no — on the instance offset/color.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *divisor, one draw*.

**Do not:** Instancing without measuring.

### Minutes 10–12 — Frame

**Say:** Still upload the instance buffer when it changes. Attribute slot limits named. n=3 on a quiz is 'three instances.'

**Ask:** When does instancing lose to a loop of three unique meshes?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Same geometry, different instance attribs.

**Board:** divisor 0 vs 1. drawInstanced.

**Say:** Color per instance as the lab kernel.

**Ask:** What does instanceCount mean in drawArraysInstanced?

**They do:** On paper: which attribs get divisor 1.

**Do not:** Wrap the first triangle in Three.js. Unfreeze conventions.

### Minutes 35–50 — Show

**Say:** 100 cubes instanced vs 100 draw calls — log times or info, no invented fps. Demo 14-instancing.html. Plant divisor on the wrong attrib.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Color per instance. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: color per instance; measured table. Homework: when instancing wins; instanced. Quiz: divisor, drawInstanced, n=3.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Instance buffer of offsets | Plant STATIC then never update. |
| 10–30 | divisor 1 + instanced draw | Plant divisor on a_pos. |
| 30–45 | Measure loop vs instance | No invented fps. |
| 45–60 | They color instances | Circulate. |

Point them at `WebGL Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. color per instance.
2. measured table.

---

## Homework

1. Written: when instancing wins.
2. Code: instanced.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
gl.vertexAttribDivisor(loc, 1);
```

---

## Extra exercises

See [[WebGL Programming/exercises/Week 12]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. instancing without measuring.
2. divisor on the wrong attrib.

## If we run long, cut

Indirect draw. Keep divisor + one draw + measure.

## If we run short, add

Measured table: loop vs instanced on this GPU.
