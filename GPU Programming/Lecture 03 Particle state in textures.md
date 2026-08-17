# Lecture 3 — Particle state in textures

**Week 3 of 15** · GPU Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** one texel = one particle; RG=pos, BA=vel; VS fetches by VertexID  
**Success check:** they can pack pos/vel into a FLOAT texture and draw points without 50k Mesh objects

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `GPU Programming/code/01-pong.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: SoA on the GPU you can draw | Invariant: neighbor texels are not spatial neighbors unless you build a grid`

## Board at the end (they photograph this)

```
state tex  (W×H FLOAT)
  texel (i,j):  RG = pos.xy    BA = vel.xy

vertex i:  u = i % W;  v = i / W
           texelFetch(state, ivec2(u,v), 0)

CPU loop of 50k Mesh  =  not this course
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** Structure of arrays on the GPU. Render: VS fetches by gl_VertexID. WebGL2 integer fetch. Instancing is a name from WebGL week 12. Invented particle counts are not measurements.

**Ask:** Why not one Mesh per particle? Wait. Want: draw-call / CPU death.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *pos in RG, vel in BA*.

**Do not:** CPU loop 50k Mesh objects.

### Minutes 10–12 — Frame

**Say:** N=64² is a teaching count they can see in the layout (64×64 texels). Points need a depth policy. Mouse force extra is a uniform.

**Ask:** How do you map VertexID to a texel?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Grid of texels. One particle per cell. Draw the RG/BA split.

**Board:** packing. Circle fetch.

**Say:** Reset button rewrites the texture from JS once — not every frame.

**Ask:** What is in BA?

**They do:** On paper: packing diagram for one particle.

**Do not:** Require CUDA. Stay in the browser (WebGL/WebGPU).

### Minutes 35–50 — Show

**Say:** N=64² falling with wrap; points. Plant 50k Mesh. Mouse force extra. Pause to inspect one texel as color.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Mouse force extra. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: mouse force + reset. Homework: packing paragraph; demo. Quiz: why not one mesh, RG pos, ID mapping.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Packing RG/BA | Plant 50k Mesh. |
| 10–30 | texelFetch by ID | Plant wrong % W. |
| 30–45 | Points + wrap | Depth policy. |
| 45–60 | Reset button | Circulate. Pause time. |

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

None this meeting.


## Snippet

```glsl
vec4 st = texelFetch(u_state, ivec2(gl_VertexID % W, gl_VertexID / W), 0);
```

---

## Extra exercises

See [[GPU Programming/exercises/Week 03]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. CPU loop 50k Mesh objects.
2. points without depth policy.

## If we run long, cut

Spatial hash grid. Keep packing + fetch + points.

## If we run short, add

Two textures if pos and vel split — still draw the layout.
