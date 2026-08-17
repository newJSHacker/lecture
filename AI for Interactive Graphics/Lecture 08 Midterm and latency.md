# Lecture 8 — Midterm and latency

**Week 8 of 15** · AI for Interactive Graphics  
**Meeting:** written midterm, then leftover lecture + live coding  
**Kernel (after the exam):** midterm; streaming, placeholders  
**Success check:** they sit the exam; after, they can state the leftover kernel in one sentence

This meeting is an **exam**, then a short class. It is not a normal content lecture. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Printed midterm + spare paper. No laptop for the exam.
- Topic list was announced at the end of Lecture 7.
- After collection: demo `AI for Interactive Graphics/code/02-asset-table.html` ready (local, no CDN).
- Parked strip (uncover after the exam): `Lecture 8 | Goal: leftover kernel | Invariant: no secrets in the frontend; cite the model`

## Midterm (about 50–60 min)

Written. No laptop. Weeks 1–7.

**Topics:** Sit midterm: ethics, proxy, textures, 3D limits, agents, RAG, logs., Time to first token., Streaming UI., Don't block the render loop on fetch.

Collect. Do not mark in silence for the rest of the hour — uncover the leftover lecture.

## Board at the end (after the exam; they photograph this)

```
TTFT; skeleton UI
Stream + orbit.
```

## Slides today (cap: 2)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## After the exam (~15–25 min lecture)

**Say:** The exam is over. The leftover kernel is on the parked strip.

**Ask:** Time to first token.

**They do:** copy the leftover board.

**Do not:** start a new project in the exam hour. Do not skip the leftover kernel if 15 minutes remain.

**2. UX.** 3D should orbit while text streams. Placeholders on textures.

**3. Cost.** Retries cost money. Cache mocks in dev.

### Show / attempt if time

**Say:** Orbit a cube while a mocked stream fills a HUD.

---

**They do:** abort button.

---

## Live coding (remaining time)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: midterm; streaming, placeholders | Plant the first common mistake. |
| 10–30 | Orbit a cube while a mocked stream fills a HUD. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

Live coding. Keep the leftover board.

## If we run short, add

One more worked leftover example.
