# Lecture 4 — Transform feedback name

**Week 4 of 15** · GPU Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** VS output captured  
**Success check:** Name TF: vertex shader writes buffers.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `GPU Programming/code/01-pong.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: VS output captured | Invariant: data lives where the kernel runs`

## Board at the end (they photograph this)

```
varyings → buffer
VS to buffer.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** TF. Particles as vertices.

**Ask:** TF: vertex shader writes buffers? Wait seven seconds. Take two answers.

**Board:** parked strip. Then varyings → buffer.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *VS output captured*.

**Do not:** Skipping particles entirely.

### Minutes 10–12 — Frame

**Say:** Today’s question: VS output captured. Kernel: VS output captured. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: skipping particles entirely.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** TF. Particles as vertices.

**Say:** vs FS. FS ping-pong is often easier in WebGL teaching.

**Say:** WebGPU. Compute shaders make TF less necessary.

**Ask:** TF: vertex shader writes buffers? Wait seven seconds. Take two answers.

**They do:** On paper: rasterizer discard name.

**Do not:** require CUDA. WebGL/WebGPU in the browser.

### Minutes 35–50 — Show

**Say:** Live demo: Diagram + optional tiny TF or a 'we use ping-pong instead' README with a working FS sim.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** rasterizer discard name.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: rasterizer discard name.; compare one sentence.. Homework: Written: TF vs FBO.; working particles from week 3 OK.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: VS output captured | Plant the first common mistake. |
| 10–30 | Diagram + optional tiny TF or a 'we use ping-pong instead' README with a working FS sim. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. TF captures (4)
2. discard (3)
3. WebGPU replacement (3)


## Snippet

```js
gl.transformFeedbackVaryings(prog, ['v_pos'], gl.SEPARATE_ATTRIBS);
```

---

## Extra exercises

See [[GPU Programming/exercises/Week 04]].

---

## Notes you may still need (from the outline)

**1. TF.** Particles as vertices. VS updates pos. Rasterizer can be rasterizer discard.

**2. vs FS.** FS ping-pong is often easier in WebGL teaching. TF is the 'graphics pipeline as compute' story.

**3. WebGPU.** Compute shaders make TF less necessary. Still teach the name.

---

## Common mistakes

1. skipping particles entirely.
2. claiming TF without a buffer.

## If we run long, cut

WebGPU

## If we run short, add

compare one sentence.
