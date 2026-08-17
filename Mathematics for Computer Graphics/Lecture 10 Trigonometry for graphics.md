# Lecture 10 — Trigonometry for graphics

**Week 10 of 15** · Mathematics for Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** `(x,y) = (r cos t, r sin t)`; N-gon vertices  
**Success check:** they convert polar to cartesian in radians and they know sin²+cos²=1

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `Mathematics for Computer Graphics/code/07-rotate.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: put a point on a circle | Invariant: trig in this course is the unit circle and polar — not a trig identity exam`

## Board at the end (they photograph this)

```
unit circle: (cos θ, sin θ)
polar:  x = r cos θ,  y = r sin θ
sin²+cos² = 1     (only identity required)

Math.cos(degrees) is wrong
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** A planet, a pendulum, an N-gon, a cylinder vertex: polar. Law of cosines named for a lighting picture — not a lab.

**Ask:** cos(0)? Wait. Want: 1.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *`(x,y) = (r cos t, r sin t)`; N-gon vertices*.

**Do not:** Sin(degrees).

### Minutes 10–12 — Frame

**Say:** Small-angle approximations not required. Oscillation as animation: y = cos(t).

**Ask:** Why sin²+cos² matters for a unit vector?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Unit circle. Polar.

**Board:** N-gon vertices from i * 2π/N.

**Say:** r=0 is a point, not a crash. Degrees plant.

**Ask:** Polar to xy formula.

**They do:** Vertices of a square from polar (r, k·π/2).

**Do not:** Start with eigenvalues. Mix row-vector formulas.

### Minutes 35–50 — Show

**Say:** Point on a circle, θ slider; pendulum. Demo rotate page or axes.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** polar(r,θ); Lissajous extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Homework: polar to a cylinder vertex extra; N-gon. Quiz: cos 0, polar, why sin²+cos².

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Unit circle | Degrees in cos. |
| 15–40 | N-gon | Off-by-one closing the loop. |
| 40–55 | Pendulum | t in radians. |
| 55–60 | They write polar() | Circulate. |

Point them at `Mathematics for Computer Graphics/code/07-rotate.html` as the after-class check, not as the lecture.

---

## Lab

1. polar(r,θ).
2. Lissajous extra.

---

## Homework

1. Written: from polar to a vertex on a cylinder extra.
2. Code: N-gon vertices.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
x = r * Math.cos(t); y = r * Math.sin(t);
```

---

## Extra exercises

See [[Mathematics for Computer Graphics/exercises/Week 10]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. sin(degrees).
2. r=0 polar crash.

## If we run long, cut

Lissajous. Keep polar + N-gon.

## If we run short, add

Law of cosines on the board as a name.
