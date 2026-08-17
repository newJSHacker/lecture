# Lecture 2 — React state vs 3D

**Week 2 of 15** · Interactive Experience Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** useState is the UI clock; useFrame + ref is the 3D clock  
**Success check:** they can show jank from setState every frame and move rotation onto a ref

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `Interactive Experience/code/02-two-clocks.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: select in React; spin in useFrame | Invariant: 3D and DOM are two clocks`

## Board at the end (they photograph this)

```
React clock     useState / click     re-render
WebGL clock     useFrame(_, dt)      mesh.ref

setState({ t }) every frame  =  jank
new Material() every render  =  leak
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** Last time: a graph. Today: two clocks. React re-renders are for HUD. The WebGL loop is useFrame. Mixing them is the live-coding crime of this course.

**Ask:** If a cube must spin, do you put t in useState? Wait. Want: no — ref + dt.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *useState, useFrame*.

**Do not:** SetState({t}) every frame.

### Minutes 10–12 — Frame

**Say:** Click selects (state). Spin uses useRef on the mesh. Lifting: selected id in React; color on the mesh from that id. We do not invent fps.

**Ask:** Why does a new material every render hurt?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Discrete UI vs per-frame motion. Write both clocks.

**Board:** setState({t}) crossed out. useFrame += dt on ref.current.rotation.

**Say:** Plant jank, then fix. Demo 02-two-clocks.html if R3F is down — same split: button vs rAF.

**Ask:** When is useState correct for 3D?

**They do:** On paper: selected id in React; rotation in useFrame. Two arrows.

**Do not:** Fight React state with the frame loop silently.

### Minutes 35–50 — Show

**Say:** Click a box to select; spin via ref. Plant setState in useFrame. Read the hitch out loud. Do not quote fps.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Move rotation onto a ref. Leave selected in useState. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: jank demo then fix; dpr. Homework: when setState is wrong. Quiz: useFrame vs useState, why ref, what jank is.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Click = state | Plant t in useState. |
| 10–30 | Spin via ref + dt | Plant setState every frame. |
| 30–45 | New material every render | Fix: one material. |
| 45–60 | They split the clocks | Circulate. |

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

None this meeting.


## Snippet

```jsx
useFrame((_, dt) => { ref.current.rotation.y += dt; });
```

---

## Extra exercises

See [[Interactive Experience/exercises/Week 02]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. setState({t}) every frame.
2. new material every render.

## If we run long, cut

Lifting state across routes. Keep two clocks.

## If we run short, add

dpr reminder on the Canvas.
