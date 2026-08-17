# Lecture 1 — GPGPU idea

**Week 1 of 15** · GPU Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** GPU as throughput: one FS kernel over a grid; readback is slow  
**Success check:** they can contrast CPU latency vs GPU throughput and say why this is a kernel, not a triangle demo

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `GPU Programming/code/01-pong.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: see a fullscreen kernel | Invariant: data lives where the kernel runs; CUDA slides without a browser path are the wrong degree`

## Board at the end (they photograph this)

```
CPU:  one thread, low latency
GPU:  many lanes, high throughput

FS kernel:  one texel / pixel  (no pointers)

readPixels every frame  =  stall
this program: WebGL then WebGPU — not CUDA-only
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** Particles, fluids teasers, image filters, then an honest WebGPU intro. Graphics students already write FS kernels; GPGPU is the same hardware with fewer triangles. Teaching only CUDA in a web degree fails the course contract.

**Ask:** Is CUDA required this term? Wait. Want: no.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *GPU as throughput*.

**Do not:** Teaching only CUDA slides in a web degree.

### Minutes 8–12 — Frame

**Say:** Web vs native: CUDA/OpenCL exist. IGWT ships in the browser: FBO ping-pong, TF as a name, then WebGPU. Limits: no pointers in FS, fixed output size, readback is slow.

**Ask:** Why is readPixels every frame a problem?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Throughput bars vs a latency needle. Same silicon, different job.

**Board:** data-parallel vs graphics. Circle no CUDA-only path.

**Say:** A gradient 'simulation' into a texture is already a kernel. Time is a uniform you can pause.

**Ask:** Where does the state live this week?

**They do:** On paper: CPU vs GPU, four bullets, no CUDA-only line.

**Do not:** Require CUDA. Stay in the browser (WebGL/WebGPU).

### Minutes 35–50 — Show

**Say:** Fullscreen FS writes a gradient into a texture (static). Demo GPU Programming/code/01-pong.html when it helps. Plant CUDA-only slides. Plant readPixels every frame. Local serve, no CDN.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Time uniform. Why this is a kernel, in a sentence. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: time uniform + kernel sentence. Homework: CPU vs GPU one page; screenshot. Quiz: throughput, readback, CUDA this program?

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Throughput vs latency | Plant CUDA-only path. |
| 10–30 | FS as kernel | Plant readPixels every frame. |
| 30–45 | u_time pause | Debug a still. |
| 45–60 | They write the kernel sentence | Circulate. |

Point them at `GPU Programming/code/01-pong.html` as the after-class check, not as the lecture.

---

## Lab

1. time uniform.
2. why this is a kernel.

---

## Homework

1. Written: CPU vs GPU 1 page.
2. screenshot.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```glsl
outColor = vec4(uv, 0.5+0.5*sin(u_time), 1.0);
```

---

## Extra exercises

See [[GPU Programming/exercises/Week 01]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. teaching only CUDA slides in a web degree.
2. readPixels every frame.

## If we run long, cut

OpenCL history. Keep kernel + no CUDA-only.

## If we run short, add

Fixed output size as a limit on the board.
