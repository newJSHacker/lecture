# Lecture 4 — Cross product

**Week 4 of 15** · Mathematics for Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** `cross2(a,b) = ax by − ay bx`; triangle normal (b−a)×(c−a)  
**Success check:** they get a signed area and they can show i×j=k on the right-hand rule

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `Mathematics for Computer Graphics/code/04-cross.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: a number that knows left from right | Invariant: IGWT is right-handed; unsigned area throws away the predicate`

## Board at the end (they photograph this)

```
2D:  ax by − ay bx     signed area of parallelogram
     same kernel as orient(a,b,c) in Computational Geometry

3D:  i × j = k     n = (b−a) × (c−a)

flip two vertices → flip n
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** Computational Geometry’s `orient` is this 2D cross. Lighting normals are the 3D cross of edges.

**Ask:** (2,0)×(0,3) in 2D? Wait. Want: 6.

**Board:** parked strip. Then right-hand rule.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *2D signed area, 3D perpendicular*.

**Do not:** Left-handed 'until it looks right'.

### Minutes 10–12 — Frame

**Say:** Right-hand thumb on the axis. Do not switch handedness ‘until it looks right.’

**Ask:** What is i×j?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** 2D signed area. Positive vs negative winding.

**Board:** hands. Triangle normal.

**Say:** Determinant mnemonic for 3D. Area of parallelogram is the magnitude.

**Ask:** Why does winding matter for a GPU triangle?

**They do:** On paper: signed area of triangle (0,0),(1,0),(0,1).

**Do not:** start with eigenvalues. Do not mix row-vector formulas.

### Minutes 35–50 — Show

**Say:** 2D signed area; 3D n on a drawn triangle. Demo `04-cross.html`.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** orient clone; normal of a triangle in the xy plane.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Homework: right-hand rule; tests i×j=k. Quiz: 2D cross, i×j, winding.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–20 | cross2 | Unsigned abs as the wrong extra. |
| 20–40 | orient three points | Collinear → 0. |
| 40–55 | 3D i×j=k | Left-hand plant. |
| 55–60 | They test xy triangle | Circulate. |

Point them at `Mathematics for Computer Graphics/code/04-cross.html` as the after-class check, not as the lecture.

---

## Lab

1. orient clone.
2. Normal of a triangle in the xy plane.

---

## Homework

1. Written: right-hand rule.
2. Code: tests i×j=k.

---

## Quiz next meeting (they hear this now)

1. 2D cross (2,0)×(0,3) (3)
2. i×j (3)
3. why winding matters (4)


## Snippet

```js
function cross2(a,b){ return a.x*b.y - a.y*b.x; }
```

---

## Extra exercises

See [[Mathematics for Computer Graphics/exercises/Week 04]].

---

## Notes you may still need (from the outline)

**1. 2D.** ax by − ay bx. Same as computational geometry `orient` kernel.

**2. 3D.** i × j = k. Determinant of the 3×3 mnemonic. Lighting normals = cross of edges.

**3. Handedness.** IGWT is right-handed. Flipping two vertices flips the normal.

---

## Common mistakes

1. Left-handed 'until it looks right'.
2. Unsigned area only.

## If we run long, cut

Full 3D lighting. Keep 2D + i×j=k.

## If we run short, add

Scalar triple product name only.
