# Lecture 12 — Instancing

**Week 12 of 15** · WebGL Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** divisor, one draw  
**Success check:** instance attribute.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `WebGL Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: divisor, one draw | Invariant: CPU fills buffers; GPU runs the shader; P*V*M; CCW`

## Board at the end (they photograph this)

```
gl.drawArraysInstanced
Forest.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** GPU repetition. Forest, particles, bolts.

**Ask:** instance attribute? Wait seven seconds. Take two answers.

**Board:** parked strip. Then gl.drawArraysInstanced.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *divisor, one draw*.

**Do not:** Instancing without measuring.

### Minutes 10–12 — Frame

**Say:** Today’s question: divisor, one draw. Kernel: divisor, one draw. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: instancing without measuring.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** GPU repetition. Forest, particles, bolts.

**Say:** CPU. Still upload instance buffer when it changes.

**Say:** Limits. Attribute slots.

**Ask:** instance attribute? Wait seven seconds. Take two answers.

**They do:** On paper: color per instance.

**Do not:** wrap the first triangle in Three.js. Freeze conventions.

### Minutes 35–50 — Show

**Say:** Live demo: 100 cubes instanced vs 100 draw calls (measure).. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** color per instance.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: color per instance.; measured table.. Homework: Written: when instancing wins.; Code: instanced.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: divisor, one draw | Plant the first common mistake. |
| 10–30 | 100 cubes instanced vs 100 draw calls (measure). | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. divisor (4)
2. drawInstanced (3)
3. n=3 (3)


## Snippet

```js
gl.vertexAttribDivisor(loc, 1);
```

---

## Extra exercises

See [[WebGL Programming/exercises/Week 12]].

---

## Notes you may still need (from the outline)

**1. GPU repetition.** Forest, particles, bolts. Demo 14.

**2. CPU.** Still upload instance buffer when it changes.

**3. Limits.** Attribute slots.

---

## Common mistakes

1. instancing without measuring.
2. divisor on the wrong attrib.

## If we run long, cut

Limits

## If we run short, add

measured table.
