# Lecture 12 — Real-time budgets

**Week 12 of 15** · Blender for Real-Time Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** tris, batches, maps  
**Success check:** Count triangles.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `Blender/code/03-budget.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: tris, batches, maps | Invariant: units, facing, and budget travel with the asset`

## Board at the end (they photograph this)

```
table: platform → tri cap
Budget table.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** Budgets. Mobile vs desktop.

**Ask:** Count triangles? Wait seven seconds. Take two answers.

**Board:** parked strip. Then table: platform → tri cap.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *tris, batches, maps*.

**Do not:** Invented '60 fps' without a device.

### Minutes 10–12 — Frame

**Say:** Today’s question: tris, batches, maps. Kernel: tris, batches, maps. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Invented '60 fps' without a device.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Budgets. Mobile vs desktop.

**Say:** Batches. Each material can be a draw.

**Say:** Measure. Three.js `renderer.info` next week.

**Ask:** Count triangles? Wait seven seconds. Take two answers.

**They do:** On paper: Decimate extra and compare.

**Do not:** model at unknown scale. Do not skip apply rotation.

### Minutes 35–50 — Show

**Say:** Live demo: Fill a budget sheet for your crate/mug: tris, maps, materials.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Decimate extra and compare.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Decimate extra and compare.; One atlas vs three materials.. Homework: Written: budget table with **measured** counts.; If you cut, what you cut.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: tris, batches, maps | Plant the first common mistake. |
| 10–30 | Fill a budget sheet for your crate/mug: tris, maps, materials. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Blender/code/03-budget.html` as the after-class check, not as the lecture.

---

## Lab

1. Decimate extra and compare.
2. One atlas vs three materials.

---

## Homework

1. Written: budget table with **measured** counts.
2. If you cut, what you cut.

---

## Quiz next meeting (they hear this now)

1. draw call (3)
2. why atlas (4)
3. LOD (3)


## Snippet

```
tris | materials | 1024² maps | target platform
```

---

## Extra exercises

See [[Blender/exercises/Week 12]].

---

## Notes you may still need (from the outline)

**1. Budgets.** Mobile vs desktop. A student product viewer: tens of thousands of tris is plenty. A city: LOD and instancing (Three.js / WebGL courses).

**2. Batches.** Each material can be a draw. Atlas when you can. Don't make 40 materials for 40 bolts.

**3. Measure.** Three.js `renderer.info` next week. This week: a written budget for *their* asset.

---

## Common mistakes

1. Invented '60 fps' without a device.
2. Nanite speech on a crate.

## If we run long, cut

Measure

## If we run short, add

One atlas vs three materials.
