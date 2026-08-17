# Lecture 8 — Midterm and types preview

**Week 8 of 15** · Modern JavaScript Development  
**Meeting:** written midterm, then leftover lecture + live coding  
**Kernel (after the exam):** JSDoc (or optional TS) on lerp/clamp; Point as {x,y} with a type name  
**Success check:** after the exam they can annotate lerp in JSDoc and say why any is a smell

This meeting is an **exam**, then a short class. It is not a normal content lecture. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Printed midterm + spare paper. No laptop for the exam.
- Topic list was announced at the end of Lecture 7.
- After collection: demo `Modern JavaScript/code/08-modules.html` ready (local, no CDN).
- Parked strip (uncover after the exam): `Lecture 8 | Goal: leftover kernel | Invariant: types are comments the machine can check; any is opting out`

## Midterm (about 50–60 min)

Written. No laptop. Weeks 1–7.

**Topics:** let/const vs var; arrows not constructors; shallow spread; named export + why serve; Promise states + catch; await vs Promise.all; fetch res.ok + abort + no keys; npm scripts, lockfile, no node_modules in git.

Collect. Do not mark in silence for the rest of the hour — uncover the leftover lecture.

## Board at the end (after the exam; they photograph this)

```
/** @param {number} a @param {number} b @param {number} t */
export function lerp(a, b, t) { return a + (b - a) * t; }

// optional TS leftover
type Point = { x: number; y: number };

any  =  smell
```

## Slides today (cap: 2)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Optional: JSDoc tooltip on lerp in the editor | photograph — do not draw the IDE |

---

## After the exam (~15–25 min lecture)

**Say:** This meeting is a **midterm**, then types as a preview. No laptop for the exam. After: JSDoc on the kernel. TypeScript is optional homework, not a second course.

**Ask:** What does any mean? Wait. Want: skip the checker.

**They do:** copy the leftover board.

**Do not:** start a new project in the exam hour. Do not skip the leftover kernel if 15 minutes remain.



### Show / attempt if time

**Say:** Add JSDoc to lerp; or a .ts Point if the lab has vite+ts. Demo Modern JavaScript/code/08-modules.html as the module reminder. Plant any on lerp. Remove it.

**They do:** Typed clamp — JSDoc or .ts. Midterm reflection if time is gone.

---

## Live coding (remaining time)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | JSDoc on lerp | Plant any. Fix number. |
| 15–40 | Point type name | They copy. No new bundler. |
| 40–60 | They JSDoc clamp | Circulate. |

---

## Lab

1. Typed clamp.
2. Midterm reflection.

---

## Homework

1. Optional TS Point tests.

---

## Quiz next meeting

None this week — midterm. Next quiz is Lecture 9.

## Extra exercises

See [[Modern JavaScript/exercises/Week 08]].

## If we run long, cut

Live coding if the exam ran long. Keep the JSDoc board.

## If we run short, add

One more leftover: clamp JSDoc with a failing call they can see.
