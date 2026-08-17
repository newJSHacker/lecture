# Lecture 4 — 3D from prompts

**Week 4 of 15** · AI for Interactive Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** inspect image-to-3D: normals, holes, scale, legal question — cleanup is the skill  
**Success check:** they can fill a table: gen mesh vs a crate (tris, UVs, scale) and not call the gen the homework

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `AI for Interactive Graphics/code/02-asset-table.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: inspection, not one-click mesh | Invariant: no secrets in the frontend; cite the model`

## Board at the end (they photograph this)

```
gen mesh → Blender cleanup → glTF
inspect: normals  holes  scale  UVs

we mention IP lawsuits     we do not play lawyer
one-click mesh as the whole HW  =  fail
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Wireframe of a gen mesh vs a crate | photograph |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** Tools improve; the teaching point is inspection. One-click mesh as the whole homework fails. We mention training-data lawsuits; we do not give legal advice.

**Ask:** If UVs are missing, is the mesh done? Wait. Want: no.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *limits of image-to-3D*.

**Do not:** One-click mesh as the whole homework.

### Minutes 10–12 — Frame

**Say:** Survey is allowed if tools cost money. Cleanup in Blender extra. Screenshot wireframe. Scale is meters.

**Ask:** What do you write instead of a legal conclusion?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Honesty. Limits of image-to-3D.

**Board:** inspect list. IP: mention, don't advise.

**Say:** Table: tris, UVs yes/no, scale vs student crate.

**Ask:** Why is cleanup the course skill?

**They do:** Empty table headers; they fill from a still or a file.

**Do not:** Put API keys in client JS. Skip integrity.

### Minutes 35–50 — Show

**Say:** Gen vs crate table. Plant one-click as HW. Plant a legal claim — strike. Wireframe screenshot.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Fill the inspection table. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: cleanup extra; wireframe. Homework: limits paragraph. Quiz: inspect list, no legal advice, cleanup.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Inspect list | Plant one-click HW. |
| 15–40 | Table vs crate | Plant no inspection. |
| 40–55 | No legal claims | Strike the sentence. |
| 55–60 | They screenshot wireframe | Circulate. |

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

None this meeting.


## Extra exercises

See [[AI for Interactive Graphics/exercises/Week 04]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. one-click mesh as the whole homework.
2. no inspection.

## If we run long, cut

IP seminar. Keep inspect + cleanup.

## If we run short, add

Wireframe screenshot.
