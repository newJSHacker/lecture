# Lecture 1 — GPGPU idea

**Week 1 of 15** · GPU Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** GPU as throughput  
**Success check:** Contrast CPU latency vs GPU throughput.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `GPU Programming/code/01-pong.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: GPU as throughput | Invariant: data lives where the kernel runs`

## Board at the end (they photograph this)

```
data parallel vs graphics
Throughput bars.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** Why this course. Particles, fluids teasers, image filters, and an honest WebGPU intro.

**Ask:** Contrast CPU latency vs GPU throughput? Wait seven seconds. Take two answers.

**Board:** parked strip. Then data parallel vs graphics.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *GPU as throughput*.

**Do not:** Teaching only CUDA slides in a web degree.

### Minutes 8–12 — Frame

**Say:** Today’s question: GPU as throughput. Kernel: GPU as throughput. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: teaching only CUDA slides in a web degree.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Why this course. Particles, fluids teasers, image filters, and an honest WebGPU intro.

**Say:** Web vs native. CUDA/OpenCL exist.

**Say:** Limits. No pointers in FS.

**Ask:** Contrast CPU latency vs GPU throughput? Wait seven seconds. Take two answers.

**They do:** On paper: time uniform.

**Do not:** require CUDA. WebGL/WebGPU in the browser.

### Minutes 35–50 — Show

**Say:** Live demo: Fullscreen FS that writes a gradient 'simulation' into a texture (static).. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** time uniform.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: time uniform.; why this is a kernel.. Homework: Written: CPU vs GPU 1 page.; screenshot.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: GPU as throughput | Plant the first common mistake. |
| 10–30 | Fullscreen FS that writes a gradient 'simulation' into a texture (static). | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. throughput (3)
2. readback (4)
3. CUDA this program? (3)


## Snippet

```glsl
outColor = vec4(uv, 0.5+0.5*sin(u_time), 1.0);
```

---

## Extra exercises

See [[GPU Programming/exercises/Week 01]].

---

## Notes you may still need (from the outline)

**1. Why this course.** Particles, fluids teasers, image filters, and an honest WebGPU intro. Graphics students already write FS kernels; GPGPU is the same hardware with fewer triangles.

**2. Web vs native.** CUDA/OpenCL exist. IGWT still ships in a browser: FBO ping-pong, transform feedback name, then WebGPU compute.

**3. Limits.** No pointers in FS. Fixed output size. Readback is slow.

---

## Common mistakes

1. teaching only CUDA slides in a web degree.
2. readPixels every frame.

## If we run long, cut

Limits

## If we run short, add

why this is a kernel.
