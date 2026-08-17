# Lecture 12 — Fullscreen post

**Week 12 of 15** · Shader Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** pass 1: scene → FBO color; pass 2: fullscreen FS (vignette/grain)  
**Success check:** they can name both passes and toggle the post without using it as lighting

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `Shader Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: scene tex → FS | Invariant: post is an image filter on a named pass; it is not the light`

## Board at the end (they photograph this)

```
PASS 1  scene (march or mesh)  →  color tex
PASS 2  fullscreen quad         →  vignette / grain

ping-pong  named for GPU course
FXAA       named for RTR
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** Same FBO idea as WebGL week 11. Name every pass. A 4K FBO on integrated graphics is a hang — we do not invent timings; we shrink the target or omit the claim.

**Ask:** How many passes in vignette-on-a-cube? Wait. Want: two (at least).

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *scene tex → FS*.

**Do not:** Post as a substitute for lighting.

### Minutes 10–12 — Frame

**Say:** Kernel filters: blur/sharpen teaching. Separable blur is a name. Ping-pong is GPU Programming's week 2.

**Ask:** Why extra fill rate?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Two boxes: scene, then quad. Label the texture.

**Board:** two passes. Circle 'not lighting'.

**Say:** Grain should be after tonemap in RTR; here it is a 2D teaching filter. Toggle with a uniform.

**Ask:** What is pass 1 writing?

**They do:** On paper: arrows FBO color → sampler2D in FS.

**Do not:** Paste a 200-line Shadertoy as the first kernel.

### Minutes 35–50 — Show

**Say:** Vignette + grain on a marching scene or textured cube. Plant post as lighting. Toggle post.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Blur extra (separable name). Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: blur name + toggle. Homework: why extra fill rate; two-pass code. Quiz: FBO, grain should be, 8 passes as a smell.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | FBO scene | Plant 4K target. |
| 10–30 | Vignette FS | Plant post as lighting. |
| 30–45 | Toggle uniform | Pause; debug still. |
| 45–60 | They name separable blur | Circulate. |

Point them at `Shader Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. blur extra (separable name).
2. toggle post.

---

## Homework

1. Written: why extra fill rate.
2. Two-pass code.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```glsl
color *= smoothstep(1.2, 0.4, length(uv-0.5));
```

---

## Extra exercises

See [[Shader Programming/exercises/Week 12]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. post as a substitute for lighting.
2. 4K FBO on integrated GPU.

## If we run long, cut

Eight Instagram passes. Keep two named passes.

## If we run short, add

Ping-pong as a name only.
