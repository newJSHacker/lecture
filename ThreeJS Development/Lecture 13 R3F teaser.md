# Lecture 13 — R3F teaser

**Week 13 of 15** · Three.js Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** declarative three  
**Success check:** What R3F is.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 12 (10 min, paper or LMS).
- Demo: `ThreeJS Development/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 13 | Goal: declarative three | Invariant: Three.js is an engine, not the algorithm`

## Board at the end (they photograph this)

```
Canvas > mesh
JSX tree.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 12 quiz. Mark one item together. Then:

**Say:** Semester 5. Interactive Experience.

**Ask:** What R3F is? Wait seven seconds. Take two answers.

**Board:** parked strip. Then Canvas > mesh.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *declarative three*.

**Do not:** Abandoning the Three.js project to start R3F overnight.

### Minutes 10–12 — Frame

**Say:** Today’s question: declarative three. Kernel: declarative three. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: abandoning the Three.js project to start R3F overnight.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Semester 5. Interactive Experience.

**Say:** Mental model. Same scene graph.

**Say:** Demo. none required.

**Ask:** What R3F is? Wait seven seconds. Take two answers.

**They do:** On paper: table: R3F prop → Object3D.

**Do not:** treat the inspector as the renderer. Local vendor only.

### Minutes 35–50 — Show

**Say:** Live demo: Optional 20-line R3F cube if the lab has a bundler; else a slide mapping.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** table: R3F prop → Object3D.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: table: R3F prop → Object3D.; no full app.. Homework: Written: when R3F.; none.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: declarative three | Plant the first common mistake. |
| 10–30 | Optional 20-line R3F cube if the lab has a bundler; else a slide mapping. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `ThreeJS Development/code/` as the after-class check, not as the lecture.

---

## Lab

1. table: R3F prop → Object3D.
2. no full app.

---

## Homework

1. Written: when R3F.
2. none.

---

## Quiz next meeting (they hear this now)

1. R3F sits on (3)
2. useFrame is (4)
3. why wait (3)


## Snippet

```jsx
<mesh><boxGeometry/><meshStandardMaterial/></mesh>
```

---

## Extra exercises

See [[ThreeJS Development/exercises/Week 13]].

---

## Notes you may still need (from the outline)

**1. Semester 5.** Interactive Experience.

**2. Mental model.** Same scene graph.

**3. Demo.** none required.

---

## Common mistakes

1. abandoning the Three.js project to start R3F overnight.

## If we run long, cut

Demo

## If we run short, add

no full app.
