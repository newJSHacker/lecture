# Lecture 2 — Radiosity idea

**Week 2 of 15** · Advanced Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** patches, form factors  
**Success check:** Discretize a room into patches.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `Advanced Computer Graphics/code/01-radiosity2.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: patches, form factors | Invariant: local lighting is bounce 0; GI is the rest`

## Board at the end (they photograph this)

```
F_ij = fraction of energy i→j
Patches + arrows.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** Classic. Goral et al.

**Ask:** Discretize a room into patches? Wait seven seconds. Take two answers.

**Board:** parked strip. Then F_ij = fraction of energy i→j.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *patches, form factors*.

**Do not:** Full hemicube as required lab.

### Minutes 10–12 — Frame

**Say:** Today’s question: patches, form factors. Kernel: patches, form factors. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: full hemicube as required lab.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Classic. Goral et al.

**Say:** Teaching math. A 4-patch room: students compute a tiny linear system **or** iterate gather with made-up F_ij.

**Say:** Realtime cousins. Lightmaps baked in Blender.

**Ask:** Discretize a room into patches? Wait seven seconds. Take two answers.

**They do:** On paper: Blender lightmap bake extra as oracle.

**Do not:** start with a production path tracer.

### Minutes 35–50 — Show

**Say:** Live demo: Two-quad color bleed: iterate `B_i = E_i + ρ_i Σ F_ij B_j` with a 2×2 made-up F.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Blender lightmap bake extra as oracle.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Blender lightmap bake extra as oracle.; plot convergence.. Homework: Written: why diffuse-only.; spreadsheet or JS of the 2×2.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: patches, form factors | Plant the first common mistake. |
| 10–30 | Two-quad color bleed: iterate `B_i = E_i + ρ_i Σ F_ij B_j` with a 2×2 made-up F. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Advanced Computer Graphics/code/01-radiosity2.html` as the after-class check, not as the lecture.

---

## Lab

1. Blender lightmap bake extra as oracle.
2. plot convergence.

---

## Homework

1. Written: why diffuse-only.
2. spreadsheet or JS of the 2×2.

---

## Quiz next meeting (they hear this now)

1. form factor (4)
2. view independent (3)
3. mirrors (3)


## Snippet

```js
for (let k=0;k<20;k++) for (let i=0;i<n;i++) B[i] = E[i] + rho[i]*dotF(i,B);
```

---

## Extra exercises

See [[Advanced Computer Graphics/exercises/Week 02]].

---

## Notes you may still need (from the outline)

**1. Classic.** Goral et al. Diffuse-only. View-independent. Great for interiors; bad for mirrors.

**2. Teaching math.** A 4-patch room: students compute a tiny linear system **or** iterate gather with made-up F_ij. Honesty: F_ij from hemicube is named, not coded in full.

**3. Realtime cousins.** Lightmaps baked in Blender. Probes.

---

## Common mistakes

1. full hemicube as required lab.
2. radiosity on a mirror sphere.

## If we run long, cut

Realtime cousins

## If we run short, add

plot convergence.
