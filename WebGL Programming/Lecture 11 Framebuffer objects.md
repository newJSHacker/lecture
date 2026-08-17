# Lecture 11 — Framebuffer objects

**Week 11 of 15** · WebGL Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** FBO: render to texture, then a fullscreen second pass  
**Success check:** they createFramebuffer, check COMPLETE, unbind to the canvas, and blit via a quad

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `WebGL Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: offscreen, then on screen | Invariant: the default framebuffer is the canvas; forget unbind and you draw into the texture forever`

## Board at the end (they photograph this)

```
createTexture + renderbuffer(depth)
createFramebuffer → COLOR_ATTACHMENT0
check FRAMEBUFFER_COMPLETE
draw scene → tex
bindFramebuffer(null) → draw quad sampling tex

FBO size ≠ canvas size   (often)
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** Post and GPGPU start here. Demo 13-framebuffer-post.html: cube to FBO, vignette on a fullscreen triangle. This is what EffectComposer hides next course.

**Ask:** After drawing to the FBO, where do you bind before the screen pass? Wait. Want: null / the canvas.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *render to texture*.

**Do not:** Forgetting to unbind.

### Minutes 10–12 — Frame

**Say:** Depth renderbuffer if 3D goes into the FBO. Incomplete FBO is a status, not a JS throw. Size: FBO can be smaller than the canvas.

**Ask:** Why might FRAMEBUFFER_COMPLETE fail?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Offscreen color tex. Second program samples it.

**Board:** two passes. Unbind.

**Say:** Identity post shader is the debug. Invert extra.

**Ask:** Do you need depth on a fullscreen post quad?

**They do:** On paper: the bind sequence for pass 1 and pass 2.

**Do not:** Wrap the first triangle in Three.js. Unfreeze conventions.

### Minutes 35–50 — Show

**Say:** Draw cube to FBO; display as a quad. Demo 13-framebuffer-post.html. Plant forgetting to unbind. Plant 3D into FBO with no depth.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Incomplete FBO debug: log the status. Then invert extra. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: incomplete debug; invert extra. Homework: why FBO; one offscreen pass. Quiz: COMPLETE, unbind, post.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Create FBO + tex | Plant no COMPLETE check. |
| 10–30 | Scene into FBO | Plant no depth RB. |
| 30–45 | Unbind + quad | Plant still bound to FBO. |
| 45–60 | They invert | Circulate. |

Point them at `WebGL Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. incomplete FBO debug.
2. second pass invert extra.

---

## Homework

1. Written: why FBO.
2. Code: one offscreen pass.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
gl.bindFramebuffer(gl.FRAMEBUFFER, fbo);
```

---

## Extra exercises

See [[WebGL Programming/exercises/Week 11]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. forgetting to unbind.
2. depth missing then 3D into FBO.

## If we run long, cut

Ping-pong GPGPU. Keep one offscreen pass.

## If we run short, add

Second-pass invert extra.
