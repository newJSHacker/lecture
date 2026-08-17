# Lecture 11 — Particles in WebGPU

**Week 11 of 15** · GPU Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** buffer of structs  
**Success check:** Struct Particle.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `GPU Programming/code/01-pong.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: buffer of structs | Invariant: data lives where the kernel runs`

## Board at the end (they photograph this)

```
compute update + render
Compute then draw.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** Two passes. Compute: physics.

**Ask:** Struct Particle? Wait seven seconds. Take two answers.

**Board:** parked strip. Then compute update + render.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *buffer of structs*.

**Do not:** Uploading 100k positions from JS every frame.

### Minutes 10–12 — Frame

**Say:** Today’s question: buffer of structs. Kernel: buffer of structs. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: uploading 100k positions from JS every frame.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Two passes. Compute: physics.

**Say:** When stay WebGL. If the audience is Safari-old or the feature is a textured cube, WebGL is enough.

**Say:** Limits. Buffer sizes.

**Ask:** Struct Particle? Wait seven seconds. Take two answers.

**They do:** On paper: WebGL fallback note.

**Do not:** require CUDA. WebGL/WebGPU in the browser.

### Minutes 35–50 — Show

**Say:** Live demo: N particles in WGSL compute; draw as points.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** WebGL fallback note.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: WebGL fallback note.; dt uniform.. Homework: Written: when you would not use WebGPU.; demo.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: buffer of structs | Plant the first common mistake. |
| 10–30 | N particles in WGSL compute; draw as points. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `GPU Programming/code/01-pong.html` as the after-class check, not as the lecture.

---

## Lab

1. WebGL fallback note.
2. dt uniform.

---

## Homework

1. Written: when you would not use WebGPU.
2. demo.

---

## Quiz next meeting (they hear this now)

1. source of truth (4)
2. two passes (3)
3. Safari (3)


## Snippet

```wgsl
struct P { pos: vec2f, vel: vec2f }
```

---

## Extra exercises

See [[GPU Programming/exercises/Week 11]].

---

## Notes you may still need (from the outline)

**1. Two passes.** Compute: physics. Render: draw points/triangles.

**2. When stay WebGL.** If the audience is Safari-old or the feature is a textured cube, WebGL is enough. Honesty in the README.

**3. Limits.** Buffer sizes. Workgroup limits.

---

## Common mistakes

1. uploading 100k positions from JS every frame.
2. no fallback story for the course project if required to run in the lab.

## If we run long, cut

Limits

## If we run short, add

dt uniform.
