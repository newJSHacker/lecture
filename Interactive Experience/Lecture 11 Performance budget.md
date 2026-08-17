# Lecture 11 — Performance budget

**Week 11 of 15** · Interactive Experience Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** instancing, dpr, draw calls  
**Success check:** InstancedMesh / Instances.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `Interactive Experience/code/02-two-clocks.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: instancing, dpr, draw calls | Invariant: 3D and DOM are two clocks`

## Board at the end (they photograph this)

```
drei Instances; info.render
Budget.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** R3F cost. Each `<mesh>` is an object.

**Ask:** InstancedMesh / Instances? Wait seven seconds. Take two answers.

**Board:** parked strip. Then drei Instances; info.render.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *instancing, dpr, draw calls*.

**Do not:** Invented fps.

### Minutes 10–12 — Frame

**Say:** Today’s question: instancing, dpr, draw calls. Kernel: instancing, dpr, draw calls. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: invented fps.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** R3F cost. Each `<mesh>` is an object.

**Say:** Textures. Blender budgets still apply.

**Say:** Dev vs prod. Strict mode double-mount.

**Ask:** InstancedMesh / Instances? Wait seven seconds. Take two answers.

**They do:** On paper: dpr 1 vs 2.

**Do not:** fight React state with the frame loop silently.

### Minutes 35–50 — Show

**Say:** Live demo: 200 trees: naive vs instanced; log counts.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** dpr 1 vs 2.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: dpr 1 vs 2.; one table.. Homework: Written: measured table.; code.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: instancing, dpr, draw calls | Plant the first common mistake. |
| 10–30 | 200 trees: naive vs instanced; log counts. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. Instances (4)
2. dpr (3)
3. strict double (3)


## Snippet

```jsx
<Instances limit={200}>{/* ... */}</Instances>
```

---

## Extra exercises

See [[Interactive Experience/exercises/Week 11]].

---

## Notes you may still need (from the outline)

**1. R3F cost.** Each `<mesh>` is an object. Lists of 1k meshes should be instanced or drei `<Instances>`.

**2. Textures.** Blender budgets still apply.

**3. Dev vs prod.** Strict mode double-mount. Don't panic; dispose.

---

## Common mistakes

1. invented fps.
2. 500 MeshStandardMaterials.

## If we run long, cut

Dev vs prod

## If we run short, add

one table.
