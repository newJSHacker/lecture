# Lecture 8 — Midterm and ray marching intro

**Week 8 of 15** · Shader Programming  
**Meeting:** written midterm, then leftover lecture + live coding  
**Kernel (after the exam):** sphere trace: p += d * dir until hit or escape  
**Success check:** after the exam they can step a ray by the SDF distance and color a hit

This meeting is an **exam**, then a short class. It is not a normal content lecture. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Printed midterm + spare paper. No laptop for the exam.
- Topic list was announced at the end of Lecture 7.
- After collection: demo `Shader Programming/code/` ready (local, no CDN).
- Parked strip (uncover after the exam): `Lecture 8 | Goal: leftover kernel | Invariant: a true SDF lets you step by d; smoothmin can break that safety`

## Midterm (about 50–60 min)

Written. No laptop. Weeks 1–7.

**Topics:** varying vs uniform; gamma decode/encode; fract/polar; hash+bilinear; fBm octaves; signed SDF + CSG.

Collect. Do not mark in silence for the rest of the hour — uncover the leftover lecture.

## Board at the end (after the exam; they photograph this)

```
p = cam
for i in 0..maxSteps:
  d = map(p)
  if d < eps:  HIT
  p += d * dir
  if too far:  MISS

smoothmin  may  overstep
```

## Slides today (cap: 2)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## After the exam (~15–25 min lecture)

**Say:** This meeting is a **midterm**, then sphere tracing. No laptop for the exam. After: walk the ray by d. Do not start with eight nested SDFs.

**Ask:** What is the leftover picture?

**They do:** copy the leftover board.

**Do not:** start a new project in the exam hour. Do not skip the leftover kernel if 15 minutes remain.



### Show / attempt if time

**Say:** March a sphere; Lambert on the hit. Plant a constant step size that skips the surface. Miss color as a debug uniform.

**They do:** Miss color + max-steps slider (a uniform you can pause).

---

## Live coding (remaining time)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | p += d * dir | Plant fixed 0.1 steps. |
| 15–40 | Sphere + Lambert | Plant eight nested SDFs. |
| 40–60 | Miss color uniform | They type. Circulate. |

---

## Lab

1. miss color.
2. max steps slider.

---

## Homework

1. Reflection + a screenshot of a hit.

---

## Quiz next meeting

None this week — midterm. Next quiz is Lecture 9.

## Extra exercises

See [[Shader Programming/exercises/Week 08]].

## If we run long, cut

Live coding if the exam ran long. Keep the leftover board.

## If we run short, add

Lipschitz / smoothmin warning in one sentence.
