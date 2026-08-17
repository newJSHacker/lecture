# Lecture 7 — Camera matrices

**Week 7 of 15** · WebGL Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** P V M in the shader  
**Success check:** Reuse CG I lookAt/perspective if they have it.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `WebGL Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: P V M in the shader | Invariant: CPU fills buffers; GPU runs the shader; P*V*M; CCW`

## Board at the end (they photograph this)

```
gl_Position = P*V*M*pos
PVM.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** Same math. [[10 Computer Graphics I]] Weeks 7–9.

**Ask:** Reuse CG I lookAt/perspective if they have it? Wait seven seconds. Take two answers.

**Board:** parked strip. Then gl_Position = P*V*M*pos.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *P V M in the shader*.

**Do not:** Three.js camera as the lab.

### Minutes 10–12 — Frame

**Say:** Today’s question: P V M in the shader. Kernel: P V M in the shader. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Three.js camera as the lab.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Same math. [[10 Computer Graphics I]] Weeks 7–9.

**Say:** Three.js later. These uniforms are camera.projectionMatrix etc.

**Say:** Demo. 07 orbit.

**Ask:** Reuse CG I lookAt/perspective if they have it? Wait seven seconds. Take two answers.

**They do:** On paper: WASD extra.

**Do not:** wrap the first triangle in Three.js. Freeze conventions.

### Minutes 35–50 — Show

**Say:** Live demo: lookAt + perspective from JS mat4; spin the cube.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** WASD extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: WASD extra.; ortho toggle.. Homework: Written: mapping table CPU→uniform.; Code: orbit.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: P V M in the shader | Plant the first common mistake. |
| 10–30 | lookAt + perspective from JS mat4; spin the cube. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `WebGL Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. WASD extra.
2. ortho toggle.

---

## Homework

1. Written: mapping table CPU→uniform.
2. Code: orbit.

---

## Quiz next meeting (they hear this now)

1. product order (4)
2. lookAt (3)
3. fov radians (3)


## Snippet

```glsl
gl_Position = u_p * u_v * u_m * vec4(a_pos, 1.0);
```

---

## Extra exercises

See [[WebGL Programming/exercises/Week 07]].

---

## Notes you may still need (from the outline)

**1. Same math.** [[10 Computer Graphics I]] Weeks 7–9.

**2. Three.js later.** These uniforms are camera.projectionMatrix etc.

**3. Demo.** 07 orbit.

---

## Common mistakes

1. Three.js camera as the lab.
2. row-major P.

## If we run long, cut

Demo

## If we run short, add

ortho toggle.
