# Lecture 11 — Framebuffer objects

**Week 11 of 15** · WebGL Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** render to texture  
**Success check:** createFramebuffer.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `WebGL Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: render to texture | Invariant: CPU fills buffers; GPU runs the shader; P*V*M; CCW`

## Board at the end (they photograph this)

```
FBO → color tex → second pass
Two passes.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** Offscreen. Post and GPGPU.

**Ask:** createFramebuffer? Wait seven seconds. Take two answers.

**Board:** parked strip. Then FBO → color tex → second pass.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *render to texture*.

**Do not:** Forgetting to unbind.

### Minutes 10–12 — Frame

**Say:** Today’s question: render to texture. Kernel: render to texture. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: forgetting to unbind.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Offscreen. Post and GPGPU.

**Say:** Size. FBO size vs canvas.

**Say:** Depth. DEPTH_COMPONENT16 renderbuffer if 3D into FBO.

**Ask:** createFramebuffer? Wait seven seconds. Take two answers.

**They do:** On paper: incomplete FBO debug.

**Do not:** wrap the first triangle in Three.js. Freeze conventions.

### Minutes 35–50 — Show

**Say:** Live demo: Draw cube to FBO; display as a quad.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** incomplete FBO debug.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: incomplete FBO debug.; second pass invert extra.. Homework: Written: why FBO.; Code: one offscreen pass.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: render to texture | Plant the first common mistake. |
| 10–30 | Draw cube to FBO; display as a quad. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. COMPLETE (3)
2. unbind (3)
3. post (4)


## Snippet

```js
gl.bindFramebuffer(gl.FRAMEBUFFER, fbo);
```

---

## Extra exercises

See [[WebGL Programming/exercises/Week 11]].

---

## Notes you may still need (from the outline)

**1. Offscreen.** Post and GPGPU. [[WebGL/15 Postprocess]], [[WebGL/17 Particles and GPGPU]].

**2. Size.** FBO size vs canvas.

**3. Depth.** DEPTH_COMPONENT16 renderbuffer if 3D into FBO.

---

## Common mistakes

1. forgetting to unbind.
2. depth missing then 3D into FBO.

## If we run long, cut

Depth

## If we run short, add

second pass invert extra.
