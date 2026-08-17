# Lecture 12 — Frames and change of basis

**Week 12 of 15** · Mathematics for Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** a frame = origin + axes; orthonormal 2D from one vector + perp; lookAt sketch  
**Success check:** they can say M’s columns are object axes in world

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `Mathematics for Computer Graphics/code/09-lookat.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: name where you are standing | Invariant: a frame is origin + axes; orthonormal means length 1 and dot 0`

## Board at the end (they photograph this)

```
frame: origin + x-axis + y-axis (+ z)

columns of M = object axes (and origin) in world

orthonormal:  |axis|=1,  axis_i · axis_j = 0
lookAt builds one
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** Object space is a frame. World is a frame. Camera is a frame. The model matrix **is** a frame.

**Ask:** What is a frame, in three words? Wait. Want: origin plus axes.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *a frame = origin + axes; orthonormal 2D from one vector + perp; lookAt sketch*.

**Do not:** Scaling axes and still calling them orthonormal.

### Minutes 10–12 — Frame

**Say:** CG I Week 6. Right-handed three axes. Scaling axes and still calling them orthonormal is a bug.

**Ask:** Are scaled axes orthonormal?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Two frames, same point, two coordinate pairs.

**Board:** columns. Change of coordinates teaching-level.

**Say:** Build orthonormal 2D: n = normalize(v), perp = (−n.y, n.x) in right-handed 2D.

**Ask:** M’s columns?

**They do:** Sketch lookAt: eye, target, up → axes.

**Do not:** Start with eigenvalues. Mix row-vector formulas.

### Minutes 35–50 — Show

**Say:** Local frame on a rotated box; world frame. Demo `09-lookat.html`.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Orthonormal 2D from one vector + perp; tests.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Homework: M’s columns; rotate a frame. Quiz: frame, columns, orthonormal. Next week maps this course onto Computer Graphics I.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–20 | Two frames | Same point. |
| 20–40 | Columns of M | Origin in the last column / homogeneous reminder. |
| 40–55 | lookAt sketch | Do not derive the full 4×4 if time is short. |
| 55–60 | They build perp | Circulate. |

Point them at `Mathematics for Computer Graphics/code/09-lookat.html` as the after-class check, not as the lecture.

---

## Lab

1. Build orthonormal 2D from one vector + perp.
2. Tests.

---

## Homework

1. Written: M's columns.
2. Code: rotate a frame.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
// columns of M = object axes in world
```

---

## Extra exercises

See [[Mathematics for Computer Graphics/exercises/Week 12]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Scaling axes and still calling them orthonormal.

## If we run long, cut

Full lookAt 4×4. Keep 2D orthonormal + columns.

## If we run short, add

Name the camera frame.
