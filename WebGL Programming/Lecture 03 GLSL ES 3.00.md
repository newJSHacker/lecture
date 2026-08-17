# Lecture 3 — GLSL ES 3.00

**Week 3 of 15** · WebGL Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** #version 300 es first line; precision; in/out; outColor not gl_FragColor  
**Success check:** they can break a shader, read the compile log, and ship a versioned VS/FS pair

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `WebGL Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: GLSL ES 3.00 that compiles | Invariant: the first line is the language; the log is the teacher`

## Board at the end (they photograph this)

```
#version 300 es          ← first line, nothing before
precision highp float;
in  / out                not attribute / varying
out vec4 outColor;       not gl_FragColor
texture()                not texture2D

vec3  mat4  sampler2D
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** A silent black screen is often a shader that did not compile. Today we make the log loud. WebGL1 vs 2 is a dialect, not a vibe.

**Ask:** Can #version 300 es sit on line 2 after a comment? Wait. Want: first line; even a blank can bite — freeze: first.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *version, precision, in/out*.

**Do not:** Version after other lines.

### Minutes 10–12 — Frame

**Say:** in/out, layout(location=), outColor. precision highp float in FS. Types: vec3, mat4, sampler2D. Demo: break 01-triangle shaders.

**Ask:** Does WebGL2 have gl_FragColor?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Language table on the board. WebGL1 names are banned in 300 es.

**Board:** #version, precision, outColor.

**Say:** Link error ≠ compile error. Check both.

**Ask:** texture2D in 300 es — what happens?

**They do:** On paper: the three first lines of a FS.

**Do not:** Wrap the first triangle in Three.js. Unfreeze conventions.

### Minutes 35–50 — Show

**Say:** Break a shader; read the log; fix. Plant version after other lines. Plant texture2D. Plant gl_FragColor.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** A second program that paints debug magenta. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: debug-color program + precision extra. Homework: WebGL1 vs 2 diffs; versioned pair. Quiz: first line, gl_FragColor?, precision.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | #version first | Plant it on line 2. |
| 10–30 | Break / log / fix | They must hear the log. |
| 30–45 | outColor vs gl_FragColor | Plant the old name. |
| 45–60 | They write a second program | Circulate. |

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

None this meeting.


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

_none_

---

## Common mistakes

1. version after other lines.
2. using texture2D in 300 es.

## If we run long, cut

Every GLSL built-in. Keep version + logs.

## If we run short, add

precision extra on a second FS.
