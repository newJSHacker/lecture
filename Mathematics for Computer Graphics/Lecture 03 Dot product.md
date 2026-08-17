# Lecture 3 — Dot product

**Week 3 of 15** · Mathematics for Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** dot product; projection; Lambert as n·ℓ preview  
**Success check:** they compute a·b and a projection, and they know perpendicular means 0

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `Mathematics for Computer Graphics/code/03-dot.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: turn two arrows into one number that means angle | Invariant: a·b = |a||b|cosθ only if you mean that; unit-ize before treating the number as cosine`

## Board at the end (they photograph this)

```
a·b = ax bx + ay by     =  |a||b| cosθ

proj_a b  =  ((a·b)/(a·a)) a

a·b = 0  ⊥     >0 acute     <0 obtuse
Lambert preview:  n·ℓ
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** Lighting and collision are this product. Today 2D. Lambert in Computer Graphics I is n·ℓ — bounce 0, not GI.

**Ask:** If two unit vectors are perpendicular, what is the dot? Wait. Want: 0.

**Board:** parked strip. Then two arrows, shadow of one on the other.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *projection, cosine*.

**Do not:** Forgetting to unit-ize before using as cosine.

### Minutes 10–12 — Frame

**Say:** Two formulas: sum of products, and cosine. Do not mix them with un-normalized vectors and call it cosθ.

**Ask:** cos of 0° between unit vectors?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Algebra first. Then the shadow picture: projection.

**Board:** two arrows; shadow of b on a. Sign: acute / right / obtuse. Back-face intuition.

**Say:** `a·a` in the denominator — zero vector again.

**Ask:** Write the projection formula.

**They do:** On paper: (1,0)·(2,2) and the projection of (2,2) onto (1,0).

**Do not:** start with eigenvalues. Do not mix row-vector formulas.

### Minutes 35–50 — Show

**Say:** Slider θ; show dot and a numeric projection. Demo `03-dot.html`.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** `project(b,a)`. Reject a perpendicular pair with an assert.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Homework: Lambert one sentence; tests including 90°. Quiz: perpendicular, cos 0°, projection formula.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | dot as sum | Forget z if someone pastes 3D. |
| 15–35 | projection | Plant forgetting a·a. |
| 35–50 | sign / back-face | Draw it. |
| 50–60 | They write project | Circulate. |

Point them at `Mathematics for Computer Graphics/code/03-dot.html` as the after-class check, not as the lecture.

---

## Lab

1. project(b,a).
2. Reject a perpendicular pair.

---

## Homework

1. Written: Lambert one sentence.
2. Code: tests including 90°.

---

## Quiz next meeting (they hear this now)

1. dot of perpendicular (3)
2. cos of 0° (2)
3. projection formula (5)


## Snippet

```js
const d = a.x*b.x + a.y*b.y;
```

---

## Extra exercises

See [[Mathematics for Computer Graphics/exercises/Week 03]].

---

## Notes you may still need (from the outline)

**1. Algebra.** a·b = ax bx + ay by (+ az bz). Also |a||b|cosθ.

**2. Projection.** proj_a b = (a·b / a·a) a. Lighting and collision use this.

**3. Sign.** Acute, obtuse, right. Back-face intuition.

---

## Common mistakes

1. Forgetting to unit-ize before using as cosine.
2. 3D forgetting z.

## If we run long, cut

3D z. Keep 2D + projection.

## If we run short, add

Clamp n·ℓ to 0 as Lambert preview.
