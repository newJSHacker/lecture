# Lecture 8 — Midterm and loading UX

**Week 8 of 15** · Interactive Experience Development  
**Meeting:** written midterm, then leftover lecture + live coding  
**Kernel (after the exam):** midterm; Suspense  
**Success check:** they sit the exam; after, they can state the leftover kernel in one sentence

This meeting is an **exam**, then a short class. It is not a normal content lecture. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Printed midterm + spare paper. No laptop for the exam.
- Topic list was announced at the end of Lecture 7.
- After collection: demo `Interactive Experience/code/02-two-clocks.html` ready (local, no CDN).
- Parked strip (uncover after the exam): `Lecture 8 | Goal: leftover kernel | Invariant: 3D and DOM are two clocks`

## Midterm (about 50–60 min)

Written. No laptop. Weeks 1–7.

**Topics:** Sit midterm: reconciler, state vs frame, HUD, scroll, audio, physics-oracle., useLoader / Suspense., Progress bar., Don't freeze the tab on a 50MB glb.

Collect. Do not mark in silence for the rest of the hour — uncover the leftover lecture.

## Board at the end (after the exam; they photograph this)

```
fallback = progress
Fallback.
```

## Slides today (cap: 2)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## After the exam (~15–25 min lecture)

**Say:** The exam is over. The leftover kernel is on the parked strip.

**Ask:** useLoader / Suspense.

**They do:** copy the leftover board.

**Do not:** start a new project in the exam hour. Do not skip the leftover kernel if 15 minutes remain.

**2. Loading.** drei `useProgress`. Placeholder cube. Compress glb (Blender course).

**3. UX.** Timeout message. Reduce motion still applies.

### Show / attempt if time

**Say:** Suspense fallback while a glTF loads (or a fake delay).

---

**They do:** error if missing file.

---

## Live coding (remaining time)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: midterm; Suspense | Plant the first common mistake. |
| 10–30 | Suspense fallback while a glTF loads (or a fake delay). | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

---

## Lab

1. error if missing file.
2. progress %.

---

## Homework

1. Reflection + loading screenshot.

---

## Quiz next meeting

None this week — midterm. Next quiz is Lecture 9.

## Extra exercises

See [[Interactive Experience/exercises/Week 08]].

## If we run long, cut

Live coding. Keep the leftover board.

## If we run short, add

One more worked leftover example.
