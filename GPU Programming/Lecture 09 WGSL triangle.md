# Lecture 9 — WGSL triangle

**Week 9 of 15** · GPU Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** WGSL vs/fs: @builtin(vertex_index) → clip position; bind group for time  
**Success check:** they can read a WGSL pair, resize, and table six GLSL vs WGSL rows

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `GPU Programming/code/01-pong.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: a triangle you wrote | Invariant: Three.js WebGPURenderer without reading WGSL is not the lab; validation errors are loud on purpose`

## Board at the end (they photograph this)

```
@vertex   fn vs(@builtin(vertex_index) i: u32)
          -> @builtin(position) vec4f

@fragment fn fs(...) -> @location(0) vec4f

clip z  0..1  (not GLSL's -1..1)   — freeze and say it
bind group  ≈  uniforms
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** WGSL is typed. @location. No GLSL preprocessor soup. navigator.gpu.requestAdapter then configure the canvas. Copying a full sample unread fails. Still no CUDA.

**Ask:** Who supplies vertex_index — a VBO, or the draw? Wait. Want: the draw (builtin).

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *vertex_index, clip*.

**Do not:** Three.js WebGPURenderer as the only lab with no WGSL read.

### Minutes 10–12 — Frame

**Say:** Colored triangle; resize. Uniform time extra. Compare GLSL side by side. Clip Z convention named.

**Ask:** What is a bind group?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Three vertices from an index. No buffer required for the hello.

**Board:** @vertex @fragment. Circle clip z.

**Say:** Validation is loud — read it like a GLSL compile log.

**Ask:** Write the vs signature in one line.

**They do:** On paper: GLSL vs WGSL, three rows to start the homework table.

**Do not:** Require CUDA. Stay in the browser (WebGL/WebGPU).

### Minutes 35–50 — Show

**Say:** Colored triangle WGSL; resize. Plant WebGPURenderer as the only lab. Plant unread sample paste. Local, no CDN.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Uniform time extra. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: time uniform + GLSL side by side. Homework: 6-row table; code. Quiz: @builtin(position), bind group, clip z.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | requestAdapter + configure | Plant no detect. |
| 10–30 | WGSL triangle | Plant Three.js-only lab. |
| 30–45 | Resize + validation error | Read it out loud. |
| 45–60 | They add time bind group | Circulate. |

Point them at `GPU Programming/code/01-pong.html` as the after-class check, not as the lecture.

---

## Lab

1. uniform time extra.
2. compare GLSL side by side.

---

## Homework

1. Written: GLSL vs WGSL table (6 rows).
2. code.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```wgsl
@vertex fn vs(@builtin(vertex_index) i: u32) -> @builtin(position) vec4f { /* ... */ }
```

---

## Extra exercises

See [[GPU Programming/exercises/Week 09]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. three.js WebGPURenderer as the only lab with no WGSL read.
2. copying a full sample unread.

## If we run long, cut

A mesh loader. Keep triangle + bind group + table.

## If we run short, add

Clip z 0..1 on the parked strip.
