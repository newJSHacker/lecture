# Lecture 8 — Midterm and lighting start

**Week 8 of 15** · WebGL Programming  
**Meeting:** written midterm, then leftover lecture + live coding  
**Kernel (after the exam):** midterm; then Lambert in the fragment: n·l  
**Success check:** after the exam they can pass a normal and shade Lambert without a specular term

This meeting is an **exam**, then a short class. It is not a normal content lecture. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Printed midterm + spare paper. No laptop for the exam.
- Topic list was announced at the end of Lecture 7.
- After collection: demo `WebGL Programming/code/` ready (local, no CDN).
- Parked strip (uncover after the exam): `Lecture 8 | Goal: leftover kernel | Invariant: lighting is a dot product after you normalize; n as color is the debug`

## Midterm (about 50–60 min)

Written. No laptop. Weeks 1–7.

**Topics:** pipeline boxes; buffer layout/stride; #version 300 es; uniform vs attribute; DEPTH_TEST/CCW; texImage2D/UV debug; gl_Position = P*V*M and clip vs NDC.

Collect. Do not mark in silence for the rest of the hour — uncover the leftover lecture.

## Board at the end (after the exam; they photograph this)

```
N, L normalized     L toward the light
ndotl = max(dot(N, L), 0.0)
color = albedo * (ambient + lightColor * ndotl)

DEBUG: outColor = vec4(N*0.5+0.5, 1);
```

## Slides today (cap: 2)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## After the exam (~15–25 min lecture)

**Say:** This meeting is a **midterm**, then Lambert in the FS. No laptop for the exam. After: CG I Lambert, now per fragment. Demo 06-phong-cube.html with spec off.

**Ask:** What is the leftover picture?

**They do:** copy the leftover board.

**Do not:** start a new project in the exam hour. Do not skip the leftover kernel if 15 minutes remain.



### Show / attempt if time

**Say:** Lambert cube; light vector uniform. Plant unnormalized n. Plant lighting in the VS only and calling it per-pixel.

**They do:** n as color debug. Then Lambert.

---

## Live coding (remaining time)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Pass normals as varying | Plant not normalizing after interp. |
| 15–40 | Lambert n·l | Plant L away from the light. |
| 40–60 | n as color | They type. Circulate. |

---

## Lab

1. n as color.
2. two-sided extra.

---

## Homework

1. Written: VS vs FS lighting.
2. reflection.

---

## Quiz next meeting

None this week — midterm. Next quiz is Lecture 9.

## Extra exercises

See [[WebGL Programming/exercises/Week 08]].

## If we run long, cut

Phong specular today. Keep Lambert + n-debug.

## If we run short, add

Two-sided extra: abs(dot) named, then why we usually don't.
