# Lecture 5 — Motion and drei helpers

**Week 5 of 15** · Interactive Experience Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** one motion library; CameraControls vs OrbitControls do not both own the camera  
**Success check:** they can spring or lerp one part on click and say which control is makeDefault

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `Interactive Experience/code/02-two-clocks.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: feel without fighting the camera | Invariant: 3D and DOM are two clocks`

## Board at the end (they photograph this)

```
pick one:  lerp    or    spring
do not: GSAP + spring + CSS on the same property

OrbitControls  vs  CameraControls
          makeDefault — one owner
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** Product sites use springs. Games often lerp. Two owners of the camera is a bug, not a style.

**Ask:** If Orbit and CameraControls both run, who wins? Wait. Want: a fight — pick makeDefault.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *easing, CameraControls*.

**Do not:** GSAP + spring + CSS all on one property.

### Minutes 10–12 — Frame

**Say:** drei helpers are oracles. Cleanup: geometries created in effects must dispose, or use JSX geometries. We freeze one library today.

**Ask:** What must unmount dispose?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Feel is a choice under constraint. One library.

**Board:** two control names. Cross out dual ownership.

**Say:** Mode toggle: orbit vs story camera. Story wins during the beat.

**Ask:** lerp vs spring in one sentence?

**They do:** On paper: click → spring position; orbit disabled while it runs.

**Do not:** Fight React state with the frame loop silently.

### Minutes 35–50 — Show

**Say:** Spring a part on click. Plant two controls. Fix makeDefault. Plant leaked geometry on hot reload.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** One spring or lerp on click. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: orbit vs story toggle; dispose note. Homework: which control owns the camera. Quiz: makeDefault, one library, dispose.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Lerp or spring one part | Plant three libraries. |
| 15–40 | makeDefault | Plant dual controls. |
| 40–55 | Dispose / JSX geom | Hot-reload leak. |
| 55–60 | They add a mode toggle | Circulate. |

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

None this meeting.


## Snippet

```jsx
<OrbitControls makeDefault />
```

---

## Extra exercises

See [[Interactive Experience/exercises/Week 05]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. GSAP + spring + CSS all on one property.
2. leaking geometries.

## If we run long, cut

Full CameraControls API. Keep one owner + one motion.

## If we run short, add

dispose note on a useLayoutEffect geometry.
