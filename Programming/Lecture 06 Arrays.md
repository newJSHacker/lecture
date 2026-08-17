# Lecture 6 — Arrays

**Week 6 of 15** · Introduction to Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** `const b = a.slice()` and average / max-index of an array  
**Success check:** they can say whether two names point at the same array (alias) or a copy

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `Programming/code/06-arrays.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: store many values | Invariant: index 0 is the first; `length-1` is the last; `push` mutates even on `const``

## Board at the end (they photograph this)

```
[  10 |  20 |  30 ]     indices 0, 1, 2
         ↑
       a[1]

const a = [];  a.push(1);   // legal: const blocks rebind, not mutation
const b = a;     // alias
const c = a.slice();  // copy
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** Vertices will be arrays of points. An off-by-one here is a missing triangle in Computer Graphics I. Today: index, push, copy.

**Ask:** What is the index of the last element of `a`? Wait. Want: `a.length - 1`.

**Board:** parked strip. Then boxes 0..n-1.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *push, map, index*.

**Do not:** `a = a.push(x)`.

### Minutes 10–12 — Frame

**Say:** `map`/`filter` are names only this week. Required kernel is a `for` loop. `const a = []` can still `push`.

**Ask:** Does `const a = []` mean the array cannot grow?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Boxes 0..n−1. Holes (`a[9]` when length 3) are forbidden in this course.

**Board:** alias vs copy. Two arrows to one row vs two rows.

**Say:** `a = a.push(x)` is a bug: `push` returns the new length. Copy with `slice` before you sort if you need the original.

**Ask:** After `const b = a; b.push(1)`, what is `a.length`?

**They do:** On paper: reverse a 4-element array on a copy.

**Do not:** mix Python syntax into a JS term. Do not skip the attempt.

### Minutes 35–50 — Show

**Say:** Average of an array; then index of the max. I will plant `a = a.push(x)` and read the number that appears.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Reverse a **copy**. Do not mutate the original. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: reverse copy; remove duplicates with nested loop (n small). Homework: letter histogram; index vs value. Quiz: last index, push return, copy vs alias.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Build an array with push | Plant `a = a.push`. |
| 10–30 | Average and max index | Off-by-one on the loop. |
| 30–45 | `slice` vs alias | Mutate both; show the shared row. |
| 45–60 | They reverse a copy | Circulate. |

Point them at `Programming/code/06-arrays.html` as the after-class check, not as the lecture.

---

## Lab

1. Reverse a copy.
2. Remove duplicates with a nested loop (n small).

---

## Homework

1. Histogram of letters.
2. Written: index vs value.

---

## Quiz next meeting (they hear this now)

1. Index of last element (2)
2. push return value (2)
3. Copy vs alias (6)


## Snippet

```js
const b = a.slice();
```

---

## Extra exercises

See [[Programming/exercises/Week 06]].

---

## Notes you may still need (from the outline)

**1. A list of values.** Vertices will be arrays of points. Indices into a cube. Off-by-one here becomes a missing triangle later.

**2. Mutation.** push changes the array. `const a = []` can still push. Copy before sort if you need the original.

**3. Higher-order preview.** `arr.map` / `filter` names only. Required: for-loop. Optional: map for the homework extra.

---

## Common mistakes

1. `a = a.push(x)`.
2. Using map without understanding for.

## If we run long, cut

`map` as required. Keep for-loop + slice.

## If we run short, add

`for...of` vs index when you need the i.
