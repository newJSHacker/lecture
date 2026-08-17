# Lecture 8 — Midterm and perspective projection

**Week 8 of 15** · Computer Graphics I  
**Meeting:** written midterm, then leftover lecture + live coding  
**Kernel (after the exam):** perspective(fov, aspect, near, far); ortho; last row copies −z into w; near>0  
**Success check:** after the exam they can toggle ortho/perspective on the cube and read clip.w; cube grows when fov shrinks

This meeting is an **exam**, then a short class. It is not a normal content lecture. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Printed midterm + spare paper. No laptop for the exam.
- Topic list was announced at the end of Lecture 7.
- After collection: demo `Computer Graphics/code/08-rotate-center.html` ready (local, no CDN).
- Parked strip (uncover after the exam): `Lecture 8 | Goal: leftover kernel | Invariant: a picture is an array; putPixel lives in pixels`

## Midterm (about 50–60 min)

Written. No laptop. Weeks 1–7.

**Topics:** six spaces; P*V*M; canvas vs world origin; over; barycentric centroid and pixel centers; point vs vector (w); T R vs R T; rotate about c; 2×2 rotation; scene-graph leaf product; lookAt; V*eye; degenerate up; normal matrix name only. No full P derivation on the paper.

Collect. Do not mark in silence for the rest of the hour — uncover the leftover lecture.

## Board at the end (after the exam; they photograph this)

```
ortho: box → clip cube     no foreshorten
persp: frustum  fov (radians, vertical)  aspect  near  far

sy = 1/tan(fov/2)    sx = sy/aspect
P last row (0,0,−1,0)  copies −z into w

near > 0     far > near     near = 0 forbidden
Do not divide by w today — look at clip.w. Divide is Week 9.
```

## Slides today (cap: 2)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## After the exam (~15–25 min lecture)

**Say:** This meeting is a **midterm**, then perspective. No laptop. After: we finally write P. If the cube is behind the camera, V is wrong — do not ‘fix’ P.

**Ask:** What is the leftover picture?

**They do:** copy the leftover board.

**Do not:** start a new project in the exam hour. Do not skip the leftover kernel if 15 minutes remain.



### Show / attempt if time

**Say:** perspective and ortho. Course cube, M=I, V=lookAt, P=perspective. Toggle ortho. Print p_clip for one vertex. Demo 11-perspective.html. Plant fov in degrees into tan. Plant aspect = height/width.

**They do:** Slider fov. Cube must grow when fov shrinks. Aspect from canvas width/height.

---

## Live coding (remaining time)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Write P once; test a center-line point | Plant near=0. |
| 15–40 | Cube foreshortens | If behind camera, fix V not P. |
| 40–60 | Ortho toggle | Flat engineering drawing vs recede. |

---

## Lab

1. Implement `perspective` with a unit test: a point on the camera’s look axis has ndc.x ≈ 0 after divide (Week 9 can finish divide; this week you may divide in JS for the test).
2. Slider fov. Cube must grow when fov shrinks.
3. Aspect from canvas width/height.

---

## Homework

1. Written: why far/near too huge hurts depth (tease Week 9).
2. Code: `ortho` + toggle.
3. Midterm reflection optional: one mistake you will not repeat.

---

## Quiz next meeting

None this week — midterm. Next quiz is Lecture 9.

## Extra exercises

See [[Computer Graphics/exercises/Week 08]].

## If we run long, cut

Full a,b derivation from near/far if time is gone. Quote Shirley / Scratchapixel and test a point.

## If we run short, add

Print clip.w for a near vs far vertex.
