# Lecture 8 — Midterm and debugging

**Week 8 of 15** · Introduction to Programming  
**Meeting:** written midterm, then leftover lecture + live coding  
**Kernel (after the exam):** read a stack trace; `console.assert`; one breakpoint  
**Success check:** after the exam, they can point at the first stack line of a planted bug

This meeting is an **exam**, then a short class. It is not a normal content lecture. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Printed midterm + spare paper. No laptop for the exam.
- Topic list was announced at the end of Lecture 7.
- After collection: demo `Programming/code/05-clamp.html` ready (local, no CDN).
- Parked strip (uncover after the exam): `Lecture 8 | Goal: leftover kernel | Invariant: syntax vs runtime vs wrong answer are three different diseases`

## Midterm (about 50–60 min)

Written. No laptop. Weeks 1–7.

**Topics:** values and `'3'+1`; `let`/`const`; `===`; loops 0..n−1; functions that return; arrays (copy vs alias); objects `{x,y}`.

Collect. Do not mark in silence for the rest of the hour — uncover the leftover lecture.

## Board at the end (after the exam; they photograph this)

```
syntax     red squiggle / failed to parse
runtime    throws: TypeError, ReferenceError
wrong      runs, lies

read the FIRST line of the stack
console.assert(clamp(5,0,3)===3, 'clamp high')
```

## Slides today (cap: 2)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | A real TypeError stack, first line circled | do not draw Chrome’s UI |

---

## After the exam (~15–25 min lecture)

**Say:** This meeting is a **midterm**, then a short lecture on debugging. No laptop for the exam.

**Ask:** Read a stack trace.

**They do:** copy the leftover board.

**Do not:** start a new project in the exam hour. Do not skip the leftover kernel if 15 minutes remain.

**2. Debugging.** Syntax error vs runtime vs wrong answer. Breakpoints in DevTools. Do not `console.log` fifty times as the only strategy — but it is allowed.

**3. assert.** `console.assert(lerp(0,10,0.5)===5)` is the seed of Week 19 kernel tests in later courses.

### Show / attempt if time

**Say:** After collection: a broken `average` that divides by `length-1`. Breakpoint on the return. `console.assert`.

**They do:** They fix one planted bug in a starter after the exam (if time). Otherwise this is the lab.

---

## Live coding (remaining time)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Broken average + breakpoint | They watch you; then they try. |
| 15–40 | Three error kinds on the board | Plant a silent wrong answer (no throw). |
| 40–60 | They write asserts for centroid | Circulate. |

---

## Lab

1. Fix three planted bugs in a starter.
2. Write 5 asserts for last week's centroid.

---

## Homework

1. Reflection: one midterm item you missed, rewrite the solution.

---

## Quiz next meeting

None this week — midterm. Next quiz is Lecture 9.

## Extra exercises

See [[Programming/exercises/Week 08]].

## If we run long, cut

Live coding if the exam ran long. Keep the error-kinds board.

## If we run short, add

Binary-search a bug: comment out half.
