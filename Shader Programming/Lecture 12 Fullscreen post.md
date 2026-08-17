# Lecture 12 — Fullscreen post

**Week 12 of 15** · Shader Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** scene tex → FS  
**Success check:** Render a 3D or Shadertoy scene to a texture (or use a still).

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `Shader Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: scene tex → FS | Invariant: a shader is a program over pixels or vertices`

## Board at the end (they photograph this)

```
FBO color → quad
Two passes.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** Post. Same FBO idea as WebGL week 11.

**Ask:** Render a 3D or Shadertoy scene to a texture (or use a still)? Wait seven seconds. Take two answers.

**Board:** parked strip. Then FBO color → quad.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *scene tex → FS*.

**Do not:** Post as a substitute for lighting.

### Minutes 10–12 — Frame

**Say:** Today’s question: scene tex → FS. Kernel: scene tex → FS. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: post as a substitute for lighting.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Post. Same FBO idea as WebGL week 11.

**Say:** FXAA name. RTR will name AA.

**Say:** Ping-pong. Named for GPU course.

**Ask:** Render a 3D or Shadertoy scene to a texture (or use a still)? Wait seven seconds. Take two answers.

**They do:** On paper: blur extra (separable name).

**Do not:** paste a 200-line Shadertoy as the first kernel.

### Minutes 35–50 — Show

**Say:** Live demo: Vignette + grain on a marching scene or a textured cube.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** blur extra (separable name).

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: blur extra (separable name).; toggle post.. Homework: Written: why extra fill rate.; Two-pass code.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: scene tex → FS | Plant the first common mistake. |
| 10–30 | Vignette + grain on a marching scene or a textured cube. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. FBO (3)
2. grain should be (4)
3. 8 passes (3)


## Snippet

```glsl
color *= smoothstep(1.2, 0.4, length(uv-0.5));
```

---

## Extra exercises

See [[Shader Programming/exercises/Week 12]].

---

## Notes you may still need (from the outline)

**1. Post.** Same FBO idea as WebGL week 11. Shaders here are 2D image filters.

**2. FXAA name.** RTR will name AA. This week: kernel filters (blur/sharpen) as teaching.

**3. Ping-pong.** Named for GPU course.

---

## Common mistakes

1. post as a substitute for lighting.
2. 4K FBO on integrated GPU.

## If we run long, cut

Ping-pong

## If we run short, add

toggle post.
