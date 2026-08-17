# Lecture 8 — Midterm and compositor

**Week 8 of 15** · Interactive Web Development  
**Meeting:** written midterm, then leftover lecture + live coding  
**Kernel (after the exam):** compositor layers as a name; transform/opacity vs left/top; will-change sparingly  
**Success check:** after the exam they can say why a left animation is the wrong leftover demo and remove a sprayed will-change

This meeting is an **exam**, then a short class. It is not a normal content lecture. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Printed midterm + spare paper. No laptop for the exam.
- Topic list was announced at the end of Lecture 7.
- After collection: demo `Interactive Web/code/08-cull.html` ready (local, no CDN).
- Parked strip (uncover after the exam): `Lecture 8 | Goal: leftover kernel | Invariant: layers are a memory bet; will-change is not a speed cheat code; do not invent fps`

## Midterm (about 50–60 min)

Written. No laptop. Weeks 1–7.

**Topics:** getContext 2d, paths, save/restore; rAF, dt, clear, cap; pointer mapping via bounding rect; SVG viewBox vs Canvas; transitions on transform + reduced motion; @keyframes vs physics; local GSAP timeline, no CDN.

Collect. Do not mark in silence for the rest of the hour — uncover the leftover lecture.

## Board at the end (after the exam; they photograph this)

```
layout  →  paint  →  composite

transform / opacity     (composite)
left / top / width      (layout)

will-change: transform;    /* hint; costs memory; remove after */
paint flashing            /* DevTools name — photograph if used */
```

## Slides today (cap: 2)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Optional: paint-flashing screenshot, left vs transform | photo; no fps overlay you invented |

---

## After the exam (~15–25 min lecture)

**Say:** This meeting is a **midterm**, then the compositor leftover from Web Technologies week 12, now with motion. No laptop for the exam. After: layers as a name. We do not invent fps.

**Ask:** Does will-change: transform on every node help? Wait. Want: no — memory, extra layers.

**They do:** copy the leftover board.

**Do not:** start a new project in the exam hour. Do not skip the leftover kernel if 15 minutes remain.



### Show / attempt if time

**Say:** Paint flashing on a janky left animation vs transform. Do not quote fps. Plant will-change on everything. Remove it.

**They do:** Remove a will-change after. Midterm reflection if time is gone.

---

## Live coding (remaining time)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | left vs transform | Plant left. No invented fps. |
| 15–40 | will-change spray | Remove after. |
| 40–60 | They write the three-stage names | Circulate. |

---

## Lab

1. Remove a will-change after.
2. Midterm reflection.

---

## Homework

1. Written: layers.
2. None.

---

## Quiz next meeting

None this week — midterm. Next quiz is Lecture 9.

## Extra exercises

See [[Interactive Web/exercises/Week 08]].

## If we run long, cut

Live coding if the exam ran long. Keep the leftover board.

## If we run short, add

One more leftover: photograph paint flashing if DevTools is already open.
