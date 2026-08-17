# Lecture 2 — Vectors

**Week 2 of 15** · Mathematics for Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** vec2 add, sub, scale, len, normalize; refuse p+q  
**Success check:** they subtract two points to get a vector and they do not normalize zero

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `Mathematics for Computer Graphics/code/02-add.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: draw an arrow that is not a point | Invariant: a point is a location; a vector is a displacement; p+q is meaningless`

## Board at the end (they photograph this)

```
point P     vector a (arrow, free to slide)

a + b   parallelogram
s a     stretch
|a|     hypot(ax, ay)
â       a / |a|     if |a| ≠ 0
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** If they cannot say whether something is a point or a vector, they cannot write M correctly. That is the course principle.

**Ask:** Why is P+Q not a point? Wait. Want: two locations do not add; their difference is a vector.

**Board:** parked strip. Then arrow not a point.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *magnitude, add, scale*.

**Do not:** Normalizing zero.

### Minutes 10–12 — Frame

**Say:** CG I Week 4 is this in 3D with w. Today 2D arrows.

**Ask:** What is P − P?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Parallelogram rule. Scale. Length `Math.hypot`.

**Board:** arrow not attached to the origin. Then unit arrow.

**Say:** Zero vector: do not divide. Return a policy (skip, or (0,0) with a comment) — do not NaN silently.

**Ask:** Unit of (0,2)? Want: (0,1).

**They do:** On paper: |(3,4)|. Want: 5.

**Do not:** start with eigenvalues. Do not mix row-vector formulas.

### Minutes 35–50 — Show

**Say:** Interactive two arrows add. Demo `02-add.html`.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Implement add, sub, scale, len, normalize. Tests including zero.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Homework: why p+q is meaningless; 8 tests. Quiz: length (3,4), unit (0,2), p minus p.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | add / parallelogram | Draw it. |
| 15–35 | len / normalize | Plant divide by zero. |
| 35–50 | sub of two points | Label the result a vector. |
| 50–60 | They write tests | Circulate. |

Point them at `Mathematics for Computer Graphics/code/02-add.html` as the after-class check, not as the lecture.

---

## Lab

1. vec2.js: add, sub, scale, len, normalize.
2. Tests including zero.

---

## Homework

1. Written: why p+q is meaningless.
2. Code: 8 tests.

---

## Quiz next meeting (they hear this now)

1. | (3,4) | (2)
2. unit of (0,2) (3)
3. p minus p (5)


## Snippet

```js
function len(a){ return Math.hypot(a.x, a.y); }
```

---

## Extra exercises

See [[Mathematics for Computer Graphics/exercises/Week 02]].

---

## Notes you may still need (from the outline)

**1. Point vs vector.** A point is a location. A vector is a displacement. CG I Week 4 is this with 3D and w.

**2. Operations.** a+b parallelogram. s*a stretch. |a| = hypot.

**3. Normalization.** unit vector. Zero vector: do not divide.

---

## Common mistakes

1. Normalizing zero.
2. Adding points.

## If we run long, cut

3D. Keep 2D + zero policy.

## If we run short, add

Column vs row name; we use columns later.
