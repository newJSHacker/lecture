# Lecture 8 — Midterm and SSAO idea

**Week 8 of 15** · Real-Time Rendering  
**Meeting:** written midterm, then leftover lecture + live coding  
**Kernel (after the exam):** SSAO as a post pass: sample neighbors in view-space depth  
**Success check:** after the exam they can name AO as a fake post and toggle it

This meeting is an **exam**, then a short class. It is not a normal content lecture. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Printed midterm + spare paper. No laptop for the exam.
- Topic list was announced at the end of Lecture 7.
- After collection: demo `Real-Time Rendering/code/` ready (local, no CDN).
- Parked strip (uncover after the exam): `Lecture 8 | Goal: leftover kernel | Invariant: SSAO is not a true GI pass; it is a named post on depth`

## Midterm (about 50–60 min)

Written. No laptop. Weeks 1–7.

**Topics:** forward path; D F G and F0; IBL names; HDR/tonemap order; bloom's three passes; shadow map + PCF.

Collect. Do not mark in silence for the rest of the hour — uncover the leftover lecture.

## Board at the end (after the exam; they photograph this)

```
PASS: SSAO post
  sample hemisphere in view space
  darken if depth neighbors occlude

fake · noisy · dark rims · skip sky
HBAO  name only
```

## Slides today (cap: 2)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## After the exam (~15–25 min lecture)

**Say:** This meeting is a **midterm**, then SSAO as a post. No laptop. After: sample neighbors in depth. Do not require production HBAO.

**Ask:** What is the leftover picture?

**They do:** copy the leftover board.

**Do not:** start a new project in the exam hour. Do not skip the leftover kernel if 15 minutes remain.



### Show / attempt if time

**Say:** Two planes in a corner; cheap SSAO or a Three.js SAO pass explained after the boxes. Plant SSAO as GI. Radius slider. No invented fps.

**They do:** Toggle + radius uniform.

---

## Live coding (remaining time)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Name the AO post | Plant SSAO as GI. |
| 15–40 | Hemisphere samples | Plant missing sky skip. |
| 40–60 | Toggle + radius | They type. Circulate. |

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

Live coding if the exam ran long. Keep the leftover board.

## If we run short, add

Noise / dark-rim artifacts named.
