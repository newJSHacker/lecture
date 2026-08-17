# Lecture 2 — Mesh modeling

**Week 2 of 15** · Blender for Real-Time Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** verts edges faces  
**Success check:** Extrude, inset, loop cut.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `Blender/code/02-export.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: verts edges faces | Invariant: units, facing, and budget travel with the asset`

## Board at the end (they photograph this)

```
quad vs triangle vs n-gon
Quad grid.
Red/blue faces.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** Topology. Real-time cares about **triangle count** and **deformation**.

**Ask:** Extrude, inset, loop cut? Wait seven seconds. Take two answers.

**Board:** parked strip. Then quad vs triangle vs n-gon.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *verts edges faces*.

**Do not:** Sculpting a hero as week-2 homework.

### Minutes 10–12 — Frame

**Say:** Today’s question: verts edges faces. Kernel: verts edges faces. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Sculpting a hero as week-2 homework.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Topology. Real-time cares about **triangle count** and **deformation**.

**Say:** Operators. E extrude, I inset, Ctrl+R loop cut, G/S/R.

**Say:** Ngons. Allowed on flat caps.

**Ask:** Extrude, inset, loop cut? Wait seven seconds. Take two answers.

**They do:** On paper: A table with 4 legs (keep them separate objects or one mesh — justify).

**Do not:** model at unknown scale. Do not skip apply rotation.

### Minutes 35–50 — Show

**Say:** Live demo: Model a simple mug or crate from a cube. Show face orientation. Report triangle count.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** A table with 4 legs (keep them separate objects or one mesh — justify).

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: A table with 4 legs (keep them separate objects or one mesh — justify).; Screenshot statistics.. Homework: Written: quad vs tri in real-time.; Blend file + triangle count.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: verts edges faces | Plant the first common mistake. |
| 10–30 | Model a simple mug or crate from a cube. Show face orientation. Report triangle count. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. extrude (2)
2. why face orientation (4)
3. n-gon risk (4)


## Snippet

```
Viewport overlays → Statistics, Face Orientation
```

---

## Extra exercises

See [[Blender/exercises/Week 02]].

---

## Notes you may still need (from the outline)

**1. Topology.** Real-time cares about **triangle count** and **deformation**. Film cares about subdivision beauty. Prefer quads on deforming surfaces; triangles are what glTF stores anyway.

**2. Operators.** E extrude, I inset, Ctrl+R loop cut, G/S/R. Merge by distance. Face orientation overlay (blue/red).

**3. Ngons.** Allowed on flat caps. Dangerous on curves. Overlay: Face orientation + statistics.

---

## Common mistakes

1. Sculpting a hero as week-2 homework.
2. Inverted normals shipped to Three.js.

## If we run long, cut

Ngons

## If we run short, add

Screenshot statistics.
