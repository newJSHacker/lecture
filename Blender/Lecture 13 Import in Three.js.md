# Lecture 13 — Import in Three.js

**Week 13 of 15** · Blender for Real-Time Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** scale, shadows, colors  
**Success check:** Load the glb in the existing Three.js demo pattern.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 12 (10 min, paper or LMS).
- Demo: `Blender/code/03-budget.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 13 | Goal: scale, shadows, colors | Invariant: units, facing, and budget travel with the asset`

## Board at the end (they photograph this)

```
loader.load → traverse shadows
Loader box.
1 m cube reference.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 12 quiz. Mark one item together. Then:

**Say:** The handshake. This week is the reason the course exists.

**Ask:** Load the glb in the existing Three.js demo pattern? Wait seven seconds. Take two answers.

**Board:** parked strip. Then loader.load → traverse shadows.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *scale, shadows, colors*.

**Do not:** Re-exporting 20 times without the viewer step.

### Minutes 10–12 — Frame

**Say:** Today’s question: scale, shadows, colors. Kernel: scale, shadows, colors. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Re-exporting 20 times without the viewer step.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** The handshake. This week is the reason the course exists.

**Say:** Bugs. Scale 0.01, black material (metal+rough+no env), inverted normals, missing UVs, animation not in export.

**Say:** Env. Standard material needs an environment to look like the Blender preview.

**Ask:** Load the glb in the existing Three.js demo pattern? Wait seven seconds. Take two answers.

**They do:** On paper: Shadow on a plane.

**Do not:** model at unknown scale. Do not skip apply rotation.

### Minutes 35–50 — Show

**Say:** Live demo: A 40-line loader page using local `ThreeJS/vendor/` showing the student glb + a directional light.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Shadow on a plane.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Shadow on a plane.; AxesHelper to check size.. Homework: Written: bug you hit and the fix.; URL or file:// note.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: scale, shadows, colors | Plant the first common mistake. |
| 10–30 | A 40-line loader page using local `ThreeJS/vendor/` showing the student glb + a directional light. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Blender/code/03-budget.html` as the after-class check, not as the lecture.

---

## Lab

1. Shadow on a plane.
2. AxesHelper to check size.

---

## Homework

1. Written: bug you hit and the fix.
2. URL or file:// note.

---

## Quiz next meeting (they hear this now)

1. traverse (3)
2. black metal cause (4)
3. Y-up (3)


## Snippet

```js
loader.load('crate.glb', (g) => scene.add(g.scene));
```

---

## Extra exercises

See [[Blender/exercises/Week 13]].

---

## Notes you may still need (from the outline)

**1. The handshake.** This week is the reason the course exists. Asset from Blender → [[18 Three.js Development]] loader.

**2. Bugs.** Scale 0.01, black material (metal+rough+no env), inverted normals, missing UVs, animation not in export.

**3. Env.** Standard material needs an environment to look like the Blender preview.

---

## Common mistakes

1. Re-exporting 20 times without the viewer step.
2. Unlit material to 'fix' black.

## If we run long, cut

Env

## If we run short, add

AxesHelper to check size.
