# Lecture 8 — Midterm and ray marching intro

**Week 8 of 15** · Shader Programming  
**Meeting:** written midterm, then leftover lecture + live coding  
**Kernel (after the exam):** midterm; sphere trace idea  
**Success check:** they sit the exam; after, they can state the leftover kernel in one sentence

This meeting is an **exam**, then a short class. It is not a normal content lecture. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Printed midterm + spare paper. No laptop for the exam.
- Topic list was announced at the end of Lecture 7.
- After collection: demo `Shader Programming/code/` ready (local, no CDN).
- Parked strip (uncover after the exam): `Lecture 8 | Goal: leftover kernel | Invariant: a shader is a program over pixels or vertices`

## Midterm (about 50–60 min)

Written. No laptop. Weeks 1–7.

**Topics:** Sit midterm: gamma, uv, noise, fBm, SDF2D., Sphere tracing: step by d., Escape and hit thresholds., Don't start with 8 nested SDFs.

Collect. Do not mark in silence for the rest of the hour — uncover the leftover lecture.

## Board at the end (after the exam; they photograph this)

```
p += d * dir
Ray with disks.
```

## Slides today (cap: 2)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## After the exam (~15–25 min lecture)

**Say:** The exam is over. The leftover kernel is on the parked strip.

**Ask:** Sphere tracing: step by d.

**They do:** copy the leftover board.

**Do not:** start a new project in the exam hour. Do not skip the leftover kernel if 15 minutes remain.

**2. March.** From the camera, walk along the ray by the SDF distance. Safe if the field is a true SDF (Lipschitz). Blending/smoothmin can break safety — mention.

**3. Demo.** [[WebGL/demos]] raymarch if present; else Shadertoy sphere.

### Show / attempt if time

**Say:** March a sphere; color by Lambert.

---

**They do:** miss color.

---

## Live coding (remaining time)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: midterm; sphere trace idea | Plant the first common mistake. |
| 10–30 | March a sphere; color by Lambert. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

Live coding. Keep the leftover board.

## If we run short, add

One more worked leftover example.
