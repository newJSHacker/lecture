# Lecture 7 — Shading an SDF

**Week 7 of 15** · Shader Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** n = normalize(∇d) by central differences; Lambert n·ℓ  
**Success check:** they can estimate a 2D normal with finite differences and light it

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `Shader Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: light an SDF without an analytic n | Invariant: the normal is the gradient of the SDF; epsilon too big is a different shape`

## Board at the end (they photograph this)

```
e = 0.001   (too big: 0.1 on a tiny shape)

n.x = d(p+ex) - d(p-ex)
n.y = d(p+ey) - d(p-ey)
n = normalize(n)

Lambert: max(dot(n,L), 0)
PBR is RTR — not this hour
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** If they never compare analytic n to finite-difference n, they will trust a broken map() in week 9. Soft shadow is a name — week 9 marches. This week: N·L.

**Ask:** What happens if e=0.1 on a small circle? Wait.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *normals from gradient*.

**Do not:** Analytic n and finite-difference n never compared.

### Minutes 10–12 — Frame

**Say:** Gradient is ∇f. In 2D we fake a lit disk. Energy is still Lambert. Compare analytic (p/|p|) to FD once.

**Ask:** Why finite difference instead of only analytic?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Central differences. Tetrahedral is a name for 3D later.

**Board:** n from d. Circle e.

**Say:** Two lights extra is two dots added — still not a named PBR pass.

**Ask:** Write n.x in one line.

**They do:** On paper: analytic n of a circle vs FD sketch.

**Do not:** Paste a 200-line Shadertoy as the first kernel.

### Minutes 35–50 — Show

**Say:** Lit circle SDF; light-angle uniform. Plant e=0.1. Compare analytic vs FD on the board.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Two lights extra, or a Blinn specular extra. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: two lights or specular. Homework: why finite difference; normal2. Quiz: epsilon too big, n from d, Lambert. Midterm next week: gamma, uv, noise, fBm, SDF.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | FD normal | Plant e=0.1. |
| 10–30 | Lambert slider | Plant skipping analytic compare. |
| 30–45 | Pause light angle | Debug a still. |
| 45–60 | They add a second light | Circulate. |

Point them at `Shader Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. two lights extra.
2. specular blinn extra.

---

## Homework

1. Written: why finite difference.
2. Code: normal2.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```glsl
vec2 n = normalize(vec2(d(p+vec2(e,0))-d(p-vec2(e,0)), d(p+vec2(0,e))-d(p-vec2(0,e))));
```

---

## Extra exercises

See [[Shader Programming/exercises/Week 07]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. analytic n and finite-difference n never compared.
2. e=0.1 on a tiny shape.

## If we run long, cut

Energy conservation speech. Keep FD + Lambert.

## If we run short, add

Blinn specular as extra, named.
