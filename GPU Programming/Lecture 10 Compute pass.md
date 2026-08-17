# Lecture 10 — Compute pass

**Week 10 of 15** · GPU Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** workgroups  
**Success check:** A compute shader fills a storage texture or buffer.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `GPU Programming/code/01-pong.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: workgroups | Invariant: data lives where the kernel runs`

## Board at the end (they photograph this)

```
dispatch(x,y,z)
Grid of threads.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** Compute. No raster.

**Ask:** A compute shader fills a storage texture or buffer? Wait seven seconds. Take two answers.

**Board:** parked strip. Then dispatch(x,y,z).

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *workgroups*.

**Do not:** Compute that still rasterizes a triangle per particle.

### Minutes 10–12 — Frame

**Say:** Today’s question: workgroups. Kernel: workgroups. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: compute that still rasterizes a triangle per particle.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Compute. No raster.

**Say:** Memory. storage buffers vs textures.

**Say:** Map. This replaces some ping-pong FS hacks.

**Ask:** A compute shader fills a storage texture or buffer? Wait seven seconds. Take two answers.

**They do:** On paper: particle integrate extra if time.

**Do not:** require CUDA. WebGL/WebGPU in the browser.

### Minutes 35–50 — Show

**Say:** Live demo: Compute a gradient or noise into a texture; blit.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** particle integrate extra if time.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: particle integrate extra if time.; workgroup 8×8.. Homework: Written: workgroup.; WGSL compute.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: workgroups | Plant the first common mistake. |
| 10–30 | Compute a gradient or noise into a texture; blit. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `GPU Programming/code/01-pong.html` as the after-class check, not as the lecture.

---

## Lab

1. particle integrate extra if time.
2. workgroup 8×8.

---

## Homework

1. Written: workgroup.
2. WGSL compute.

---

## Quiz next meeting (they hear this now)

1. dispatch (3)
2. storage (4)
3. why not FS (3)


## Snippet

```wgsl
@compute @workgroup_size(8,8) fn cs(@builtin(global_invocation_id) id: vec3u) { /* ... */ }
```

---

## Extra exercises

See [[GPU Programming/exercises/Week 10]].

---

## Notes you may still need (from the outline)

**1. Compute.** No raster. Threads in a grid. Perfect for particles and blur.

**2. Memory.** storage buffers vs textures. Race if you write without sync.

**3. Map.** This replaces some ping-pong FS hacks.

---

## Common mistakes

1. compute that still rasterizes a triangle per particle.
2. unbounded loops in WGSL.

## If we run long, cut

Map

## If we run short, add

workgroup 8×8.
