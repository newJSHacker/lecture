# Lecture 2 — React state vs 3D

**Week 2 of 15** · Interactive Experience Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** useState, useFrame  
**Success check:** useFrame for motion.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `Interactive Experience/code/02-two-clocks.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: useState, useFrame | Invariant: 3D and DOM are two clocks`

## Board at the end (they photograph this)

```
state = discrete; frame = 60Hz
Two clocks.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** Two clocks. React re-renders are for **UI**.

**Ask:** useFrame for motion? Wait seven seconds. Take two answers.

**Board:** parked strip. Then state = discrete; frame = 60Hz.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *useState, useFrame*.

**Do not:** SetState({t}) every frame.

### Minutes 10–12 — Frame

**Say:** Today’s question: useState, useFrame. Kernel: useState, useFrame. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: setState({t}) every frame.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Two clocks. React re-renders are for **UI**.

**Say:** refs. `useRef` on a mesh to spin in useFrame without React render.

**Say:** Lifting state. Selected part id in React; color on the mesh from that id.

**Ask:** useFrame for motion? Wait seven seconds. Take two answers.

**They do:** On paper: jank demo: setState in useFrame then fix.

**Do not:** fight React state with the frame loop silently.

### Minutes 35–50 — Show

**Say:** Live demo: Click a box to select (state); spin in useFrame via ref.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** jank demo: setState in useFrame then fix.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: jank demo: setState in useFrame then fix.; dpr.. Homework: Written: when setState is wrong.; code.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: useState, useFrame | Plant the first common mistake. |
| 10–30 | Click a box to select (state); spin in useFrame via ref. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Interactive Experience/code/02-two-clocks.html` as the after-class check, not as the lecture.

---

## Lab

1. jank demo: setState in useFrame then fix.
2. dpr.

---

## Homework

1. Written: when setState is wrong.
2. code.

---

## Quiz next meeting (they hear this now)

1. useFrame vs useState (4)
2. why ref (3)
3. jank (3)


## Snippet

```jsx
useFrame((_, dt) => { ref.current.rotation.y += dt; });
```

---

## Extra exercises

See [[Interactive Experience/exercises/Week 02]].

---

## Notes you may still need (from the outline)

**1. Two clocks.** React re-renders are for **UI**. The WebGL loop is `useFrame`. Mixing them janks.

**2. refs.** `useRef` on a mesh to spin in useFrame without React render.

**3. Lifting state.** Selected part id in React; color on the mesh from that id.

---

## Common mistakes

1. setState({t}) every frame.
2. new material every render.

## If we run long, cut

Lifting state

## If we run short, add

dpr.
