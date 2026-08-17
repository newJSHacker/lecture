# Lecture 6 — Fluids teaser

**Week 6 of 15** · GPU Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** divergence-free idea  
**Success check:** Stable fluids names (Stam).

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `GPU Programming/code/01-pong.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: divergence-free idea | Invariant: data lives where the kernel runs`

## Board at the end (they photograph this)

```
advect → diffuse → project
Velocity + dye.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** Idea. Velocity field in a texture.

**Ask:** Stable fluids names (Stam)? Wait seven seconds. Take two answers.

**Board:** parked strip. Then advect → diffuse → project.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *divergence-free idea*.

**Do not:** Unity Visual Effect Graph as the homework.

### Minutes 10–12 — Frame

**Say:** Today’s question: divergence-free idea. Kernel: divergence-free idea. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Unity Visual Effect Graph as the homework.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Idea. Velocity field in a texture.

**Say:** Scope. A dye blob that swirls is the lab.

**Say:** Refs. GPU Gems / Stam.

**Ask:** Stable fluids names (Stam)? Wait seven seconds. Take two answers.

**They do:** On paper: one Jacobi extra or a note why skipped.

**Do not:** require CUDA. WebGL/WebGPU in the browser.

### Minutes 35–50 — Show

**Say:** Live demo: 2D dye advected by a mouse-drawn velocity or a vortex field.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** one Jacobi extra or a note why skipped.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: one Jacobi extra or a note why skipped.; dissipation.. Homework: Written: why project.; screenshot.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: divergence-free idea | Plant the first common mistake. |
| 10–30 | 2D dye advected by a mouse-drawn velocity or a vortex field. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `GPU Programming/code/01-pong.html` as the after-class check, not as the lecture.

---

## Lab

1. one Jacobi extra or a note why skipped.
2. dissipation.

---

## Homework

1. Written: why project.
2. screenshot.

---

## Quiz next meeting (they hear this now)

1. advect (3)
2. incompressible (4)
3. 3D this week? (3)


## Snippet

```glsl
vec2 p = uv - dt * vel; vec4 dye = texture(u_dye, p);
```

---

## Extra exercises

See [[GPU Programming/exercises/Week 06]].

---

## Notes you may still need (from the outline)

**1. Idea.** Velocity field in a texture. Advect. Pressure solve makes it incompressible — Jacobi iteration name.

**2. Scope.** A dye blob that swirls is the lab. 3D Navier–Stokes is a thesis.

**3. Refs.** GPU Gems / Stam. Cite.

---

## Common mistakes

1. Unity Visual Effect Graph as the homework.
2. unstable huge dt.

## If we run long, cut

Refs

## If we run short, add

dissipation.
