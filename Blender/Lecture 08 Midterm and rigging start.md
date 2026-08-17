# Lecture 8 — Midterm and rigging start

**Week 8 of 15** · Blender for Real-Time Graphics  
**Meeting:** written midterm, then leftover lecture + live coding  
**Kernel (after the exam):** midterm; armature idea  
**Success check:** they sit the exam; after, they can state the leftover kernel in one sentence

This meeting is an **exam**, then a short class. It is not a normal content lecture. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Printed midterm + spare paper. No laptop for the exam.
- Topic list was announced at the end of Lecture 7.
- After collection: demo `Blender/code/03-budget.html` ready (local, no CDN).
- Parked strip (uncover after the exam): `Lecture 8 | Goal: leftover kernel | Invariant: units, facing, and budget travel with the asset`

## Midterm (about 50–60 min)

Written. No laptop. Weeks 1–7.

**Topics:** Sit midterm: units, topo, UV, Principled, lights, keys., Add an armature., Parent with automatic weights on a simple mesh., Pose mode.

Collect. Do not mark in silence for the rest of the hour — uncover the leftover lecture.

## Board at the end (after the exam; they photograph this)

```
bone parent of mesh
Bone chain.
Weight colors.
```

## Slides today (cap: 2)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## After the exam (~15–25 min lecture)

**Say:** The exam is over. The leftover kernel is on the parked strip.

**Ask:** Add an armature.

**They do:** copy the leftover board.

**Do not:** start a new project in the exam hour. Do not skip the leftover kernel if 15 minutes remain.

**2. Bones.** A bone is a transform. Skinning is weights. Real-time: keep bone count modest.

**3. Weights.** Automatic weights on a bar or a simple arm. Weight paint names only.

### Show / attempt if time

**Say:** Two-bone arm; pose it; screenshot.

---

**They do:** Fix a weight leaking into the other bone extra.

---

## Live coding (remaining time)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: midterm; armature idea | Plant the first common mistake. |
| 10–30 | Two-bone arm; pose it; screenshot. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

---

## Lab

1. Fix a weight leaking into the other bone extra.
2. Rest pose.

---

## Homework

1. Midterm reflection + armature file.

---

## Quiz next meeting

None this week — midterm. Next quiz is Lecture 9.

## Extra exercises

See [[Blender/exercises/Week 08]].

## If we run long, cut

Live coding. Keep the leftover board.

## If we run short, add

One more worked leftover example.
