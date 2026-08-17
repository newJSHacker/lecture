# Lecture 1 — R3F architecture

**Week 1 of 15** · Interactive Experience Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** Canvas, reconciler  
**Success check:** Create a Vite + R3F app.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `Interactive Experience/code/01-hud.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: Canvas, reconciler | Invariant: 3D and DOM are two clocks`

## Board at the end (they photograph this)

```
JSX tree = scene graph
JSX = graph.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** What R3F is. React Three Fiber is a **reconciler**: React state commits become Three.js object graphs.

**Ask:** Create a Vite + R3F app? Wait seven seconds. Take two answers.

**Board:** parked strip. Then JSX tree = scene graph.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *Canvas, reconciler*.

**Do not:** CRA 2018 tutorials.

### Minutes 8–12 — Frame

**Say:** Today’s question: Canvas, reconciler. Kernel: Canvas, reconciler. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: CRA 2018 tutorials.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** What R3F is. React Three Fiber is a **reconciler**: React state commits become Three.js object graphs.

**Say:** Why a course. Product sites, scroll stories, and HUDs need **UI + 3D**.

**Say:** Vite. Modules, JSX, fast refresh.

**Ask:** Create a Vite + R3F app? Wait seven seconds. Take two answers.

**They do:** On paper: color as a prop.

**Do not:** fight React state with the frame loop silently.

### Minutes 35–50 — Show

**Say:** Live demo: A box, orbit controls, ambient+dir. Same cube as Three.js week 1.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** color as a prop.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: color as a prop.; resize is default — still cap dpr.. Homework: Written: reconciler in 8 sentences.; repo.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: Canvas, reconciler | Plant the first common mistake. |
| 10–30 | A box, orbit controls, ambient+dir. Same cube as Three.js week 1. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Interactive Experience/code/01-hud.html` as the after-class check, not as the lecture.

---

## Lab

1. color as a prop.
2. resize is default — still cap dpr.

---

## Homework

1. Written: reconciler in 8 sentences.
2. repo.

---

## Quiz next meeting (they hear this now)

1. Canvas is (3)
2. mesh maps to (4)
3. why Vite (3)


## Snippet

```jsx
<Canvas camera={{ position: [0, 1, 4] }}>
  <mesh><boxGeometry/><meshStandardMaterial/></mesh>
</Canvas>
```

## Extra exercises

See [[Interactive Experience/exercises/Week 01]].

---

## Notes you may still need (from the outline)

**1. What R3F is.** React Three Fiber is a **reconciler**: React state commits become Three.js object graphs. It is not a different renderer math. [[18 Three.js Development]] still applies.

**2. Why a course.** Product sites, scroll stories, and HUDs need **UI + 3D**. R3F is how IGWT ships that without two competing scene graphs.

**3. Vite.** Modules, JSX, fast refresh. file:// will not work. `npm run dev`.

---

## Common mistakes

1. CRA 2018 tutorials.
2. no dpr cap.

## If we run long, cut

Vite

## If we run short, add

resize is default — still cap dpr.
