# Lecture 6 — Matrices 2×2 and 3×3

**Week 6 of 15** · Mathematics for Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** multiply 2×2 by hand and in code; show AB ≠ BA on a square  
**Success check:** they multiply 2×2 and they can say columns are where the basis goes

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `Mathematics for Computer Graphics/code/06-matmul.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: a linear map as a box of numbers | Invariant: column vectors; multiplication is composition; not commutative`

## Board at the end (they photograph this)

```
columns of A = images of basis e1, e2

I A = A
AB ≠ BA     (same story as T R vs R T)

v' = A v
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** A matrix is a linear function. Columns are where basis vectors go. That sentence is Computer Graphics I’s model matrix.

**Ask:** Is AB the same as BA? Wait. Want: no.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *multiply 2×2 by hand and in code; show AB ≠ BA on a square*.

**Do not:** Row-vector formulas mixed.

### Minutes 10–12 — Frame

**Say:** We use **column** vectors in this program. Do not mix row-vector formulas from a random blog.

**Ask:** What is I times A?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Identity. Then multiply: row-column. Composition.

**Board:** basis images. Non-commute: scale then rotate vs reverse.

**Say:** Rotate/scale as 2×2. Code: tiny `mul2`; nested loops later.

**Ask:** 2×2 rotate 90° of (1,0) — freeze **one** convention on the board.

**They do:** Multiply two 2×2 matrices by hand.

**Do not:** Start with eigenvalues. Mix row-vector formulas.

### Minutes 35–50 — Show

**Say:** Apply a 2×2 to a square’s four corners; before/after. Demo `06-matmul.html`.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** mat2 mul tests; scale then rotate vs reverse.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Homework: columns as images of basis; mul2. Quiz: I A, AB vs BA, rotate 90 of (1,0).

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | By hand mul | Row-vector plant. |
| 15–40 | Square corners | Non-commute. |
| 40–55 | mul2 | Index bugs. |
| 55–60 | They write I test | Circulate. |

Point them at `Mathematics for Computer Graphics/code/06-matmul.html` as the after-class check, not as the lecture.

---

## Lab

1. mat2 mul tests.
2. Scale then rotate vs reverse.

---

## Homework

1. Written: columns as images of basis.
2. Code: mul2.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
function mul2(A,B){ /* 2×2 */ }
```

---

## Extra exercises

See [[Mathematics for Computer Graphics/exercises/Week 06]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Row-vector formulas mixed.
2. Commuting blindly.

## If we run long, cut

3×3. Keep 2×2 + non-commute.

## If we run short, add

3×3 identity named.
