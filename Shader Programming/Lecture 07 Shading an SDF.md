# Lecture 7 — Shading an SDF

**Week 7 of 15** · Shader Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** normals from gradient  
**Success check:** Estimate a 2D/3D normal with tetrahedral or central differences.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `Shader Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: normals from gradient | Invariant: a shader is a program over pixels or vertices`

## Board at the end (they photograph this)

```
n = normalize(vec3(d(p+e)-d(p-e)))
Gradient.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** Gradient. The normal is ∇f for an SDF f.

**Ask:** Estimate a 2D/3D normal with tetrahedral or central differences? Wait seven seconds. Take two answers.

**Board:** parked strip. Then n = normalize(vec3(d(p+e)-d(p-e))).

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *normals from gradient*.

**Do not:** Analytic n and finite-difference n never compared.

### Minutes 10–12 — Frame

**Say:** Today’s question: normals from gradient. Kernel: normals from gradient. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: analytic n and finite-difference n never compared.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Gradient. The normal is ∇f for an SDF f.

**Say:** Soft shadow name. IQ's `shadow` via raymarch — week 9.

**Say:** Energy. Still Lambert.

**Ask:** Estimate a 2D/3D normal with tetrahedral or central differences? Wait seven seconds. Take two answers.

**They do:** On paper: two lights extra.

**Do not:** paste a 200-line Shadertoy as the first kernel.

### Minutes 35–50 — Show

**Say:** Live demo: Lit circle SDF; light angle slider.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** two lights extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: two lights extra.; specular blinn extra.. Homework: Written: why finite difference.; Code: normal2.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: normals from gradient | Plant the first common mistake. |
| 10–30 | Lit circle SDF; light angle slider. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. epsilon too big (3)
2. n from d (4)
3. Lambert (3)


## Snippet

```glsl
vec2 n = normalize(vec2(d(p+vec2(e,0))-d(p-vec2(e,0)), d(p+vec2(0,e))-d(p-vec2(0,e))));
```

---

## Extra exercises

See [[Shader Programming/exercises/Week 07]].

---

## Notes you may still need (from the outline)

**1. Gradient.** The normal is ∇f for an SDF f. In 2D, light a 'height' or fake 3D with n.xy.

**2. Soft shadow name.** IQ's `shadow` via raymarch — week 9. This week: N·L.

**3. Energy.** Still Lambert. PBR is RTR course.

---

## Common mistakes

1. analytic n and finite-difference n never compared.
2. e=0.1 on a tiny shape.

## If we run long, cut

Energy

## If we run short, add

specular blinn extra.
