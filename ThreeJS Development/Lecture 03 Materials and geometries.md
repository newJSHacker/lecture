# Lecture 3 — Materials and geometries

**Week 3 of 15** · Three.js Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** BoxGeometry, Standard vs Basic  
**Success check:** Box/Sphere/Plane.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `ThreeJS Development/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: BoxGeometry, Standard vs Basic | Invariant: Three.js is an engine, not the algorithm`

## Board at the end (they photograph this)

```
MeshStandardMaterial
Material table.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** Basic. Unlit.

**Ask:** Box/Sphere/Plane? Wait seven seconds. Take two answers.

**Board:** parked strip. Then MeshStandardMaterial.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *BoxGeometry, Standard vs Basic*.

**Do not:** Leaking geometries in a loop.

### Minutes 10–12 — Frame

**Say:** Today’s question: BoxGeometry, Standard vs Basic. Kernel: BoxGeometry, Standard vs Basic. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: leaking geometries in a loop.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Basic. Unlit.

**Say:** Standard. PBR-ish.

**Say:** Custom. ShaderMaterial is shader course.

**Ask:** Box/Sphere/Plane? Wait seven seconds. Take two answers.

**They do:** On paper: wireframe toggle.

**Do not:** treat the inspector as the renderer. Local vendor only.

### Minutes 35–50 — Show

**Say:** Live demo: Three meshes three materials.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** wireframe toggle.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: wireframe toggle.; shared geometry.. Homework: Written: Basic vs Standard.; Code: trio.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: BoxGeometry, Standard vs Basic | Plant the first common mistake. |
| 10–30 | Three meshes three materials. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `ThreeJS Development/code/` as the after-class check, not as the lecture.

---

## Lab

1. wireframe toggle.
2. shared geometry.

---

## Homework

1. Written: Basic vs Standard.
2. Code: trio.

---

## Quiz next meeting (they hear this now)

1. unlit material (3)
2. dispose (4)
3. Standard is PBR? (3)


## Snippet

```js
new THREE.MeshStandardMaterial({ color: 0x8899aa, metalness: 0.1, roughness: 0.6 });
```

---

## Extra exercises

See [[ThreeJS Development/exercises/Week 03]].

---

## Notes you may still need (from the outline)

**1. Basic.** Unlit. Debug.

**2. Standard.** PBR-ish. Real-Time Rendering later.

**3. Custom.** ShaderMaterial is shader course.

---

## Common mistakes

1. leaking geometries in a loop.

## If we run long, cut

Custom

## If we run short, add

shared geometry.
