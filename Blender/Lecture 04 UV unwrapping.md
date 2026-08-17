# Lecture 4 — UV unwrapping

**Week 4 of 15** · Blender for Real-Time Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** seams, islands, texel  
**Success check:** Mark seams on a crate.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `Blender/code/03-budget.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: seams, islands, texel | Invariant: units, facing, and budget travel with the asset`

## Board at the end (they photograph this)

```
cut seams, unwrap, pack
Seams on a cube.
Checker.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** Why UVs. The fragment shader samples a 2D image.

**Ask:** Mark seams on a crate? Wait seven seconds. Take two answers.

**Board:** parked strip. Then cut seams, unwrap, pack.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *seams, islands, texel*.

**Do not:** Smart UV project on a character as the only method.

### Minutes 10–12 — Frame

**Say:** Today’s question: seams, islands, texel. Kernel: seams, islands, texel. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Smart UV project on a character as the only method.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Why UVs. The fragment shader samples a 2D image.

**Say:** Seams. Put seams where they hide.

**Say:** Checker. Apply a checker grid material.

**Ask:** Mark seams on a crate? Wait seven seconds. Take two answers.

**They do:** On paper: Pack with a margin.

**Do not:** model at unknown scale. Do not skip apply rotation.

### Minutes 35–50 — Show

**Say:** Live demo: Unwrap the week-2 crate; checker; screenshot UV editor + 3D.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Pack with a margin.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Pack with a margin.; One overlap bug then fix.. Homework: Written: what a seam is.; UV screenshot.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: seams, islands, texel | Plant the first common mistake. |
| 10–30 | Unwrap the week-2 crate; checker; screenshot UV editor + 3D. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Blender/code/03-budget.html` as the after-class check, not as the lecture.

---

## Lab

1. Pack with a margin.
2. One overlap bug then fix.

---

## Homework

1. Written: what a seam is.
2. UV screenshot.

---

## Quiz next meeting (they hear this now)

1. island (3)
2. stretch symptom (4)
3. why checker (3)


## Snippet

```
U → Unwrap  |  UV editor → Pack Islands
```

---

## Extra exercises

See [[Blender/exercises/Week 04]].

---

## Notes you may still need (from the outline)

**1. Why UVs.** The fragment shader samples a 2D image. UVs are the mapping. Stretch = blur. Overlap = two faces share texels (lightmaps hate this; albedo sometimes OK for trim).

**2. Seams.** Put seams where they hide. Cylinders: one side seam + caps.

**3. Checker.** Apply a checker grid material. Even squares = good. Skinny rectangles = stretch.

---

## Common mistakes

1. Smart UV project on a character as the only method.
2. Tiny islands, giant waste.

## If we run long, cut

Checker

## If we run short, add

One overlap bug then fix.
