# Lecture 8 — Midterm and shadow research names

**Week 8 of 15** · Advanced Computer Graphics  
**Meeting:** written midterm, then leftover lecture + live coding  
**Kernel (after the exam):** midterm; then VSM / CSM / PCSS as names: leak, seams, blocker search  
**Success check:** after the exam they can fill a compare table and sketch cascade splits

This meeting is an **exam**, then a short class. It is not a normal content lecture. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Printed midterm + spare paper. No laptop for the exam.
- Topic list was announced at the end of Lecture 7.
- After collection: demo `Advanced Computer Graphics/code/02-tracer.html` ready (local, no CDN).
- Parked strip (uncover after the exam): `Lecture 8 | Goal: leftover kernel | Invariant: local lighting is bounce 0; GI is the rest`

## Midterm (about 50–60 min)

Written. No laptop. Weeks 1–7.

**Topics:** direct vs indirect; IBL ≠ GI; radiosity gather; MC spp + cosine; mirror/glass depth; Beer–Lambert; tiled lights.

Collect. Do not mark in silence for the rest of the hour — uncover the leftover lecture.

## Board at the end (after the exam; they photograph this)

```
VSM   mean+variance, Chebyshev     light leak
CSM   splits in view depth         seams
PCSS  blocker search               contact-ish

write 1 page comparing two
implement none or one extra
```

## Slides today (cap: 2)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## After the exam (~15–25 min lecture)

**Say:** This meeting is a **midterm**, then shadow names beyond PCF. No laptop for the exam. After: we name VSM leak, CSM seams, PCSS blockers. We do not ship a production shadow stack.

**Ask:** What is the leftover picture?

**They do:** copy the leftover board.

**Do not:** start a new project in the exam hour. Do not skip the leftover kernel if 15 minutes remain.



### Show / attempt if time

**Say:** Written compare table. Optional tiny VSM extra. Draw cascade splits. Light-leak sketch.

**They do:** Fill VSM vs CSM vs PCSS (one row each).

---

## Live coding (remaining time)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Three names | Plant implement-all. |
| 15–40 | Table: leak / seams / blockers | They write. |
| 40–60 | Cascade sketch | Circulate. |

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

Implement all three. Keep names + table.

## If we run short, add

Light-leak sketch.
