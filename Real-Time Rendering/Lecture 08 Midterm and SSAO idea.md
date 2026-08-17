# Lecture 8 — Midterm and SSAO idea

**Week 8 of 15** · Real-Time Rendering  
**Meeting:** written midterm, then leftover lecture + live coding  
**Kernel (after the exam):** midterm; AO as post  
**Success check:** they sit the exam; after, they can state the leftover kernel in one sentence

This meeting is an **exam**, then a short class. It is not a normal content lecture. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Printed midterm + spare paper. No laptop for the exam.
- Topic list was announced at the end of Lecture 7.
- After collection: demo `Real-Time Rendering/code/` ready (local, no CDN).
- Parked strip (uncover after the exam): `Lecture 8 | Goal: leftover kernel | Invariant: a frame is a budget; name the pass`

## Midterm (about 50–60 min)

Written. No laptop. Weeks 1–7.

**Topics:** Sit midterm: PBR knobs, HDR, bloom, shadow map, PCF., SSAO: sample neighbors in depth., It's a fake., Don't require a production HBAO.

Collect. Do not mark in silence for the rest of the hour — uncover the leftover lecture.

## Board at the end (after the exam; they photograph this)

```
sample hemisphere in view space
Hemisphere samples.
```

## Slides today (cap: 2)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## After the exam (~15–25 min lecture)

**Say:** The exam is over. The leftover kernel is on the parked strip.

**Ask:** SSAO: sample neighbors in depth.

**They do:** copy the leftover board.

**Do not:** start a new project in the exam hour. Do not skip the leftover kernel if 15 minutes remain.

**2. SSAO.** Darken where depth neighbors are occluders. View-space. Horizon-based names only.

**3. Artifacts.** Dark rims, noise, missing on sky.

### Show / attempt if time

**Say:** A corner of two planes with a cheap SSAO or a Three.js SAO pass **explained**.

---

**They do:** toggle.

---

## Live coding (remaining time)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: midterm; AO as post | Plant the first common mistake. |
| 10–30 | A corner of two planes with a cheap SSAO or a Three.js SAO pass **explained**. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

---

## Lab

1. toggle.
2. radius slider.

---

## Homework

1. Reflection + AO screenshot.

---

## Quiz next meeting

None this week — midterm. Next quiz is Lecture 9.

## Extra exercises

See [[Real-Time Rendering/exercises/Week 08]].

## If we run long, cut

Live coding. Keep the leftover board.

## If we run short, add

One more worked leftover example.
