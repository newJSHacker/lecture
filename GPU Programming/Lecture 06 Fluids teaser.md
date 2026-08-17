# Lecture 6 — Fluids teaser

**Week 6 of 15** · GPU Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** stable-fluids names: advect → diffuse → project; dye and velocity textures  
**Success check:** they can advect a dye by a velocity field and say why project (incompressible)

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `GPU Programming/code/01-pong.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: divergence-free as a name, dye as a picture | Invariant: a swirling dye is the lab; 3D Navier–Stokes is a thesis; Unity VFX is not the homework`

## Board at the end (they photograph this)

```
vel tex   RG = velocity
dye tex   RGB = color     (ping-pong each)

advect  →  diffuse  →  project (Jacobi name)
  dye samples uv - dt * vel

3D NS  not this week
cite Stam / GPU Gems
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** Velocity field in a texture. Pressure solve makes it incompressible — Jacobi iteration named. A dye blob that swirls is the lab. Unstable huge dt fails. Cite.

**Ask:** Is 3D fluid the week? Wait. Want: no.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *divergence-free idea*.

**Do not:** Unity Visual Effect Graph as the homework.

### Minutes 10–12 — Frame

**Say:** Scope: 2D dye, mouse or vortex velocity. One Jacobi extra or a note why skipped. Dissipation extra. Still ping-pong — WebGPU later.

**Ask:** Why project?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Two layouts: vel and dye. Ping-pong both.

**Board:** advect → diffuse → project. Circle incompressible.

**Say:** Backtrace uv - dt*vel. Pause to see a still swirl.

**Ask:** Write the advect sample line.

**They do:** On paper: memory layout of vel vs dye.

**Do not:** Require CUDA. Stay in the browser (WebGL/WebGPU).

### Minutes 35–50 — Show

**Say:** 2D dye advected by mouse velocity or a vortex. Plant Unity VFX as homework. Plant huge dt. Local only.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** One Jacobi extra or a skip note. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: Jacobi note + dissipation. Homework: why project; screenshot. Quiz: advect, incompressible, 3D this week?

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Vel + dye layout | Plant Unity VFX homework. |
| 10–30 | Advect dye | Plant huge dt. |
| 30–45 | Project name | Jacobi optional. |
| 45–60 | They add dissipation | Circulate. Cite Stam. |

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

None this meeting.


## Snippet

```glsl
vec2 p = uv - dt * vel; vec4 dye = texture(u_dye, p);
```

---

## Extra exercises

See [[GPU Programming/exercises/Week 06]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Unity Visual Effect Graph as the homework.
2. unstable huge dt.

## If we run long, cut

Full pressure solver. Keep advect + named project + layouts.

## If we run short, add

Dissipation on dye.
