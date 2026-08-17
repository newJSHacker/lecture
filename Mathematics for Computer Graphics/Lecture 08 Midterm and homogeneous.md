# Lecture 8 — Midterm and homogeneous

**Week 8 of 15** · Mathematics for Computer Graphics  
**Meeting:** written midterm, then leftover lecture + live coding  
**Kernel (after the exam):** homogeneous (x,y,1) vs (x,y,0); translate a triangle with 3×3  
**Success check:** after the exam they can say why translation needs an extra 1

This meeting is an **exam**, then a short class. It is not a normal content lecture. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Printed midterm + spare paper. No laptop for the exam.
- Topic list was announced at the end of Lecture 7.
- After collection: demo `Mathematics for Computer Graphics/code/10-pvm.html` ready (local, no CDN).
- Parked strip (uncover after the exam): `Lecture 8 | Goal: leftover kernel | Invariant: w=1 point, w=0 direction; translation ignores directions`

## Midterm (about 50–60 min)

Written. No laptop. Weeks 1–7.

**Topics:** vectors add/scale/len; point vs vector; dot and projection; 2D cross / i×j; p(t); 2×2 mul and det.

Collect. Do not mark in silence for the rest of the hour — uncover the leftover lecture.

## Board at the end (after the exam; they photograph this)

```
point      (x, y, 1)
direction  (x, y, 0)    lights-as-directions; translation skipped

T(tx,ty) * (x,y,1) = (x+tx, y+ty, 1)
T * (x,y,0) = (x,y,0)
```

## Slides today (cap: 2)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## After the exam (~15–25 min lecture)

**Say:** This meeting is a **midterm**, then homogeneous coordinates. Translation does not fit 2×2 linear. Add a 1. CG I Week 5 is the 4×4 version.

**Ask:** Homogeneous point vs direction.

**They do:** copy the leftover board.

**Do not:** start a new project in the exam hour. Do not skip the leftover kernel if 15 minutes remain.

**2. Homogeneous.** Translation does not fit 2×2 linear. Add a 1. CG I Week 5 is the 4×4 version.

**3. Directions.** w=0 ignores translation. Lights-as-directions.

### Show / attempt if time

**Say:** 3×3 2D affine: translate a triangle. T on a direction unchanged.

**They do:** T(1,0)*point; T*direction unchanged.

---

## Live coding (remaining time)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–20 | Homogeneous column | Plant translating a normal as a point. |
| 20–45 | Translate triangle | w forgotten → garbage. |
| 45–60 | They test w=0 | Circulate. |

---

## Lab

1. T(1,0) * point.
2. T * direction unchanged.

---

## Homework

1. Written: why 3×3 for 2D affine.
2. Midterm reflection.

---

## Quiz next meeting

None this week — midterm. Next quiz is Lecture 9.

## Extra exercises

See [[Mathematics for Computer Graphics/exercises/Week 08]].

## If we run long, cut

4×4. Keep 3×3 + w.

## If we run short, add

Preview 4×4 identity.
