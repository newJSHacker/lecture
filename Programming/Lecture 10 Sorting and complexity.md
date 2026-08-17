# Lecture 10 — Sorting and complexity

**Week 10 of 15** · Introduction to Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** selection sort by hand and in code; count swaps; measure n=1000 vs 2000  
**Success check:** they can run selection sort on 6 numbers on paper and not call `array.sort` in the lab

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `Programming/code/09-sort.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: put an array in order and say why it costs | Invariant: nested loops over n are Θ(n²) teaching-level; doubling n roughly quadruples that work`

## Board at the end (they photograph this)

```
selection: for i: find min in i..n-1; swap into i

n cards → n² comparisons (teaching picture)

built-in:  array.sort((a,b)=>a-b)   // exists; not the lab
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Optional: stopwatch photo of two n’s on **this** machine | never invent a millisecond |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** Sorting is so you can binary search. We implement selection sort so you **feel** n². Built-in sort exists; it is not today’s lab.

**Ask:** If n doubles, what happens to nested-loop work? Wait. Want: about four times, not two.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *selection sort by hand and in code; count swaps; measure n=1000 vs 2000*.

**Do not:** Calling sort in the lab.

### Minutes 10–12 — Frame

**Say:** Find min, swap to front. Easy to see. No Master theorem. No invented timings — if we time, we time on this machine.

**Ask:** May you call `.sort` in the lab? Want: no.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Trace 6 numbers on the board. Circle the min each pass.

**Board:** n vs n² sketch. Label “teaching picture, not a proof.”

**Say:** `array.sort((a,b)=>a-b)` — remember the comparator or you get lexicographic strings. Project may use built-in; lab may not.

**Ask:** How many times does the inner loop run, roughly? Want: about n²/2.

**They do:** On paper: one pass of selection sort on `[4,1,3,2]`.

**Do not:** Mix Python syntax into a JS term. Skip the attempt.

### Minutes 35–50 — Show

**Say:** Sort 12 numbers on the board then in code. Count swaps. I will not quote an fps or a millisecond I did not measure.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Implement selection sort on a 6-element array. Tests: already sorted, reversed, duplicates.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: selection sort + tests; **measure** n=1000 vs 2000 (write the numbers you saw). Homework: why n²; insertion sort optional. Quiz: idea, doubling, built-in in project?

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Trace 6 numbers | They copy the board. |
| 15–40 | Implement | Plant `.sort` as a “shortcut” then delete it. |
| 40–55 | Time n=1000 vs 2000 if the machine allows | Write the real numbers. If noisy, say so. |
| 55–60 | They add a duplicate test | Circulate. |

Point them at `Programming/code/09-sort.html` as the after-class check, not as the lecture.

---

## Lab

1. Selection sort + tests.
2. Time n=1000 vs n=2000 (measured, not invented).

---

## Homework

1. Written: why n².
2. Insertion sort extra optional.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
for (let i=0;i<n;i++){ let m=i; for(let j=i+1;j<n;j++) if(a[j]<a[m]) m=j; swap(a,i,m); }
```

---

## Extra exercises

See [[Programming/exercises/Week 10]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Calling sort in the lab.
2. Invented timings.

## If we run long, cut

Insertion sort. Keep selection + doubling.

## If we run short, add

Stable vs unstable: name only.
