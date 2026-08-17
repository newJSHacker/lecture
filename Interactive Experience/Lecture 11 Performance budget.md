# Lecture 11 — Performance budget

**Week 11 of 15** · Interactive Experience Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** instance lists; cap dpr; count draw calls; do not invent fps  
**Success check:** they can replace a naive list of meshes with Instances and write a table without a fake fps number

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `Interactive Experience/code/02-two-clocks.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: a budget table, not a vibes number | Invariant: 3D and DOM are two clocks`

## Board at the end (they photograph this)

```
each <mesh> is an object
1k trees  →  InstancedMesh / <Instances>

dpr 1 vs 2     (cap)
draw calls     (count)

measure on a named device     or omit fps
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** A janky HUD over WebGL is last term. Today: R3F cost. Each mesh is an object. Invented fps still fail this program.

**Ask:** Is 200 <mesh> trees the same as 200 instances? Wait. Want: no.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *instancing, dpr, draw calls*.

**Do not:** Invented fps.

### Minutes 10–12 — Frame

**Say:** Textures still follow Blender budgets. Strict mode double-mount: do not panic; dispose. Dev vs prod named.

**Ask:** What do you write if you did not measure?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Count meshes. Then instance.

**Board:** naive vs Instances. dpr cap. empty fps cell if unmeasured.

**Say:** One table: device, dpr, what you cut. No fantasy 200 fps.

**Ask:** Why 500 MeshStandardMaterials hurt?

**They do:** On paper: two-row table, fps column blank or measured.

**Do not:** Fight React state with the frame loop silently.

### Minutes 35–50 — Show

**Say:** 200 trees naive vs instanced; log counts. Do not quote fps unless the profiler is on this machine. Plant invented 60.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Instances limit={200} or a smaller N they can count. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: dpr 1 vs 2; one table. Homework: budget paragraph. Quiz: Instances, dpr, do not invent fps.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Naive list | Plant 500 materials. |
| 15–40 | Instances | Count draw calls. |
| 40–55 | Table, no fake fps | Plant 200 fps. |
| 55–60 | They cap dpr | Circulate. |

Point them at `Interactive Experience/code/02-two-clocks.html` as the after-class check, not as the lecture.

---

## Lab

1. dpr 1 vs 2.
2. one table.

---

## Homework

1. Written: measured table.
2. code.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```jsx
<Instances limit={200}>{/* ... */}</Instances>
```

---

## Extra exercises

See [[Interactive Experience/exercises/Week 11]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. invented fps.
2. 500 MeshStandardMaterials.

## If we run long, cut

Renderer source dive. Keep instance + table.

## If we run short, add

One row: named device, dpr, cut.
