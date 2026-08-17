# Lecture 6 — SDF 2D

**Week 6 of 15** · Shader Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** circle, union, smooth  
**Success check:** Circle and box SDF.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `Shader Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: circle, union, smooth | Invariant: a shader is a program over pixels or vertices`

## Board at the end (they photograph this)

```
d = length(p)-r
CSG tree.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** Distance fields. A function that returns signed distance to a shape.

**Ask:** Circle and box SDF? Wait seven seconds. Take two answers.

**Board:** parked strip. Then d = length(p)-r.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *circle, union, smooth*.

**Do not:** Polygon meshes for a 2D logo in a shader course.

### Minutes 10–12 — Frame

**Say:** Today’s question: circle, union, smooth. Kernel: circle, union, smooth. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: polygon meshes for a 2D logo in a shader course.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Distance fields. A function that returns signed distance to a shape.

**Say:** CSG. min = union, max = intersection.

**Say:** Why. Logos, HUDs, 2D games, 3D modeling (Blender) all meet here.

**Ask:** Circle and box SDF? Wait seven seconds. Take two answers.

**They do:** On paper: onion (abs(d)-t) extra.

**Do not:** paste a 200-line Shadertoy as the first kernel.

### Minutes 35–50 — Show

**Say:** Live demo: A boolean logo (two circles minus a box).. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** onion (abs(d)-t) extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: onion (abs(d)-t) extra.; AA with fwidth.. Homework: Written: why signed.; Code: sdCircle + sdBox.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: circle, union, smooth | Plant the first common mistake. |
| 10–30 | A boolean logo (two circles minus a box). | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Shader Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. onion (abs(d)-t) extra.
2. AA with fwidth.

---

## Homework

1. Written: why signed.
2. Code: sdCircle + sdBox.

---

## Quiz next meeting (they hear this now)

1. union op (2)
2. smoothmin idea (4)
3. inside sign (4)


## Snippet

```glsl
float sdCircle(vec2 p, float r){ return length(p) - r; }
```

---

## Extra exercises

See [[Shader Programming/exercises/Week 06]].

---

## Notes you may still need (from the outline)

**1. Distance fields.** A function that returns signed distance to a shape. Rendering is `smoothstep` on d, or later sphere tracing in 3D.

**2. CSG.** min = union, max = intersection. Smoothmin blends.

**3. Why.** Logos, HUDs, 2D games, 3D modeling (Blender) all meet here. IQ's tables are the encyclopedia — students implement three primitives, not fifty.

---

## Common mistakes

1. polygon meshes for a 2D logo in a shader course.
2. unsigned distance only.

## If we run long, cut

Why

## If we run short, add

AA with fwidth.
