# Lecture 8 — Midterm and latency

**Week 8 of 15** · AI for Interactive Graphics  
**Meeting:** written midterm, then leftover lecture + live coding  
**Kernel (after the exam):** midterm; then latency: stream or placeholder; 3D keeps orbiting; abort  
**Success check:** after the exam they can orbit a cube while a mocked stream fills a HUD

This meeting is an **exam**, then a short class. It is not a normal content lecture. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Printed midterm + spare paper. No laptop for the exam.
- Topic list was announced at the end of Lecture 7.
- After collection: demo `AI for Interactive Graphics/code/02-asset-table.html` ready (local, no CDN).
- Parked strip (uncover after the exam): `Lecture 8 | Goal: leftover kernel | Invariant: no secrets in the frontend; cite the model`

## Midterm (about 50–60 min)

Written. No laptop. Weeks 1–7.

**Topics:** not training GPT; no frontend secrets; proxy/mock; image→map + asset table; 3D-gen inspect; allowlisted tools; RAG retrieve-then-cite.

Collect. Do not mark in silence for the rest of the hour — uncover the leftover lecture.

## Board at the end (after the exam; they photograph this)

```
time to first token     (name; measure later)
3D orbits while text streams
placeholder on textures
abort · timeout
retries cost $     cache mocks in dev
```

## Slides today (cap: 2)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## After the exam (~15–25 min lecture)

**Say:** This meeting is a **midterm**, then latency UX. No laptop for the exam. After: a frozen canvas waiting on a vendor is a fail. Placeholders. Abort. Do not invent milliseconds.

**Ask:** What is the leftover picture?

**They do:** copy the leftover board.

**Do not:** start a new project in the exam hour. Do not skip the leftover kernel if 15 minutes remain.



### Show / attempt if time

**Say:** Orbit a cube while a mocked stream fills a HUD. Plant blocking fetch that freezes the canvas. Abort button.

**They do:** Placeholder + abort. Two clocks: rAF vs await.

---

## Live coding (remaining time)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Orbit during mock stream | Plant frozen canvas. |
| 15–40 | Placeholder texture | Plant blocking await. |
| 40–60 | Abort + timeout | They type. Circulate. |

---

## Lab

1. abort button.
2. timeout UI.

---

## Homework

1. Reflection + latency notes.

---

## Quiz next meeting

None this week — midterm. Next quiz is Lecture 9.

## Extra exercises

See [[AI for Interactive Graphics/exercises/Week 08]].

## If we run long, cut

Vendor streaming protocol. Keep placeholder + abort.

## If we run short, add

Timeout UI.
