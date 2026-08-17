# Lecture 9 — Ray marched lighting

**Week 9 of 15** · Shader Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** soft shadow, AO names  
**Success check:** Secondary march toward the light.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `Shader Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: soft shadow, AO names | Invariant: a shader is a program over pixels or vertices`

## Board at the end (they photograph this)

```
shadow ray toward L
Two rays.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** Shadows. If map(p) hits before the light, it's shadowed.

**Ask:** Secondary march toward the light? Wait seven seconds. Take two answers.

**Board:** parked strip. Then shadow ray toward L.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *soft shadow, AO names*.

**Do not:** Stencil shadows speech.

### Minutes 10–12 — Frame

**Say:** Today’s question: soft shadow, AO names. Kernel: soft shadow, AO names. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: stencil shadows speech.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Shadows. If map(p) hits before the light, it's shadowed.

**Say:** AO. Sample SDF along normal.

**Say:** Materials. Albedo per object id from the map() return.

**Ask:** Secondary march toward the light? Wait seven seconds. Take two answers.

**They do:** On paper: AO toggle.

**Do not:** paste a 200-line Shadertoy as the first kernel.

### Minutes 35–50 — Show

**Say:** Live demo: Sphere+plane with a soft-ish shadow.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** AO toggle.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: AO toggle.; material id extra.. Homework: Written: why second march.; Code: shadow().. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: soft shadow, AO names | Plant the first common mistake. |
| 10–30 | Sphere+plane with a soft-ish shadow. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Shader Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. AO toggle.
2. material id extra.

---

## Homework

1. Written: why second march.
2. Code: shadow().

---

## Quiz next meeting (they hear this now)

1. hit before light (4)
2. soft idea (3)
3. AO (3)


## Snippet

```glsl
float shadow(vec3 p, vec3 l){ /* march toward l, return 0 if blocked */ }
```

---

## Extra exercises

See [[Shader Programming/exercises/Week 09]].

---

## Notes you may still need (from the outline)

**1. Shadows.** If map(p) hits before the light, it's shadowed. Soft: track minimum d/t.

**2. AO.** Sample SDF along normal. Darken crevices. Fake, fast.

**3. Materials.** Albedo per object id from the map() return.

---

## Common mistakes

1. stencil shadows speech.
2. AO as SSAO from RTR without saying so.

## If we run long, cut

Materials

## If we run short, add

material id extra.
