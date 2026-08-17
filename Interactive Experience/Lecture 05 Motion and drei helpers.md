# Lecture 5 — Motion and drei helpers

**Week 5 of 15** · Interactive Experience Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** easing, CameraControls  
**Success check:** Lerp vs spring (react-spring/drei).

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `Interactive Experience/code/02-two-clocks.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: easing, CameraControls | Invariant: 3D and DOM are two clocks`

## Board at the end (they photograph this)

```
spring vs lerp
Modes.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** Feel. Product sites use springs.

**Ask:** Lerp vs spring (react-spring/drei)? Wait seven seconds. Take two answers.

**Board:** parked strip. Then spring vs lerp.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *easing, CameraControls*.

**Do not:** GSAP + spring + CSS all on one property.

### Minutes 10–12 — Frame

**Say:** Today’s question: easing, CameraControls. Kernel: easing, CameraControls. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: GSAP + spring + CSS all on one property.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Feel. Product sites use springs.

**Say:** Camera. CameraControls vs OrbitControls.

**Say:** Cleanup. R3F unmount must dispose geometries if you create them in useLayoutEffect — or use JSX geometries.

**Ask:** Lerp vs spring (react-spring/drei)? Wait seven seconds. Take two answers.

**They do:** On paper: mode toggle orbit vs story.

**Do not:** fight React state with the frame loop silently.

### Minutes 35–50 — Show

**Say:** Live demo: Spring a camera or a part on click.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** mode toggle orbit vs story.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: mode toggle orbit vs story.; dispose note.. Homework: Written: spring vs lerp.; demo.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: easing, CameraControls | Plant the first common mistake. |
| 10–30 | Spring a camera or a part on click. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Interactive Experience/code/02-two-clocks.html` as the after-class check, not as the lecture.

---

## Lab

1. mode toggle orbit vs story.
2. dispose note.

---

## Homework

1. Written: spring vs lerp.
2. demo.

---

## Quiz next meeting (they hear this now)

1. conflict (4)
2. dispose (3)
3. one motion system (3)


## Snippet

```jsx
<OrbitControls makeDefault />
```

---

## Extra exercises

See [[Interactive Experience/exercises/Week 05]].

---

## Notes you may still need (from the outline)

**1. Feel.** Product sites use springs. Games often lerp. Pick one library and stay.

**2. Camera.** CameraControls vs OrbitControls. Conflict is a common bug.

**3. Cleanup.** R3F unmount must dispose geometries if you create them in useLayoutEffect — or use JSX geometries.

---

## Common mistakes

1. GSAP + spring + CSS all on one property.
2. leaking geometries.

## If we run long, cut

Cleanup

## If we run short, add

dispose note.
