# Lecture 7 — Deferred review + tiled

**Week 7 of 15** · Advanced Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** G-buffer review; CPU tile lists for N lights; heatmap of overlap  
**Success check:** they can bin lights into screen tiles and say why 1000 Mesh helpers are not the algorithm

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `Advanced Computer Graphics/code/02-tracer.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: many lights as a data structure | Invariant: local lighting is bounce 0; GI is the rest`

## Board at the end (they photograph this)

```
forward dies at many lights
deferred: G-buffer, then lights
tiled: light indices per screen tile
clustered: 3D bins in the frustum (name)

heatmap overlay is a valid lab
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** Deferred and clustered exist because forward dies. 1000 Mesh point-light helpers are not the algorithm. No debug view fails. We do not start a production deferred engine.

**Ask:** If two lights overlap a tile, what does the tile store? Wait. Want: two indices.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *lights in tiles*.

**Do not:** 1000 Mesh point-light helpers as the algorithm.

### Minutes 10–12 — Frame

**Say:** Restate G-buffer from RTR. Clustered named. Cull by distance extra. Compare naive vs tiled count.

**Ask:** What lives in a G-buffer?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Many lights. Why forward dies.

**Board:** tiles. Light AABB → tiles.

**Say:** Heatmap. Count, do not invent fps.

**Ask:** Clustered vs tiled in one sentence?

**They do:** On paper: 4 tiles, 3 lights, who overlaps.

**Do not:** Start with a production path tracer.

### Minutes 35–50 — Show

**Say:** N point lights; 2D heatmap of overlapping lights per tile. Plant Mesh helpers as the method. Plant no debug view.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Assign lights to tiles (JS). Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: distance cull extra; naive vs tiled count. Homework: G-buffer restated. Quiz: tiles, G-buffer, not helpers. Next: midterm then shadow names.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | G-buffer recap | Plant production deferred. |
| 15–40 | Tile lists | Plant 1000 helpers. |
| 40–55 | Heatmap | No debug plant. |
| 55–60 | They count overlaps | Circulate. |

Point them at `Advanced Computer Graphics/code/02-tracer.html` as the after-class check, not as the lecture.

---

## Lab

1. cull by distance extra.
2. compare naive vs tiled count.

---

## Homework

1. Written: why tiles.
2. heatmap screenshot.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
// for each light, add index to tiles overlapping its screen AABB
```

---

## Extra exercises

See [[Advanced Computer Graphics/exercises/Week 07]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. 1000 Mesh point-light helpers as the algorithm.
2. no debug view.

## If we run long, cut

WebGL deferred impl. Keep CPU tiles + heatmap.

## If we run short, add

Naive vs tiled count.
