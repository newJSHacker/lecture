# Lecture 6 — glTF loading

**Week 6 of 15** · Three.js Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** GLTFLoader, scale, shadows  
**Success check:** GLTFLoader + DRACO name.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `ThreeJS Development/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: GLTFLoader, scale, shadows | Invariant: Three.js is an engine, not the algorithm`

## Board at the end (they photograph this)

```
model.scene
glTF box.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** Format. Blender course exports this.

**Ask:** GLTFLoader + DRACO name? Wait seven seconds. Take two answers.

**Board:** parked strip. Then model.scene.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *GLTFLoader, scale, shadows*.

**Do not:** Hotlinking huge sketchfab without credit.

### Minutes 10–12 — Frame

**Say:** Today’s question: GLTFLoader, scale, shadows. Kernel: GLTFLoader, scale, shadows. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: hotlinking huge sketchfab without credit.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Format. Blender course exports this.

**Say:** Async. loading manager.

**Say:** Demo. model load demo.

**Ask:** GLTFLoader + DRACO name? Wait seven seconds. Take two answers.

**They do:** On paper: error UI.

**Do not:** treat the inspector as the renderer. Local vendor only.

### Minutes 35–50 — Show

**Say:** Live demo: Load a tiny glTF (or a public example with license). Traverse set castShadow.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** error UI.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: error UI.; box3 center.. Homework: Written: why glTF.; Code: load.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: GLTFLoader, scale, shadows | Plant the first common mistake. |
| 10–30 | Load a tiny glTF (or a public example with license). Traverse set castShadow. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `ThreeJS Development/code/` as the after-class check, not as the lecture.

---

## Lab

1. error UI.
2. box3 center.

---

## Homework

1. Written: why glTF.
2. Code: load.

---

## Quiz next meeting (they hear this now)

1. who is scene (3)
2. traverse (4)
3. load in rAF? (3)


## Snippet

```js
loader.load('m.glb', (g) => scene.add(g.scene));
```

---

## Extra exercises

See [[ThreeJS Development/exercises/Week 06]].

---

## Notes you may still need (from the outline)

**1. Format.** Blender course exports this.

**2. Async.** loading manager. Placeholder cube.

**3. Demo.** model load demo.

---

## Common mistakes

1. hotlinking huge sketchfab without credit.
2. loading every frame.

## If we run long, cut

Demo

## If we run short, add

box3 center.
