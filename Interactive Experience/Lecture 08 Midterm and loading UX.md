# Lecture 8 — Midterm and loading UX

**Week 8 of 15** · Interactive Experience Development  
**Meeting:** written midterm, then leftover lecture + live coding  
**Kernel (after the exam):** midterm; then Suspense / useLoader with a fallback and a missing-file error  
**Success check:** after the exam they can show a fallback while a glTF loads and a visible error if it 404s

This meeting is an **exam**, then a short class. It is not a normal content lecture. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Printed midterm + spare paper. No laptop for the exam.
- Topic list was announced at the end of Lecture 7.
- After collection: demo `Interactive Experience/code/02-two-clocks.html` ready (local, no CDN).
- Parked strip (uncover after the exam): `Lecture 8 | Goal: leftover kernel | Invariant: 3D and DOM are two clocks`

## Midterm (about 50–60 min)

Written. No laptop. Weeks 1–7.

**Topics:** reconciler/Canvas; two clocks; HUD pointer-events; scroll 0–1; one motion library + camera owner; analyser gesture; physics as oracle.

Collect. Do not mark in silence for the rest of the hour — uncover the leftover lecture.

## Board at the end (after the exam; they photograph this)

```
<Suspense fallback={placeholder}>
  <Model />
</Suspense>

missing glTF  →  visible error, not a black canvas
useProgress  =  name; % is measured, not invented
```

## Slides today (cap: 2)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## After the exam (~15–25 min lecture)

**Say:** This meeting is a **midterm**, then loading UX. No laptop for the exam. After: a black screen while a glTF loads is not mysterious — it is missing Suspense.

**Ask:** What is the leftover picture?

**They do:** copy the leftover board.

**Do not:** start a new project in the exam hour. Do not skip the leftover kernel if 15 minutes remain.



### Show / attempt if time

**Say:** Suspense fallback while a glTF loads, or a fake delay. Plant a missing file and a silent hang. Fix: error + placeholder cube.

**They do:** Fallback cube; error text if missing. Compress later (Blender).

---

## Live coding (remaining time)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Suspense fallback | Plant black canvas. |
| 15–40 | Missing glTF error | Plant silent 404. |
| 40–60 | Placeholder cube | They type. Circulate. |

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

drei useProgress UI kit. Keep fallback + error.

## If we run short, add

Timeout message name.
