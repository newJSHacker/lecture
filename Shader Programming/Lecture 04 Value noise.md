# Lecture 4 — Value noise

**Week 4 of 15** · Shader Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** hash, lerp  
**Success check:** Hash a lattice point.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `Shader Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: hash, lerp | Invariant: a shader is a program over pixels or vertices`

## Board at the end (they photograph this)

```
grid corners → bilinear
Lattice.
Lerp.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** Why noise. Fire, water, terrain, film grain.

**Ask:** Hash a lattice point? Wait seven seconds. Take two answers.

**Board:** parked strip. Then grid corners → bilinear.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *hash, lerp*.

**Do not:** True random per frame (fireflies).

### Minutes 10–12 — Frame

**Say:** Today’s question: hash, lerp. Kernel: hash, lerp. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: true random per frame (fireflies).

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Why noise. Fire, water, terrain, film grain.

**Say:** Hash. sin/dot hacks are OK for teaching.

**Say:** Value vs gradient. Value noise interpolates scalars.

**Ask:** Hash a lattice point? Wait seven seconds. Take two answers.

**They do:** On paper: Animate z as time extra.

**Do not:** paste a 200-line Shadertoy as the first kernel.

### Minutes 35–50 — Show

**Say:** Live demo: Fullscreen value noise; slider for scale.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Animate z as time extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Animate z as time extra.; Show lattice overlay.. Homework: Written: why hash.; Code: noise(vec2).. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: hash, lerp | Plant the first common mistake. |
| 10–30 | Fullscreen value noise; slider for scale. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Shader Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. Animate z as time extra.
2. Show lattice overlay.

---

## Homework

1. Written: why hash.
2. Code: noise(vec2).

---

## Quiz next meeting (they hear this now)

1. why no Math.random (3)
2. bilinear (4)
3. artifact (3)


## Snippet

```glsl
float hash(vec2 p){ return fract(sin(dot(p, vec2(127.1,311.7))) * 43758.5453); }
```

---

## Extra exercises

See [[Shader Programming/exercises/Week 04]].

---

## Notes you may still need (from the outline)

**1. Why noise.** Fire, water, terrain, film grain. Deterministic: same uv → same value.

**2. Hash.** sin/dot hacks are OK for teaching. They are not crypto. Artifacts exist — show them.

**3. Value vs gradient.** Value noise interpolates scalars. Perlin interpolates gradients — next week fBm can use either.

---

## Common mistakes

1. true random per frame (fireflies).
2. copying a 200-line library unread.

## If we run long, cut

Value vs gradient

## If we run short, add

Show lattice overlay.
