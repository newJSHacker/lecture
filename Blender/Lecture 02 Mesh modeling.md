# Lecture 2 — Mesh modeling

**Week 2 of 15** · Blender for Real-Time Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** verts, edges, faces; extrude / inset / loop cut; face orientation  
**Success check:** they can extrude a crate and turn on face orientation; they do not sculpt a hero

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `Blender/code/02-export.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: a crate, not a film character | Invariant: real-time cares about triangle count and facing; inverted normals ship as inside-out in the engine`

## Board at the end (they photograph this)

```
E extrude   I inset   Ctrl+R loop cut   G/S/R
Merge by distance

Face orientation: blue front / red back
Statistics: tris     (glTF stores triangles)

ngons OK on flat caps; dangerous on curves
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** Film cares about subdivision beauty. We care about tris and deformation. Inverted normals shipped to Three.js are a facing bug — the engine is not the bug.

**Ask:** Why turn on face orientation this week? Wait. Want: red faces will be inside-out in glTF.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *verts edges faces*.

**Do not:** Sculpting a hero as week-2 homework.

### Minutes 10–12 — Frame

**Say:** Quads on deforming surfaces; triangles are what glTF stores anyway. Ngons named. Statistics overlay. No hero sculpt as homework.

**Ask:** Quad vs tri in real-time — who triangulates?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Operators. Overlay on.

**Board:** E I Ctrl+R. Blue/red.

**Say:** A table with four legs — separate objects or one mesh, they justify.

**Ask:** What does red mean on face orientation?

**They do:** On paper: a crate in 8–12 boxes (faces).

**Do not:** Model at unknown scale. Skip apply rotation.

### Minutes 35–50 — Show

**Say:** Block a crate; overlay; statistics. Plant sculpting a hero. Plant inverted faces.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Extrude a crate. Screenshot statistics. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: table with 4 legs; statistics screenshot. Homework: quad vs tri; blend + triangle count. Quiz: extrude, why face orientation, n-gon risk.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Face orientation on | Plant skipped overlay. |
| 10–30 | Extrude crate | Plant ngons on a curve. |
| 30–45 | Statistics tris | They read the number. |
| 45–60 | They merge by distance | Circulate. |

Point them at `Blender/code/02-export.html` as the after-class check, not as the lecture.

---

## Lab

1. A table with 4 legs (keep them separate objects or one mesh — justify).
2. Screenshot statistics.

---

## Homework

1. Written: quad vs tri in real-time.
2. Blend file + triangle count.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```
Viewport overlays → Statistics, Face Orientation
```

---

## Extra exercises

See [[Blender/exercises/Week 02]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Sculpting a hero as week-2 homework.
2. Inverted normals shipped to Three.js.

## If we run long, cut

Sculpt. Keep crate + facing + count.

## If we run short, add

Screenshot statistics on the crate.
