# Lecture 1 — The shader as a program

**Week 1 of 15** · Shader Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** VS writes a varying; GPU interpolates; FS reads it — v_uv as color  
**Success check:** they can pass v_uv from VS to FS and say who interpolates

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `WebGL/shadertoy/index.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: see interpolation as a program, not a filter | Invariant: a shader is a program over pixels or vertices; a clip you cannot uniform is not the lab`

## Board at the end (they photograph this)

```
VS  →  interpolate  →  FS

attribute  →  varying  →  gl_FragColor / out
uniform    (same for every vertex/pixel)

gl_Position is clip space
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** IGWT shaders are programs you pause, uniform, and debug — not a Shadertoy tab left playing. Mesh shaders live in WebGL Programming; today the same GLSL in a fullscreen triangle. If you cannot read a compile log, you will later call a missing varying a GPU driver bug.

**Ask:** Who interpolates the color between three vertices — you, the VS, or the rasterizer? Wait seven seconds.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *VS/FS, varyings*.

**Do not:** Shadertoy copy-paste into WebGL without #version.

### Minutes 8–12 — Frame

**Say:** Two homes: mesh VS/FS, and Shadertoy-style mainImage. We freeze WebGL2: #version 300 es and precision highp float in the fragment. Desktop GLSL paste without version is a fail.

**Ask:** Where does a uniform live — per vertex or once for the draw?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Draw vertex → interpolate → fragment. The arrow in the middle is hardware. A step in the VS stays a step after interpolation if every vertex wrote the same edge; a step in the FS is per pixel.

**Board:** varying vs uniform. Circle gl_Position: clip, not pixels.

**Say:** Normals must be renormalized in the FS — interpolation shortens them. No CDN; serve the local shadertoy harness.

**Ask:** Why highp in ES fragment shaders?

**They do:** On paper: VS that outputs v_uv; FS that paints vec4(v_uv,0,1). Label who interpolates.

**Do not:** Paste a 200-line Shadertoy as the first kernel.

### Minutes 35–50 — Show

**Say:** Demo WebGL/shadertoy/index.html. Pass v_uv as color. Plant a Shadertoy paste without #version — read the compile log out loud. Then a step() in VS vs the same step in FS.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Break interpolation: step in VS versus step in FS. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: interpolation break + compile logs. Homework: varying vs uniform; uv-as-color. Quiz: who interpolates, gl_Position space, precision.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Fullscreen triangle + v_uv | Plant Shadertoy paste without #version. |
| 10–30 | uv as color | Plant normalize only in VS. |
| 30–45 | Compile log | Read the error; do not hide it. |
| 45–60 | They break interpolation | Circulate. Pause time with a uniform if the harness has one. |

Point them at `WebGL/shadertoy/index.html` as the after-class check, not as the lecture.

---

## Lab

1. Break interpolation: output a step function in VS vs FS.
2. Read compile logs.

---

## Homework

1. Written: varying vs uniform.
2. Code: uv-as-color.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```glsl
#version 300 es
precision highp float;
in vec2 v_uv;
out vec4 c;
void main(){ c = vec4(v_uv, 0.0, 1.0); }
```

## Extra exercises

See [[Shader Programming/exercises/Week 01]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Shadertoy copy-paste into WebGL without #version.
2. Normalizing in VS only.

## If we run long, cut

Precision sermon. Keep VS→FS + compile log.

## If we run short, add

One uniform float to freeze time — the course contract.
