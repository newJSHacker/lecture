# Lecture 7 — Deferred review + tiled

**Week 7 of 15** · Advanced Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** lights in tiles  
**Success check:** Restate G-buffer.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `Advanced Computer Graphics/code/02-tracer.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: lights in tiles | Invariant: local lighting is bounce 0; GI is the rest`

## Board at the end (they photograph this)

```
screen tiles → light lists
Grid overlay.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** Many lights. Deferred and clustered exist because forward dies.

**Ask:** Restate G-buffer? Wait seven seconds. Take two answers.

**Board:** parked strip. Then screen tiles → light lists.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *lights in tiles*.

**Do not:** 1000 Mesh point-light helpers as the algorithm.

### Minutes 10–12 — Frame

**Say:** Today’s question: lights in tiles. Kernel: lights in tiles. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: 1000 Mesh point-light helpers as the algorithm.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Many lights. Deferred and clustered exist because forward dies.

**Say:** Clustered. 3D bins in the frustum.

**Say:** WebGL. A light heatmap overlay is a valid lab.

**Ask:** Restate G-buffer? Wait seven seconds. Take two answers.

**They do:** On paper: cull by distance extra.

**Do not:** start with a production path tracer.

### Minutes 35–50 — Show

**Say:** Live demo: N point lights; heatmap of overlapping lights per tile (2D).. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** cull by distance extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: cull by distance extra.; compare naive vs tiled count.. Homework: Written: why tiles.; heatmap screenshot.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: lights in tiles | Plant the first common mistake. |
| 10–30 | N point lights; heatmap of overlapping lights per tile (2D). | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. tile list (4)
2. clustered (3)
3. heatmap (3)


## Snippet

```js
// for each light, add index to tiles overlapping its screen AABB
```

---

## Extra exercises

See [[Advanced Computer Graphics/exercises/Week 07]].

---

## Notes you may still need (from the outline)

**1. Many lights.** Deferred and clustered exist because forward dies. Students implement a **CPU** tile list for N lights on a 2D grid, or a heatmap fake.

**2. Clustered.** 3D bins in the frustum. Name.

**3. WebGL.** A light heatmap overlay is a valid lab.

---

## Common mistakes

1. 1000 Mesh point-light helpers as the algorithm.
2. no debug view.

## If we run long, cut

WebGL

## If we run short, add

compare naive vs tiled count.
