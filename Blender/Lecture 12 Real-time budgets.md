# Lecture 12 — Real-time budgets

**Week 12 of 15** · Blender for Real-Time Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** budget sheet: tris, batches/materials, map size; measure; no invented fps  
**Success check:** they fill Blender/code/03-budget.html with measured counts for their asset and can say why 40 materials are 40 draws

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `Blender/code/03-budget.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: numbers you measured | Invariant: a frame is a budget; Nanite speeches on a crate are off-topic; never invent 60 fps`

## Board at the end (they photograph this)

```
tris        materials/batches        maps (1024²)        device
fill with measured numbers

each material can be a draw
atlas when you can     don't 40 materials for 40 bolts

LOD / instancing  —  Three.js / WebGL courses
no invented fps
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** A student product viewer: tens of thousands of tris is plenty. Invented '60 fps' without a device is a fail. Nanite speech on a crate is a fail. Sheet: 03-budget.html.

**Ask:** If you have 40 unique materials on 40 bolts, what happens at draw-call time? Wait. Want: up to 40 draws.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *tris, batches, maps*.

**Do not:** Invented '60 fps' without a device.

### Minutes 10–12 — Frame

**Say:** Mobile vs desktop as a column, not a fps. Decimate extra and compare measured tris. renderer.info is next week in Three — this week the written sheet.

**Ask:** Why atlas?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Budget columns. Device named (their laptop).

**Board:** the table from 03-budget.html.

**Say:** Plant invented 60 fps. Plant Nanite.

**Ask:** What do you write if you have not measured?

**They do:** Fill the table headers; leave numbers blank until they count.

**Do not:** Model at unknown scale. Skip apply rotation.

### Minutes 35–50 — Show

**Say:** Count tris on the crate; count materials; map sizes. Demo 03-budget.html. Plant 60 fps. Plant Nanite.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Decimate extra and compare measured tris. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: decimate compare; one atlas vs three materials. Homework: budget table measured; what you cut. Quiz: draw call, why atlas, LOD name. Three.js import next.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Statistics tris | Write the number. |
| 10–30 | Materials = batches | Plant 40 bolt mats. |
| 30–45 | map 1024 vs 4k | Budget, not flex. |
| 45–60 | They fill 03-budget.html | No invented fps. |

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

None this meeting.


## Snippet

```
tris | materials | 1024² maps | target platform
```

---

## Extra exercises

See [[Blender/exercises/Week 12]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Invented '60 fps' without a device.
2. Nanite speech on a crate.

## If we run long, cut

City-scale LOD design. Keep their asset's sheet.

## If we run short, add

One atlas vs three materials.
