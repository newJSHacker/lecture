# Lecture 3 — GLSL ES 3.00

**Week 3 of 15** · WebGL Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** version, precision, in/out  
**Success check:** #version 300 es first line.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `WebGL Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: version, precision, in/out | Invariant: CPU fills buffers; GPU runs the shader; P*V*M; CCW`

## Board at the end (they photograph this)

```
#version 300 es
Shader stages.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** Language. [[WebGL/11 Vertex and Fragment]].

**Ask:** #version 300 es first line? Wait seven seconds. Take two answers.

**Board:** parked strip. Then #version 300 es.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *version, precision, in/out*.

**Do not:** Version after other lines.

### Minutes 10–12 — Frame

**Say:** Today’s question: version, precision, in/out. Kernel: version, precision, in/out. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: version after other lines.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Language. [[WebGL/11 Vertex and Fragment]].

**Say:** Errors. Compile log is the teacher.

**Say:** Types. vec3, mat4, sampler2D.

**Ask:** #version 300 es first line? Wait seven seconds. Take two answers.

**They do:** On paper: A second program (debug color).

**Do not:** wrap the first triangle in Three.js. Freeze conventions.

### Minutes 35–50 — Show

**Say:** Live demo: Break a shader; read the log; fix.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** A second program (debug color).

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: A second program (debug color).; precision extra.. Homework: Written: WebGL1 vs 2 shader diffs.; Code: versioned pair.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: version, precision, in/out | Plant the first common mistake. |
| 10–30 | Break a shader; read the log; fix. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `WebGL Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. A second program (debug color).
2. precision extra.

---

## Homework

1. Written: WebGL1 vs 2 shader diffs.
2. Code: versioned pair.

---

## Quiz next meeting (they hear this now)

1. first line (3)
2. gl_FragColor in WebGL2? (4)
3. precision (3)


## Snippet

```glsl
#version 300 es
precision highp float;
out vec4 outColor;
```

---

## Extra exercises

See [[WebGL Programming/exercises/Week 03]].

---

## Notes you may still need (from the outline)

**1. Language.** [[WebGL/11 Vertex and Fragment]].

**2. Errors.** Compile log is the teacher.

**3. Types.** vec3, mat4, sampler2D.

---

## Common mistakes

1. version after other lines.
2. using texture2D in 300 es.

## If we run long, cut

Types

## If we run short, add

precision extra.
