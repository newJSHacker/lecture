# Lecture 3 — Particle state in textures

**Week 3 of 15** · GPU Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** pos in RG, vel in BA  
**Success check:** Encode pos/vel in texels.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `GPU Programming/code/01-pong.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: pos in RG, vel in BA | Invariant: data lives where the kernel runs`

## Board at the end (they photograph this)

```
texel = particle
Texel grid.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** SoA on the GPU. Each texel is a particle.

**Ask:** Encode pos/vel in texels? Wait seven seconds. Take two answers.

**Board:** parked strip. Then texel = particle.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *pos in RG, vel in BA*.

**Do not:** CPU loop 50k Mesh objects.

### Minutes 10–12 — Frame

**Say:** Today’s question: pos in RG, vel in BA. Kernel: pos in RG, vel in BA. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: CPU loop 50k Mesh objects.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** SoA on the GPU. Each texel is a particle.

**Say:** Render. Vertex shader fetches texel by gl_VertexID / instance ID.

**Say:** WebGL2. Integer textures / fetch.

**Ask:** Encode pos/vel in texels? Wait seven seconds. Take two answers.

**They do:** On paper: mouse force extra.

**Do not:** require CUDA. WebGL/WebGPU in the browser.

### Minutes 35–50 — Show

**Say:** Live demo: N=64² particles falling with wrap; points.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** mouse force extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: mouse force extra.; reset button.. Homework: Written: packing.; demo.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: pos in RG, vel in BA | Plant the first common mistake. |
| 10–30 | N=64² particles falling with wrap; points. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `GPU Programming/code/01-pong.html` as the after-class check, not as the lecture.

---

## Lab

1. mouse force extra.
2. reset button.

---

## Homework

1. Written: packing.
2. demo.

---

## Quiz next meeting (they hear this now)

1. why not one mesh per particle (4)
2. RG pos (3)
3. ID mapping (3)


## Snippet

```glsl
vec4 st = texelFetch(u_state, ivec2(gl_VertexID % W, gl_VertexID / W), 0);
```

---

## Extra exercises

See [[GPU Programming/exercises/Week 03]].

---

## Notes you may still need (from the outline)

**1. SoA on the GPU.** Each texel is a particle. Neighbor particles are not spatial neighbors unless you design a grid.

**2. Render.** Vertex shader fetches texel by gl_VertexID / instance ID.

**3. WebGL2.** Integer textures / fetch. Instancing from WebGL week 12.

---

## Common mistakes

1. CPU loop 50k Mesh objects.
2. points without depth policy.

## If we run long, cut

WebGL2

## If we run short, add

reset button.
