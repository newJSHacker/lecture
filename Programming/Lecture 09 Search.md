# Lecture 9 — Search

**Week 9 of 15** · Introduction to Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** linear search and binary search on the same sorted array; log comparison counts  
**Success check:** they state the sorted precondition of binary search and have a test that fails on unsorted input

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `Programming/code/08-search.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: find a value without scanning everything — when you may | Invariant: binary search is allowed only on sorted data; mid is an integer index`

## Board at the end (they photograph this)

```
linear:  scan 0..n-1          Θ(n)
binary:  sorted!  mid probe    Θ(log n)

while (lo <= hi) {
  const mid = (lo + hi) >> 1;   // integer, not /2 float
  …
}
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** Picking, BVH, kd-trees are search. Binary search is the warmup. Today we count comparisons — we do not invent timings.

**Ask:** If the array is not sorted, may I binary search? Wait. Want: no.

**Board:** parked strip. Then sorted row of numbers, mid probe.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *linear vs binary*.

**Do not:** Binary on unsorted data.

### Minutes 10–12 — Frame

**Say:** Linear is always correct and slow. Binary is fast and **wrong** if unsorted. Off-by-one in `hi` is the classic bug.

**Ask:** What is the mid index of length 8, lo=0, hi=7?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Linear: walk until found or end. Return index or −1.

**Board:** sorted row of numbers; circle the mid probe; shrink left or right.

**Say:** Teaching-level Θ(n) vs Θ(log n). Doubling n adds one comparison in binary, not a doubling. `mid = (lo+hi)/2` can be a float — we use `>> 1` or `Math.floor`.

**Ask:** Worst-case comparisons for linear on n=100? Want: 100.

**They do:** On paper: binary-search trace for 7 in `[1,3,4,7,9]`. Write lo, hi, mid each step.

**Do not:** mix Python syntax into a JS term. Do not skip the attempt.

### Minutes 35–50 — Show

**Say:** Both searches on the same array. Log comparison counts. Then I feed unsorted data to binary and it lies.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Tests: found, missing, empty, one element. Plant unsorted and show binary fail. Eight minutes for the test list even if code is incomplete.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: those tests. Homework: one page why sorted is required; optional recursive binary. Quiz: precondition, linear worst case, mid formula.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Linear search | Return −1 policy. |
| 10–35 | Binary search | Plant `hi = mid` infinite loop. Fix `mid-1` / `mid+1`. |
| 35–50 | Unsorted trap | Show a wrong index. |
| 50–60 | They add empty-array test | Circulate. |

Point them at `Programming/code/08-search.html` as the after-class check, not as the lecture.

---

## Lab

1. Binary search tests: found, missing, empty, one element.
2. Plant an unsorted array and show binary fail.

---

## Homework

1. Written: 1 page why sorted is required.
2. Code: recursive binary extra.

---

## Quiz next meeting (they hear this now)

1. Precondition of binary search (3)
2. Comparisons worst case linear (3)
3. Mid formula (4)


## Snippet

```js
while (lo <= hi) { const mid = (lo + hi) >> 1; /* ... */ }
```

---

## Extra exercises

See [[Programming/exercises/Week 09]].

---

## Notes you may still need (from the outline)

**1. Linear search.** Scan until found. Always correct. Slow for large n.

**2. Binary search.** Needs sorted input. Mid index, shrink left or right. Off-by-one in `hi` is the classic bug.

**3. Why graphics people care.** Picking, BVH, and kd-trees (computational geometry) are search. Binary search is the warmup.

---

## Common mistakes

1. Binary on unsorted data.
2. `mid = (lo+hi)/2` floats.

## If we run long, cut

Recursive binary. Keep iterative + precondition.

## If we run short, add

Count comparisons in a table for n=16.
