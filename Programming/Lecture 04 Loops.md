# Lecture 4 — Loops

**Week 4 of 15** · Introduction to Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** `for (let i = 0; i < n; i++)` and an 8×8 checkerboard in the console  
**Success check:** they can say how many times `i < 10` from 0 runs (10) and print two nested loops

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `Programming/code/04-checker.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: repeat without copy-paste | Invariant: the loop variable counts 0 .. n−1 unless you have a reason`

## Board at the end (they photograph this)

```
for (let i = 0; i < n; i++) { … }     // n times, i = 0..n-1

fenceposts:  4 posts, 3 rails
nested:      n * n cells

invariant of sum: after k steps, s is the sum of the first k items
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Optional: a photo of a picket fence | only if you will not draw four posts |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** If you can write a loop, you can walk pixels. Computer Graphics I is nested loops over a triangle. Today we walk numbers.

**Ask:** How many times does `for (let i = 0; i < 10; i++)` run? Wait. Want: 10, not 9, not 11.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *`for (let i = 0; i < n; i++)` and an 8×8 checkerboard in the console*.

**Do not:** `i <= a.length` and crash.

### Minutes 10–12 — Frame

**Say:** `for` is the default. `while` is for unknown count. Off-by-one is the professional disease. We draw fenceposts.

**Ask:** Is the last index of an array of length n `n` or `n-1`?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** `i` from 0 inclusive to `n` exclusive. That is vertices, pixels, and students in a list.

**Board:** four posts, three rails. Inclusive vs exclusive end.

**Say:** Nested loops make a grid. A checkerboard is `#.` rows. Infinite loop: `i` never changes, or `while (true)` with no `break`.

**Ask:** If the inner loop runs n times and the outer n times, how many cells? Want: n².

**They do:** On paper: trace `s = 0; for i in 0..3: s += i`. What is s?

**Do not:** Mix Python syntax into a JS term. Skip the attempt.

### Minutes 35–50 — Show

**Say:** I print a triangle of stars, then an 8×8 checkerboard. Zoom 140%. I will plant `i <= a.length` later in live coding and crash.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Sum 1..100 in a loop. Eight minutes. Then we write the invariant: after k steps, s is the sum of 1..k.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: sum and a prime checker n ≤ 200. Homework: FizzBuzz 1..100 and the invariant paragraph. Quiz: how many times `i < 10`, infinite loop, n×n count.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Sum 1..10, narrate the invariant | Plant `i <= 10` extra iteration. Fix `<`. |
| 10–30 | Triangle of stars | Off-by-one on the inner bound. |
| 30–45 | 8×8 checkerboard | Plant `i <= a.length` if using an array. |
| 45–60 | They type sum 1..100 | Circulate. |

Point them at `Programming/code/04-checker.html` as the after-class check, not as the lecture.

---

## Lab

1. Sum 1..100.
2. Prime checker (trial division) for n ≤ 200.

---

## Homework

1. FizzBuzz 1..100.
2. Written: invariant of the sum loop.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
for (let i = 0; i < n; i++) s += a[i];
```

---

## Extra exercises

See [[Programming/exercises/Week 04]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. `i <= a.length` and crash.
2. Modifying i inside in two places.

## If we run long, cut

Prime checker derivation. Keep 0..n−1 and nested loops.

## If we run short, add

`break` / `continue` names. Still no `forEach` as the required kernel.
