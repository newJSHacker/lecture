# Lecture 9 — Geometric detail names

**Week 9 of 15** · Advanced Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** LOD, tessellation, Nanite idea  
**Success check:** LOD: swap meshes by distance.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `Advanced Computer Graphics/code/02-tracer.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: LOD, tessellation, Nanite idea | Invariant: local lighting is bounce 0; GI is the rest`

## Board at the end (they photograph this)

```
error in pixels
LOD rings.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** Why. Budgets from Blender/RTR meet **algorithm** names here.

**Ask:** LOD: swap meshes by distance? Wait seven seconds. Take two answers.

**Board:** parked strip. Then error in pixels.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *LOD, tessellation, Nanite idea*.

**Do not:** 'we used Nanite' on a glTF.

### Minutes 10–12 — Frame

**Say:** Today’s question: LOD, tessellation, Nanite idea. Kernel: LOD, tessellation, Nanite idea. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: 'we used Nanite' on a glTF.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Why. Budgets from Blender/RTR meet **algorithm** names here.

**Say:** Virtualized geometry. UE5 Nanite: cut only when you can explain visibility buffers at cartoon level.

**Say:** Web. drei `Detailed` / Three.js LOD.

**Ask:** LOD: swap meshes by distance? Wait seven seconds. Take two answers.

**They do:** On paper: hysteresis extra.

**Do not:** start with a production path tracer.

### Minutes 35–50 — Show

**Say:** Live demo: Three LOD meshes (or simplified boxes); switch; log tri count.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** hysteresis extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: hysteresis extra.; pixel error sentence.. Homework: Written: Nanite in 8 honest sentences.; LOD demo.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: LOD, tessellation, Nanite idea | Plant the first common mistake. |
| 10–30 | Three LOD meshes (or simplified boxes); switch; log tri count. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Advanced Computer Graphics/code/02-tracer.html` as the after-class check, not as the lecture.

---

## Lab

1. hysteresis extra.
2. pixel error sentence.

---

## Homework

1. Written: Nanite in 8 honest sentences.
2. LOD demo.

---

## Quiz next meeting (they hear this now)

1. LOD (3)
2. visibility buffer name (4)
3. why not in WebGL lab (3)


## Snippet

```js
lod.addLevel(high, 0); lod.addLevel(low, 20);
```

---

## Extra exercises

See [[Advanced Computer Graphics/exercises/Week 09]].

---

## Notes you may still need (from the outline)

**1. Why.** Budgets from Blender/RTR meet **algorithm** names here.

**2. Virtualized geometry.** UE5 Nanite: cut only when you can explain visibility buffers at cartoon level. Not a lab port.

**3. Web.** drei `Detailed` / Three.js LOD. That's the lab.

---

## Common mistakes

1. 'we used Nanite' on a glTF.
2. popping without hysteresis talk.

## If we run long, cut

Web

## If we run short, add

pixel error sentence.
