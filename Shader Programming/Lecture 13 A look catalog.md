# Lecture 13 — A look catalog

**Week 13 of 15** · Shader Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** portfolio of 4 looks  
**Success check:** Four fullscreen looks: pattern, noise, SDF, march-or-post.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 12 (10 min, paper or LMS).
- Demo: `Shader Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 13 | Goal: portfolio of 4 looks | Invariant: a shader is a program over pixels or vertices`

## Board at the end (they photograph this)

```
four thumbnails
Contact sheet.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 12 quiz. Mark one item together. Then:

**Say:** Craft. A shader portfolio is a set of **controlled** images, not a random Shadertoy account.

**Ask:** Four fullscreen looks: pattern, noise, SDF, march-or-post? Wait seven seconds. Take two answers.

**Board:** parked strip. Then four thumbnails.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *portfolio of 4 looks*.

**Do not:** Four identical fBm screenshots.

### Minutes 10–12 — Frame

**Say:** Today’s question: portfolio of 4 looks. Kernel: portfolio of 4 looks. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: four identical fBm screenshots.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Craft. A shader portfolio is a set of **controlled** images, not a random Shadertoy account.

**Say:** Parameters. Uniforms: time pause, one slider that matters.

**Say:** Next. RTR will put these ideas on meshes with PBR.

**Ask:** Four fullscreen looks: pattern, noise, SDF, march-or-post? Wait seven seconds. Take two answers.

**They do:** On paper: pause time.

**Do not:** paste a 200-line Shadertoy as the first kernel.

### Minutes 35–50 — Show

**Say:** Live demo: Gallery page linking four HTML/GLSL files (can reuse WebGL shadertoy harness).. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** pause time.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: pause time.; one original twist per look.. Homework: Written: one paragraph per look.; repo.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: portfolio of 4 looks | Plant the first common mistake. |
| 10–30 | Gallery page linking four HTML/GLSL files (can reuse WebGL shadertoy harness). | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Shader Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. pause time.
2. one original twist per look.

---

## Homework

1. Written: one paragraph per look.
2. repo.

---

## Quiz next meeting (they hear this now)

1. uniform vs baked (3)
2. why pause (3)
3. citation (4)


## Extra exercises

See [[Shader Programming/exercises/Week 13]].

---

## Notes you may still need (from the outline)

**1. Craft.** A shader portfolio is a set of **controlled** images, not a random Shadertoy account.

**2. Parameters.** Uniforms: time pause, one slider that matters.

**3. Next.** RTR will put these ideas on meshes with PBR.

---

## Common mistakes

1. four identical fBm screenshots.

## If we run long, cut

Next

## If we run short, add

one original twist per look.
