# Lecture 2 — Color and gamma

**Week 2 of 15** · Shader Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** linear vs sRGB  
**Success check:** Decode sRGB to linear for lighting.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `Shader Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: linear vs sRGB | Invariant: a shader is a program over pixels or vertices`

## Board at the end (they photograph this)

```
pow(c, 2.2) decode
Two gradients.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** CG I again. [[Computer Graphics/Lecture 11 Blinn Phong and Gamma]].

**Ask:** Decode sRGB to linear for lighting? Wait seven seconds. Take two answers.

**Board:** parked strip. Then pow(c, 2.2) decode.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *linear vs sRGB*.

**Do not:** Pow on normals.

### Minutes 10–12 — Frame

**Say:** Today’s question: linear vs sRGB. Kernel: linear vs sRGB. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: pow on normals.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** CG I again. [[Computer Graphics/Lecture 11 Blinn Phong and Gamma]].

**Say:** Where. Do lighting in linear.

**Say:** Textures. WebGL sRGB textures / `SRGB8_ALPHA8` names.

**Ask:** Decode sRGB to linear for lighting? Wait seven seconds. Take two answers.

**They do:** On paper: Light a Lambert quad in linear.

**Do not:** paste a 200-line Shadertoy as the first kernel.

### Minutes 35–50 — Show

**Say:** Live demo: Gradient with and without gamma encode; screenshot both.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Light a Lambert quad in linear.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Light a Lambert quad in linear.; Toggle encode.. Homework: Written: why lighting in sRGB looks wrong.; Code: encode helper.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: linear vs sRGB | Plant the first common mistake. |
| 10–30 | Gradient with and without gamma encode; screenshot both. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Shader Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. Light a Lambert quad in linear.
2. Toggle encode.

---

## Homework

1. Written: why lighting in sRGB looks wrong.
2. Code: encode helper.

---

## Quiz next meeting (they hear this now)

1. decode formula teaching (4)
2. double gamma (3)
3. albedo space (3)


## Snippet

```glsl
vec3 toLinear(vec3 c){ return pow(c, vec3(2.2)); }
vec3 toSRGB(vec3 c){ return pow(c, vec3(1.0/2.2)); }
```

---

## Extra exercises

See [[Shader Programming/exercises/Week 02]].

---

## Notes you may still need (from the outline)

**1. CG I again.** [[Computer Graphics/Lecture 11 Blinn Phong and Gamma]]. Now it is three lines in GLSL.

**2. Where.** Do lighting in linear. `pow(x, vec3(2.2))` is a teaching approximation, not a color-management product.

**3. Textures.** WebGL sRGB textures / `SRGB8_ALPHA8` names. Three.js `colorSpace`.

---

## Common mistakes

1. pow on normals.
2. Skipping encode and blaming the monitor.

## If we run long, cut

Textures

## If we run short, add

Toggle encode.
