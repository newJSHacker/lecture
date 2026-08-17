# Lecture 8 — Midterm and WebGPU intro

**Week 8 of 15** · GPU Programming  
**Meeting:** written midterm, then leftover lecture + live coding  
**Kernel (after the exam):** midterm; device/queue  
**Success check:** they sit the exam; after, they can state the leftover kernel in one sentence

This meeting is an **exam**, then a short class. It is not a normal content lecture. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Printed midterm + spare paper. No laptop for the exam.
- Topic list was announced at the end of Lecture 7.
- After collection: demo `GPU Programming/code/01-pong.html` ready (local, no CDN).
- Parked strip (uncover after the exam): `Lecture 8 | Goal: leftover kernel | Invariant: data lives where the kernel runs`

## Midterm (about 50–60 min)

Written. No laptop. Weeks 1–7.

**Topics:** Sit midterm: ping-pong, particles, Euler, fluids names, reduce., Request adapter/device., Why WGSL., Don't port the whole particle system this week.

Collect. Do not mark in silence for the rest of the hour — uncover the leftover lecture.

## Board at the end (after the exam; they photograph this)

```
adapter → device → queue
Adapter box.
```

## Slides today (cap: 2)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## After the exam (~15–25 min lecture)

**Say:** The exam is over. The leftover kernel is on the parked strip.

**Ask:** Request adapter/device.

**They do:** copy the leftover board.

**Do not:** start a new project in the exam hour. Do not skip the leftover kernel if 15 minutes remain.

**2. WebGPU.** Modern API. Explicit pipelines, bind groups, compute. Chrome. Not a Safari-only lab without a fallback plan.

**3. Mental map.** WebGL program ≈ pipeline. Uniforms ≈ bind group. FBO ≈ texture views.

### Show / attempt if time

**Say:** Hello triangle in WebGPU **or** a documented fallback WebGL triangle plus a WGSL reading.

---

**They do:** feature detect.

---

## Live coding (remaining time)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: midterm; device/queue | Plant the first common mistake. |
| 10–30 | Hello triangle in WebGPU **or** a documented fallback WebGL triangle plus a WGSL reading. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

---

## Lab

1. feature detect.
2. error popup.

---

## Homework

1. Reflection + adapter name screenshot.

---

## Quiz next meeting

None this week — midterm. Next quiz is Lecture 9.

## Extra exercises

See [[GPU Programming/exercises/Week 08]].

## If we run long, cut

Live coding. Keep the leftover board.

## If we run short, add

One more worked leftover example.
