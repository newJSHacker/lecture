# Lecture 11 — Interpolation and curves

**Week 11 of 15** · Mathematics for Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** `lerp(a,b,t)`; quadratic Bezier as lerp of lerps; cubic sampled  
**Success check:** they write lerp and a quadratic Bezier and they know t is not arc length

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `Mathematics for Computer Graphics/code/08-bezier.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: walk from A to B, then along a handle | Invariant: t is a parameter, not distance; slerp is a different word`

## Board at the end (they photograph this)

```
lerp(a,b,t) = a + t(b−a)

quadratic: lerp( lerp(A,C,t), lerp(C,B,t), t )   De Casteljau

t ∉ [0,1]  →  say whether you extrapolate
t is not arc length
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** Colors, camera paths, keyframes, fonts, SVG: lerp and Bézier. Do not call Bézier slerp.

**Ask:** lerp t=0 is? Wait. Want: a.

**Board:** parked strip. Then lerp on a segment; cubic Bezier.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *lerp, Bezier intro*.

**Do not:** T outside [0,1] without saying if extrapolating.

### Minutes 10–12 — Frame

**Say:** Policy: clamp t or allow extrapolate — say it. Cubic Bézier named for fonts/UI.

**Ask:** Is t=0.5 halfway in **distance** on a cubic? Want: not necessarily.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Segment picture. Then De Casteljau.

**Board:** handles. Two control points for cubic.

**Say:** Sample 32 points. Parametric speed warning.

**Ask:** Quadratic as lerps — say it.

**They do:** lerp tests t=0,1,0.5 on paper.

**Do not:** start with eigenvalues. Do not mix row-vector formulas.

### Minutes 35–50 — Show

**Say:** Drag 4 Bézier handles; sample 32. Demo `08-bezier.html`.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** lerp tests; quadratic Bezier function.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Homework: t vs distance; cubic Bézier. Quiz: lerp t=0, quadratic as lerps, arc-length warning.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | lerp | Wrong formula a+t*b. |
| 15–40 | Quadratic | De Casteljau. |
| 40–55 | Cubic sample | t vs speed. |
| 55–60 | They test t=0,1 | Circulate. |

Point them at `Mathematics for Computer Graphics/code/08-bezier.html` as the after-class check, not as the lecture.

---

## Lab

1. lerp tests t=0,1,0.5.
2. Quadratic Bezier function.

---

## Homework

1. Written: t vs distance.
2. Code: cubic Bezier.

---

## Quiz next meeting (they hear this now)

1. lerp t=0 (2)
2. quadratic as lerps (5)
3. arc length warning (3)


## Snippet

```js
function lerp(a,b,t){ return a + (b-a)*t; }
```

---

## Extra exercises

See [[Mathematics for Computer Graphics/exercises/Week 11]].

---

## Notes you may still need (from the outline)

**1. lerp.** a + t(b-a). Colors, camera paths, keyframes.

**2. Bezier.** De Casteljau. Two control points for cubic. SVG and fonts.

**3. Parametric speed.** t is not arc length. Mention; do not implement arc-length this term.

---

## Common mistakes

1. t outside [0,1] without saying if extrapolating.
2. Calling Bezier slerp.

## If we run long, cut

Arc-length parameterization. Keep lerp + quadratic.

## If we run short, add

Name slerp once.
