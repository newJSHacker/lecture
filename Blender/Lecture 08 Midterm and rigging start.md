# Lecture 8 — Midterm and rigging start

**Week 8 of 15** · Blender for Real-Time Graphics  
**Meeting:** written midterm, then leftover lecture + live coding  
**Kernel (after the exam):** midterm; then armature idea: a bone is a transform, weights skin the mesh  
**Success check:** after the exam they can add an armature, parent with automatic weights on a bar, and name rest pose

This meeting is an **exam**, then a short class. It is not a normal content lecture. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Printed midterm + spare paper. No laptop for the exam.
- Topic list was announced at the end of Lecture 7.
- After collection: demo `Blender/code/03-budget.html` ready (local, no CDN).
- Parked strip (uncover after the exam): `Lecture 8 | Goal: leftover kernel | Invariant: real-time keeps bone count modest; automatic weights leak — that is the leftover lab`

## Midterm (about 50–60 min)

Written. No laptop. Weeks 1–7.

**Topics:** meters/apply-scale name; topology and face orientation; modifier order; seams/checker; Principled metal 0|1; sun→directional; I-key and F-curves (not runtime fps).

Collect. Do not mark in silence for the rest of the hour — uncover the leftover lecture.

## Board at the end (after the exam; they photograph this)

```
armature  =  bones (transforms)
skin      =  weights per vertex
parent with automatic weights   (on a bar / simple arm)

Pose mode ≠ Edit bones
rest pose  =  what you export as bind
```

## Slides today (cap: 2)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## After the exam (~15–25 min lecture)

**Say:** This meeting is a **midterm**, then rigging start. No laptop for the exam. After: a bone is a transform. Weight paint names only. Modest bone count.

**Ask:** What is the leftover picture?

**They do:** copy the leftover board.

**Do not:** start a new project in the exam hour. Do not skip the leftover kernel if 15 minutes remain.



### Show / attempt if time

**Say:** Add armature; parent automatic weights on a simple mesh. Plant posing in object mode. Plant 40 bones on a crate.

**They do:** Pose the bar. Rest pose named.

---

## Live coding (remaining time)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Add armature + bone | Plant 40 bones. |
| 15–40 | Automatic weights on a bar | Leak into the other bone. |
| 40–60 | Pose vs rest | They type. Circulate. |

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

IK chains. Keep one bone + weights name.

## If we run short, add

Fix a weight leaking into the other bone extra.
