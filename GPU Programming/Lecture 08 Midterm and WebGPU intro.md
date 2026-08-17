# Lecture 8 — Midterm and WebGPU intro

**Week 8 of 15** · GPU Programming  
**Meeting:** written midterm, then leftover lecture + live coding  
**Kernel (after the exam):** WebGPU: adapter → device → queue; feature detect; WGSL later  
**Success check:** after the exam they can request adapter/device or show a documented WebGL fallback

This meeting is an **exam**, then a short class. It is not a normal content lecture. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Printed midterm + spare paper. No laptop for the exam.
- Topic list was announced at the end of Lecture 7.
- After collection: demo `GPU Programming/code/01-pong.html` ready (local, no CDN).
- Parked strip (uncover after the exam): `Lecture 8 | Goal: leftover kernel | Invariant: WebGPU is after ping-pong; no Safari-only lab without a fallback; no CUDA`

## Midterm (about 50–60 min)

Written. No laptop. Weeks 1–7.

**Topics:** throughput vs latency; ping-pong A/B; RG/BA packing; TF name; Euler+clamp; fluids names; mip reduce.

Collect. Do not mark in silence for the rest of the hour — uncover the leftover lecture.

## Board at the end (after the exam; they photograph this)

```
navigator.gpu.requestAdapter()
  → device
  → queue.submit(...)

WebGL program  ≈  pipeline
uniform        ≈  bind group
FBO            ≈  texture view

feature detect  or  WebGL triangle + WGSL reading
```

## Slides today (cap: 2)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## After the exam (~15–25 min lecture)

**Say:** This meeting is a **midterm**, then WebGPU intro. No laptop. After: adapter/device/queue. Do not port the whole particle system this week. Chrome. Not a Safari-only lab without a fallback.

**Ask:** What is the leftover picture?

**They do:** copy the leftover board.

**Do not:** start a new project in the exam hour. Do not skip the leftover kernel if 15 minutes remain.



### Show / attempt if time

**Say:** Hello triangle in WebGPU **or** documented fallback WebGL triangle plus a WGSL reading. Plant no feature detect. Plant CUDA as the leftover.

**They do:** Feature detect + error popup.

---

## Live coding (remaining time)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | adapter → device → queue | Plant skip detect. |
| 15–40 | Hello triangle or fallback | Plant CUDA leftover. |
| 40–60 | Error popup | They type. Circulate. |

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

Live coding if the exam ran long. Keep the leftover board.

## If we run short, add

Mental map WebGL ≈ pipeline on the board.
