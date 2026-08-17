# Lecture 7 — Camera matrices

**Week 7 of 15** · WebGL Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** gl_Position = P * V * M * vec4(pos,1); lookAt + perspective in JS  
**Success check:** they upload P, V, M as column-major uniforms and orbit a cube without Three.js camera

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `WebGL Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: the camera is three matrices | Invariant: clip is after P; view looks −Z; do not invert the product order`

## Board at the end (they photograph this)

```
object → world(M) → view(V) → clip(P) → NDC → pixels

gl_Position = u_p * u_v * u_m * vec4(a_pos, 1.0);

RH Y-up   look −Z   CCW   column-major
fov in radians     near 0.1
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Optional: CG I lookAt diagram photograph | photo, not a Three.js screenshot |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** Same math as Computer Graphics I weeks 7–9. Three.js later will hide these as camera.projectionMatrix and matrixWorldInverse. Today you write them. Demo 07-orbit-camera.html.

**Ask:** Is the product M*V*P or P*V*M for column vectors on the right? Wait. Want: P*V*M.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *P V M in the shader*.

**Do not:** Three.js camera as the lab.

### Minutes 10–12 — Frame

**Say:** lookAt + perspective from a JS mat4. Freeze: no THREE.PerspectiveCamera in the lab. Row-major P is the classic 'my cube vanished.'

**Ask:** What space is gl_Position?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Spaces table from WebGL/01 Conventions. Circle clip.

**Board:** the one GLSL line. Names u_p u_v u_m.

**Say:** Orbit: move eye on a circle, lookAt origin. WASD is extra.

**Ask:** Does the VS divide by w?

**They do:** On paper: product order and what each matrix does.

**Do not:** Wrap the first triangle in Three.js. Unfreeze conventions.

### Minutes 35–50 — Show

**Say:** lookAt + perspective; spin the cube. Demo 07-orbit-camera.html. Plant Three.js camera. Plant row-major P. Plant fov in degrees without conversion.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Orbit, or WASD extra if orbit already works. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: WASD extra; ortho toggle. Homework: CPU→uniform mapping table; orbit. Quiz: product order, lookAt, fov radians. Midterm next week on 1–7.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Identity PVM — clip cube | They see last week's object. |
| 10–30 | perspective + lookAt | Plant degrees. Cube gone. |
| 30–45 | Orbit mouse/drag | Plant inverted V. |
| 45–60 | They orbit | Circulate. No Three.js. |

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

None this meeting.


## Snippet

```glsl
gl_Position = u_p * u_v * u_m * vec4(a_pos, 1.0);
```

---

## Extra exercises

See [[WebGL Programming/exercises/Week 07]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Three.js camera as the lab.
2. row-major P.

## If we run long, cut

WASD full controller. Keep P*V*M + orbit.

## If we run short, add

Ortho toggle vs perspective.
