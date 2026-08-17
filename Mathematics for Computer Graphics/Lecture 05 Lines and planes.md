# Lecture 5 — Lines and planes

**Week 5 of 15** · Mathematics for Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** `p(t) = a + t d`; segment t∈[0,1], ray t≥0; plane n·(x−p)=0  
**Success check:** they can write a parametric line and say the t domain of a segment

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `Mathematics for Computer Graphics/code/05-line.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: name the set of points on a line | Invariant: t unclamped is a line, not a segment`

## Board at the end (they photograph this)

```
p(t) = a + t d
  line: t ∈ ℝ     ray: t ≥ 0     segment: t ∈ [0,1]

plane:  n · (x − p) = 0
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** Rays, segments, planes: the same objects Computer Graphics I will intersect. Today the equations.

**Ask:** What t values make a segment? Wait. Want: 0 to 1.

**Board:** parked strip. Then line p(t)=a+t d.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *parametric, implicit*.

**Do not:** T unclamped calling it a segment.

### Minutes 10–12 — Frame

**Say:** A triangle defines a plane. Ray–triangle later uses this plus barycentric. Distance to line is optional (cross/|d|).

**Ask:** Ray vs line in one sentence?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Parametric first — it codes. Implicit 2D ax+by+c=0 teaching.

**Board:** p(t). Plane. Mark t=0 and t=1.

**Say:** Intersect ray vs plane idea: solve for t, then test domain.

**Ask:** Write the plane equation.

**They do:** On paper: point at t=0.5 on a segment.

**Do not:** start with eigenvalues. Do not mix row-vector formulas.

### Minutes 35–50 — Show

**Say:** Drag a ray across a line; mark t. Demo `05-line.html`.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** onSegment using t and a bounding box; ray–line intersection 2D.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Homework: ray vs segment; closest point on segment extra. Quiz: t domain, plane, ray vs line.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | p(t) draw | t=2 still drawn as a segment — plant. |
| 15–40 | Intersect | No hit vs t<0. |
| 40–55 | Plane in 3D on paper | n not unit for equation (ok) vs distance (need |n|). |
| 55–60 | They clamp t | Circulate. |

Point them at `Mathematics for Computer Graphics/code/05-line.html` as the after-class check, not as the lecture.

---

## Lab

1. onSegment using t and bounding box.
2. Ray–line intersection 2D.

---

## Homework

1. Written: ray vs segment.
2. Code: t for closest point on segment extra.

---

## Quiz next meeting (they hear this now)

1. t domain of a segment (3)
2. plane equation (4)
3. ray vs line (3)


## Snippet

```js
const p = { x: a.x + t*d.x, y: a.y + t*d.y };
```

---

## Extra exercises

See [[Mathematics for Computer Graphics/exercises/Week 05]].

---

## Notes you may still need (from the outline)

**1. Parametric.** p(t) = a + t d. Segment t∈[0,1], ray t≥0. Same as CG geometry objects.

**2. Planes.** A triangle defines a plane. Ray–triangle later uses this plus barycentric.

**3. Distance.** Point to line in 2D via cross/|d|. Optional.

---

## Common mistakes

1. t unclamped calling it a segment.
2. n not unit for distance without dividing.

## If we run long, cut

Full ray–triangle. Keep parametric + domain.

## If we run short, add

AABB reject name.
