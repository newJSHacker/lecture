# Lecture 9 — Phong / Blinn in GLSL

**Week 9 of 15** · WebGL Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** varyings, gamma  
**Success check:** Blinn-Phong FS.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `WebGL Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: varyings, gamma | Invariant: CPU fills buffers; GPU runs the shader; P*V*M; CCW`

## Board at the end (they photograph this)

```
h = normalize(l+v)
Highlight.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** Same as CG I Week 11. Now in GLSL.

**Ask:** Blinn-Phong FS? Wait seven seconds. Take two answers.

**Board:** parked strip. Then h = normalize(l+v).

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *varyings, gamma*.

**Do not:** Gamma twice.

### Minutes 10–12 — Frame

**Say:** Today’s question: varyings, gamma. Kernel: varyings, gamma. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: gamma twice.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Same as CG I Week 11. Now in GLSL.

**Say:** Interpolation. normalize after interpolating n.

**Say:** Gamma. pow(c, vec3(1.0/2.2)).

**Ask:** Blinn-Phong FS? Wait seven seconds. Take two answers.

**They do:** On paper: gamma toggle.

**Do not:** wrap the first triangle in Three.js. Freeze conventions.

### Minutes 35–50 — Show

**Say:** Live demo: Blinn cube; shininess slider.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** gamma toggle.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: gamma toggle.; two lights extra.. Homework: Written: why normalize n in FS.; Code: blinn.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: varyings, gamma | Plant the first common mistake. |
| 10–30 | Blinn cube; shininess slider. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `WebGL Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. gamma toggle.
2. two lights extra.

---

## Homework

1. Written: why normalize n in FS.
2. Code: blinn.

---

## Quiz next meeting (they hear this now)

1. half vector (4)
2. gamma where (3)
3. PBR? (3)


## Snippet

```glsl
vec3 h = normalize(l + v);
```

---

## Extra exercises

See [[WebGL Programming/exercises/Week 09]].

---

## Notes you may still need (from the outline)

**1. Same as CG I Week 11.** Now in GLSL.

**2. Interpolation.** normalize after interpolating n.

**3. Gamma.** pow(c, vec3(1.0/2.2)).

---

## Common mistakes

1. gamma twice.
2. n not normalized.

## If we run long, cut

Gamma

## If we run short, add

two lights extra.
