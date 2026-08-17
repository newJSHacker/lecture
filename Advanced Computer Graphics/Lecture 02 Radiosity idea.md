# Lecture 2 — Radiosity idea

**Week 2 of 15** · Advanced Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** patches + form factors; iterate B_i = E_i + ρ_i Σ F_ij B_j on a tiny system  
**Success check:** they can iterate a 2×2 made-up F and say radiosity is diffuse, view-independent

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `Advanced Computer Graphics/code/01-radiosity2.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: color bleed on paper, not a hemicube coder | Invariant: local lighting is bounce 0; GI is the rest`

## Board at the end (they photograph this)

```
B_i = E_i + ρ_i Σ_j F_ij B_j

2×2 F   made-up, honest
diffuse only     bad for mirrors

hemicube     named, not coded in full
lightmaps / probes     realtime cousins
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** Goral et al. Classic interiors. Full hemicube as required lab fails. Radiosity on a mirror sphere fails the model. Demo 01-radiosity2.html.

**Ask:** Does F_ij depend on the camera? Wait. Want: no — view-independent.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *patches, form factors*.

**Do not:** Full hemicube as required lab.

### Minutes 10–12 — Frame

**Say:** 4-patch room or 2-quad bleed. Iterate gather. Blender bake as oracle extra. Plot convergence extra.

**Ask:** Why is a mirror a bad radiosity customer?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Discretize. Patches.

**Board:** the gather formula. 2×2 F.

**Say:** Honesty: F from hemicube is a name.

**Ask:** What is a form factor in one sentence?

**They do:** One iteration on paper with made-up F.

**Do not:** Start with a production path tracer.

### Minutes 35–50 — Show

**Say:** Two-quad bleed with 2×2 F. Plant hemicube as required. Plant mirror radiosity. Plot a couple iterates.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** One gather iteration in JS or on paper. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: bake extra as oracle; plot convergence. Homework: view-independent paragraph. Quiz: patches, F, diffuse-only.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Patches on a room | Plant hemicube lab. |
| 15–40 | Iterate 2×2 | Plant mirror. |
| 40–55 | Convergence sketch | They plot. |
| 55–60 | They change ρ | Circulate. |

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

None this meeting.


## Snippet

```js
for (let k=0;k<20;k++) for (let i=0;i<n;i++) B[i] = E[i] + rho[i]*dotF(i,B);
```

---

## Extra exercises

See [[Advanced Computer Graphics/exercises/Week 02]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. full hemicube as required lab.
2. radiosity on a mirror sphere.

## If we run long, cut

Hemicube implementation. Keep 2×2 gather.

## If we run short, add

Plot B over iterations.
