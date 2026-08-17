# Lecture 1 — The shader as a program

**Week 1 of 15** · Shader Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** VS/FS, varyings  
**Success check:** Write a vertex shader that passes a varying.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `WebGL/shadertoy/index.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: VS/FS, varyings | Invariant: a shader is a program over pixels or vertices`

## Board at the end (they photograph this)

```
vertex → interpolate → fragment
Pipeline.
Varying arrows.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** Two homes. Mesh shaders live in [[17 WebGL Programming]].

**Ask:** a vertex shader that passes a varying? Wait seven seconds. Take two answers.

**Board:** parked strip. Then vertex → interpolate → fragment.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *VS/FS, varyings*.

**Do not:** Shadertoy copy-paste into WebGL without #version.

### Minutes 8–12 — Frame

**Say:** Today’s question: VS/FS, varyings. Kernel: VS/FS, varyings. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Shadertoy copy-paste into WebGL without #version.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Two homes. Mesh shaders live in [[17 WebGL Programming]].

**Say:** Interpolation. VS outputs are interpolated.

**Say:** Precision. `precision highp float` in ES fragment shaders.

**Ask:** a vertex shader that passes a varying? Wait seven seconds. Take two answers.

**They do:** On paper: Break interpolation: output a step function in VS vs FS.

**Do not:** paste a 200-line Shadertoy as the first kernel.

### Minutes 35–50 — Show

**Say:** Live demo: WebGL2: pass v_uv and display as color. Then the same idea in a fullscreen triangle.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Break interpolation: output a step function in VS vs FS.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Break interpolation: output a step function in VS vs FS.; Read compile logs.. Homework: Written: varying vs uniform.; Code: uv-as-color.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: VS/FS, varyings | Plant the first common mistake. |
| 10–30 | WebGL2: pass v_uv and display as color. Then the same idea in a fullscreen triangle. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. who interpolates (4)
2. gl_Position space (3)
3. precision (3)


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

**1. Two homes.** Mesh shaders live in [[17 WebGL Programming]]. Fullscreen procedural live in Shadertoy-style `mainImage(out vec4, in vec2)` — [[WebGL/shadertoy/index.html]]. This course uses both.

**2. Interpolation.** VS outputs are interpolated. That is why a color at three vertices becomes a gradient. Normals must be renormalized in the FS.

**3. Precision.** `precision highp float` in ES fragment shaders. Desktop GLSL is looser — do not copy Shadertoy 1:1 into WebGL without version and precision.

---

## Common mistakes

1. Shadertoy copy-paste into WebGL without #version.
2. Normalizing in VS only.

## If we run long, cut

Precision

## If we run short, add

Read compile logs.
