# Lecture 11 — Recursion

**Week 11 of 15** · Introduction to Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** `fact(n)` with base case first; stack of `fact(4)`  
**Success check:** they can draw four stack frames and name the base case

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `Programming/code/10-fact.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: a function that calls itself on purpose | Invariant: write the base case before the recursive call; recurse on a smaller n`

## Board at the end (they photograph this)

```
fact(n):  if n <= 1 return 1;   else return n * fact(n-1)

fact(4)
  fact(3)
    fact(2)
      fact(1) → 1

no base case → stack overflow
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** Scene graphs, kd-trees, closest-pair divide-and-conquer: recursion is not optional in IGWT. Today: factorial so you can see the stack.

**Ask:** What happens if you omit the base case? Wait. Want: stack overflow / infinite recursion.

**Board:** parked strip. Then factorial tree.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *base case, stack*.

**Do not:** No base case.

### Minutes 10–12 — Frame

**Say:** Factorial as a loop is finer. Recursion is for divide-and-conquer **structure**. Fibonacci naive is slow — we will count calls, not invent timings.

**Ask:** What is the base case of `fact`?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Base case first. Then the recursive case on `n-1`, not on `n`.

**Board:** stack frames for `fact(4)`. Then a tree of naive `fib` — explosion of calls.

**Say:** Recursive sum of an array: index `i` or `slice`. Prefer index so you do not copy.

**Ask:** One later IGWT use of recursion? Want: scene graph / kd-tree / closest pair.

**They do:** On paper: stack drawing for `fact(4)`.

**Do not:** mix Python syntax into a JS term. Do not skip the attempt.

### Minutes 35–50 — Show

**Say:** `fact`, then recursive sum. I plant `return n * fact(n)` and we hang. Kill it. Fix `n-1`.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Naive fib + count calls for `fib(8)` or `fib(10)`. Write the number you counted.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: fib + call count; flatten nested array extra. Homework: stack drawing; recursive binary search. Quiz: base case, no base, one later use.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | fact | Plant recurse on n. |
| 15–35 | Recursive sum by index | Slice copy as the wrong extra. |
| 35–50 | fib call count | They see the tree. |
| 50–60 | They draw fact(4) | Circulate. |

Point them at `Programming/code/10-fact.html` as the after-class check, not as the lecture.

---

## Lab

1. fibonacci naive + why it is slow (count calls).
2. flatten a nested array extra.

---

## Homework

1. Written: stack drawing for fact(4).
2. Code: binary search recursive.

---

## Quiz next meeting (they hear this now)

1. Base case of fact (2)
2. What happens with no base (3)
3. One IGWT later use (5)


## Snippet

```js
function fact(n){ if(n<=1) return 1; return n*fact(n-1); }
```

---

## Extra exercises

See [[Programming/exercises/Week 11]].

---

## Notes you may still need (from the outline)

**1. Base case first.** If missing, stack overflow. Write it before the recursive call.

**2. Graphics later.** Scene graphs, kd-trees, closest-pair divide-and-conquer. Recursion is not optional in IGWT.

**3. vs loop.** Factorial as loop is finer. Recursion is for divide-and-conquer structure.

---

## Common mistakes

1. No base case.
2. Recursing on the same n.

## If we run long, cut

Flatten. Keep base case + stack.

## If we run short, add

Tail recursion name only — JS does not guarantee it.
