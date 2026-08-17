# Lecture 10 — Compute pass

**Week 10 of 15** · GPU Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** compute pass: dispatch workgroups; write storage texture/buffer; then blit  
**Success check:** they can fill a texture from @compute @workgroup_size(8,8) without a triangle-per-particle

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `GPU Programming/code/01-pong.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: a grid of threads | Invariant: compute has no raster; races if you write without sync; this replaces some ping-pong FS hacks`

## Board at the end (they photograph this)

```
dispatch(x, y, 1)

@compute @workgroup_size(8,8)
fn cs(@builtin(global_invocation_id) id: vec3u)

storage buffer  vs  storage texture
  (draw the bytes:  width×height×channels)

no triangle per particle
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** No raster. Threads in a grid. Perfect for particles and blur. Unbounded loops in WGSL are a hang. Fallback: if WebGPU is missing, they still have ping-pong from week 2 — say so.

**Ask:** Does a compute shader need a triangle? Wait. Want: no.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *workgroups*.

**Do not:** Compute that still rasterizes a triangle per particle.

### Minutes 10–12 — Frame

**Say:** Memory: storage buffers vs textures. Map: replaces some FS ping-pong. Workgroup 8×8 is the lab size. Particle integrate extra if time — still in a buffer they draw.

**Ask:** Why workgroups?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Grid of threads over the texture. id.xy is the texel.

**Board:** dispatch + workgroup_size. Circle storage.

**Say:** Blit to the canvas is a separate render pass — name both.

**Ask:** What does dispatch(x,y,z) mean?

**They do:** On paper: compute pass then render/blit pass.

**Do not:** Require CUDA. Stay in the browser (WebGL/WebGPU).

### Minutes 35–50 — Show

**Say:** Compute a gradient or noise into a texture; blit. Plant compute that still rasterizes a triangle per particle. Plant unbounded loop.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Workgroup 8×8, or particle integrate extra. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: 8×8 + integrate extra if time. Homework: workgroup paragraph; WGSL compute. Quiz: dispatch, storage, why not FS.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Name compute pass | Plant triangle-per-particle. |
| 10–30 | 8×8 fill + blit | Plant unbounded loop. |
| 30–45 | Storage layout | Draw the bytes. |
| 45–60 | They dispatch | Circulate. Feature detect. |

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

None this meeting.


## Snippet

```wgsl
@compute @workgroup_size(8,8) fn cs(@builtin(global_invocation_id) id: vec3u) { /* ... */ }
```

---

## Extra exercises

See [[GPU Programming/exercises/Week 10]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. compute that still rasterizes a triangle per particle.
2. unbounded loops in WGSL.

## If we run long, cut

Shared-memory prefix sum. Keep dispatch + storage + blit.

## If we run short, add

Race/sync as a one-line warning.
