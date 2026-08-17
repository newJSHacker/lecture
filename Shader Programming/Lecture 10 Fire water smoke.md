# Lecture 10 — Fire water smoke

**Week 10 of 15** · Shader Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** domain, lookup, noise  
**Success check:** Read [[WebGL/18 Shadertoy Effects]] and one of fire/water/smoke glsl.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `Shader Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: domain, lookup, noise | Invariant: a shader is a program over pixels or vertices`

## Board at the end (they photograph this)

```
uv distortion + fBm mask
Layers of fire.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** Catalog. Students **study** then **shrink**.

**Ask:** Read [[WebGL/18 Shadertoy Effects]] and one of fire/water/smoke glsl? Wait seven seconds. Take two answers.

**Board:** parked strip. Then uv distortion + fBm mask.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *domain, lookup, noise*.

**Do not:** Pasting aurora.glsl as the homework.

### Minutes 10–12 — Frame

**Say:** Today’s question: domain, lookup, noise. Kernel: domain, lookup, noise. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: pasting aurora.glsl as the homework.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Catalog. Students **study** then **shrink**.

**Say:** Water. Normals from height fBm; fresnel name; reflection as a gradient sky.

**Say:** Ethics. Comment what was copied.

**Ask:** Read [[WebGL/18 Shadertoy Effects]] and one of fire/water/smoke glsl? Wait seven seconds. Take two answers.

**They do:** On paper: one parameter that is yours.

**Do not:** paste a 200-line Shadertoy as the first kernel.

### Minutes 35–50 — Show

**Say:** Live demo: A 40-line fire or water; cite the catalog.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** one parameter that is yours.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: one parameter that is yours.; screenshot.. Homework: Written: three functions you reused.; Your GLSL.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: domain, lookup, noise | Plant the first common mistake. |
| 10–30 | A 40-line fire or water; cite the catalog. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Shader Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. one parameter that is yours.
2. screenshot.

---

## Homework

1. Written: three functions you reused.
2. Your GLSL.

---

## Quiz next meeting (they hear this now)

1. domain warp (3)
2. why cite (4)
3. fresnel name (3)


## Snippet

See `WebGL/shadertoy/fire.glsl` — then write a smaller `mainImage`.

---

## Extra exercises

See [[Shader Programming/exercises/Week 10]].

---

## Notes you may still need (from the outline)

**1. Catalog.** Students **study** then **shrink**. A 30-line fire is the lab, not 400 unread lines.

**2. Water.** Normals from height fBm; fresnel name; reflection as a gradient sky.

**3. Ethics.** Comment what was copied. Integrity: [[Teaching/12 Academic Integrity and AI]].

---

## Common mistakes

1. pasting aurora.glsl as the homework.
2. no citation.

## If we run long, cut

Ethics

## If we run short, add

screenshot.
