# Lecture 7 — Inverse and systems

**Week 7 of 15** · Mathematics for Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** det 2×2; invert when det≠0; rotation inverse is transpose  
**Success check:** they compute det, invert a rotation by transpose, and refuse det 0

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `Mathematics for Computer Graphics/code/06-matmul.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: undo a linear map when you may | Invariant: det is area scale; det 0 means no inverse — collapsed geometry`

## Board at the end (they photograph this)

```
det [a b; c d] = ad − bc     area scale; negative = flip

R⁻¹ = Rᵀ     (rotation)
(sI)⁻¹ = (1/s) I   if s ≠ 0

det = 0  →  singular, no inverse
normals preview: (M⁻¹)ᵀ
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** Undo. If det=0 the geometry collapsed. Inverting by transposing a **scale** is a bug.

**Ask:** What is det of a rotation? Wait. Want: 1 (or −1 if a flip snuck in).

**Board:** parked strip. Then det as area scale.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *2×2 inverse, det*.

**Do not:** Inverting by transposing a scale.

### Minutes 10–12 — Frame

**Say:** Solve 2×2 with inverse at teaching level. (M⁻¹)ᵀ for normals: name it; 2D non-uniform scale demo.

**Ask:** Singular means?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Area scale picture. Negative det flips winding.

**Board:** no inverse. Transpose of R.

**Say:** Divide by det 0 → do not. Detect and throw or skip.

**Ask:** Inverse of Ry — wait, 2D R(θ)? Want: R(−θ) = transpose.

**They do:** Invert [[2,0],[0,2]] and try [[1,0],[2,0]].

**Do not:** start with eigenvalues. Do not mix row-vector formulas.

### Minutes 35–50 — Show

**Say:** Non-uniform scale a square; wrong vs right normal. Demo matmul page or board.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** invert2 when det≠0; detect singular.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Homework: det 0 picture; tests. Quiz: det of rotate, inverse of R, singular. Midterm next week: vec, dot, cross, mul2, det — then homogeneous after the exam.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | det by hand | Sign. |
| 15–40 | invert2 | Plant transpose of scale. |
| 40–55 | normal demo | Non-uniform. |
| 55–60 | They detect singular | Circulate. |

Point them at `Mathematics for Computer Graphics/code/06-matmul.html` as the after-class check, not as the lecture.

---

## Lab

1. invert2 when det≠0.
2. Detect singular.

---

## Homework

1. Written: det 0 picture.
2. Code: tests.

---

## Quiz next meeting (they hear this now)

1. det of rotate (2)
2. inverse of Ry (4)
3. singular meaning (4)


## Snippet

```js
const det = a*d - b*c;
```

---

## Extra exercises

See [[Mathematics for Computer Graphics/exercises/Week 07]].

---

## Notes you may still need (from the outline)

**1. Determinant.** Area scale. Negative means flip (reflection / winding).

**2. Inverse.** Undo. Rotation inverse is transpose. If det=0, no inverse — collapsed geometry.

**3. Normals preview.** (M⁻¹)ᵀ in CG I. Name it; compute in 2D on a non-uniform scale.

---

## Common mistakes

1. Inverting by transposing a scale.
2. Dividing by det 0.

## If we run long, cut

Gaussian elimination. Keep det + 2×2 inverse.

## If we run short, add

Cramer name only.
