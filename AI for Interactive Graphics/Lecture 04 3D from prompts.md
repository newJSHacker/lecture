# Lecture 4 — 3D from prompts

**Week 4 of 15** · AI for Interactive Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** limits of image-to-3D  
**Success check:** Try one image-to-3D **or** study papers/products as a survey if tools cost money.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `AI for Interactive Graphics/code/02-asset-table.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: limits of image-to-3D | Invariant: no secrets in the frontend; cite the model`

## Board at the end (they photograph this)

```
mesh quality vs glTF needs
Wireframe vs crate.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** Honesty. 2026 tools improve; the **teaching point** is inspection: normals, holes, scale, legal.

**Ask:** Try one image-to-3D **or** study papers/products as a survey if tools cost money? Wait seven seconds. Take two answers.

**Board:** parked strip. Then mesh quality vs glTF needs.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *limits of image-to-3D*.

**Do not:** One-click mesh as the whole homework.

### Minutes 10–12 — Frame

**Say:** Today’s question: limits of image-to-3D. Kernel: limits of image-to-3D. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: one-click mesh as the whole homework.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Honesty. 2026 tools improve; the **teaching point** is inspection: normals, holes, scale, legal.

**Say:** Pipeline. Gen mesh → Blender cleanup → glTF.

**Say:** IP. Training data lawsuits: mention, don't pretend to be a lawyer.

**Ask:** Try one image-to-3D **or** study papers/products as a survey if tools cost money? Wait seven seconds. Take two answers.

**They do:** On paper: one cleanup step in Blender extra.

**Do not:** put API keys in client JS. Do not skip integrity.

### Minutes 35–50 — Show

**Say:** Live demo: A table: gen mesh vs student crate (tris, UVs yes/no, scale).. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** one cleanup step in Blender extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: one cleanup step in Blender extra.; screenshot wireframe.. Homework: Written: 1 page limits.; table.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: limits of image-to-3D | Plant the first common mistake. |
| 10–30 | A table: gen mesh vs student crate (tris, UVs yes/no, scale). | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `AI for Interactive Graphics/code/02-asset-table.html` as the after-class check, not as the lecture.

---

## Lab

1. one cleanup step in Blender extra.
2. screenshot wireframe.

---

## Homework

1. Written: 1 page limits.
2. table.

---

## Quiz next meeting (they hear this now)

1. UV likely? (3)
2. why retopo (4)
3. IP mention (3)


## Extra exercises

See [[AI for Interactive Graphics/exercises/Week 04]].

---

## Notes you may still need (from the outline)

**1. Honesty.** 2026 tools improve; the **teaching point** is inspection: normals, holes, scale, legal.

**2. Pipeline.** Gen mesh → Blender cleanup → glTF. Cleanup is the course skill.

**3. IP.** Training data lawsuits: mention, don't pretend to be a lawyer.

---

## Common mistakes

1. one-click mesh as the whole homework.
2. no inspection.

## If we run long, cut

IP

## If we run short, add

screenshot wireframe.
