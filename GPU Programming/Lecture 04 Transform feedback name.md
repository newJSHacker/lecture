# Lecture 4 — Transform feedback name

**Week 4 of 15** · GPU Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** transform feedback name: VS writes varyings into a buffer; rasterizer discard  
**Success check:** they can name TF vs FBO ping-pong and keep particles working even if TF is diagram-only

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `GPU Programming/code/01-pong.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: name VS→buffer | Invariant: TF is the graphics pipeline as compute; ping-pong remains the teaching path until WebGPU`

## Board at the end (they photograph this)

```
TF:   VS varyings  →  GL buffer   (optional rasterizer discard)
FBO:  FS           →  texture     (week 2 — still valid)

WebGPU compute  will replace a lot of TF
no CUDA path
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** Particles as vertices: VS updates pos. Rasterizer discard named. FS ping-pong is often easier in WebGL teaching. Skipping particles entirely fails. Claiming TF without a buffer fails.

**Ask:** What does TF capture — FS color, or VS outputs? Wait. Want: VS.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *VS output captured*.

**Do not:** Skipping particles entirely.

### Minutes 10–12 — Frame

**Say:** Diagram required. Tiny TF optional. A README that says 'we use ping-pong instead' plus a working FS sim is honest. WebGPU compute later makes TF less necessary — still teach the name.

**Ask:** When would you keep FBO ping-pong?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** VS to buffer arrow. Discard the triangles.

**Board:** TF vs FBO table. Circle discard.

**Say:** transformFeedbackVaryings as a 20pt name, not a CUDA port.

**Ask:** WebGPU's replacement in one word?

**They do:** On paper: TF vs FBO, one sentence each.

**Do not:** Require CUDA. Stay in the browser (WebGL/WebGPU).

### Minutes 35–50 — Show

**Say:** Diagram + optional tiny TF, or ping-pong README with working FS sim. Plant skip particles. Plant TF with no buffer.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Rasterizer discard name + compare sentence. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: discard name + compare. Homework: TF vs FBO; week-3 particles OK. Quiz: TF captures, discard, WebGPU replacement.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Name TF | Plant skip particles. |
| 10–30 | Diagram VS→buffer | Plant TF without a buffer. |
| 30–45 | Ping-pong still runs | Honesty in README. |
| 45–60 | They write the compare | Circulate. |

Point them at `GPU Programming/code/01-pong.html` as the after-class check, not as the lecture.

---

## Lab

1. rasterizer discard name.
2. compare one sentence.

---

## Homework

1. Written: TF vs FBO.
2. working particles from week 3 OK.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
gl.transformFeedbackVaryings(prog, ['v_pos'], gl.SEPARATE_ATTRIBS);
```

---

## Extra exercises

See [[GPU Programming/exercises/Week 04]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. skipping particles entirely.
2. claiming TF without a buffer.

## If we run long, cut

A full TF engine. Keep the name + honest ping-pong.

## If we run short, add

SEPARATE_ATTRIBS as a name.
