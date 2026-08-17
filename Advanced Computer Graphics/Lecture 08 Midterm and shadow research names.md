# Lecture 8 — Midterm and shadow research names

**Week 8 of 15** · Advanced Computer Graphics  
**Meeting:** written midterm, then leftover lecture + live coding  
**Kernel (after the exam):** midterm; VSM, CSM, PCSS  
**Success check:** they sit the exam; after, they can state the leftover kernel in one sentence

This meeting is an **exam**, then a short class. It is not a normal content lecture. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Printed midterm + spare paper. No laptop for the exam.
- Topic list was announced at the end of Lecture 7.
- After collection: demo `Advanced Computer Graphics/code/02-tracer.html` ready (local, no CDN).
- Parked strip (uncover after the exam): `Lecture 8 | Goal: leftover kernel | Invariant: local lighting is bounce 0; GI is the rest`

## Midterm (about 50–60 min)

Written. No laptop. Weeks 1–7.

**Topics:** Sit midterm: GI taxonomy, radiosity, path tracing, volumes, tiled lights., VSM: mean + variance, Chebyshev., CSM: split frustum., PCSS name.

Collect. Do not mark in silence for the rest of the hour — uncover the leftover lecture.

## Board at the end (after the exam; they photograph this)

```
moments; cascades; penumbra
Three columns.
```

## Slides today (cap: 2)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## After the exam (~15–25 min lecture)

**Say:** The exam is over. The leftover kernel is on the parked strip.

**Ask:** VSM: mean + variance, Chebyshev.

**They do:** copy the leftover board.

**Do not:** start a new project in the exam hour. Do not skip the leftover kernel if 15 minutes remain.

**2. Shadows beyond PCF.** VSM light leak. CSM seams. PCSS blocker search.

**3. Pick.** Students write 1 page comparing two, implement none or one extra.

### Show / attempt if time

**Say:** Written compare VSM vs CSM vs PCSS (table). Optional tiny VSM extra.

---

**They do:** draw cascade splits.

---

## Live coding (remaining time)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: midterm; VSM, CSM, PCSS | Plant the first common mistake. |
| 10–30 | Written compare VSM vs CSM vs PCSS (table). Optional tiny VSM extra. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

---

## Lab

1. draw cascade splits.
2. light leak sketch.

---

## Homework

1. Midterm reflection + table.

---

## Quiz next meeting

None this week — midterm. Next quiz is Lecture 9.

## Extra exercises

See [[Advanced Computer Graphics/exercises/Week 08]].

## If we run long, cut

Live coding. Keep the leftover board.

## If we run short, add

One more worked leftover example.
