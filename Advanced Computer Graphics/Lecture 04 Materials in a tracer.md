# Lecture 4 — Materials in a tracer

**Week 4 of 15** · Advanced Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** mirror bounce; glass: refract + Schlick mix; max depth  
**Success check:** they can reflect a mirror sphere and name ior 1.5 without unbounded recursion

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `Advanced Computer Graphics/code/02-tracer.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: two materials in a teaching tracer | Invariant: local lighting is bounce 0; GI is the rest`

## Board at the end (they photograph this)

```
mirror:  reflect(ω, n)
glass:   refract, ior 1.5, Schlick k
max depth     Russian roulette named

WebGLPathTracer = oracle after theirs looks like noise
dispersion not required
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** BXDF teaching. Mirror is easy. Dispersion as required fails. Unbounded recursion fails. Production tracers remain oracles.

**Ask:** What stops a hall of mirrors? Wait. Want: max depth / roulette.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *metal, glass names*.

**Do not:** Dispersion as required.

### Minutes 10–12 — Frame

**Say:** Fake glass with reflect-only if refract slips. Lambert floor stays. ior slider extra. Depth 2 vs 5 extra. Microfacet optional extra — RTR already named it.

**Ask:** What is Schlick mixing?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Mirror first. Then glass names.

**Board:** reflect / refract / k. Max depth.

**Say:** Oracle after their noise looks like a picture.

**Ask:** Why not recurse forever?

**They do:** Trace a mirror hit on paper: new direction.

**Do not:** Start with a production path tracer.

### Minutes 35–50 — Show

**Say:** Mirror sphere + glass or reflect-only glass; Lambert floor. Plant dispersion required. Plant depth ∞.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Mirror bounce in the tracer. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: ior extra; depth 2 vs 5. Homework: Schlick sentence. Quiz: mirror, ior, max depth.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Mirror bounce | Plant unbounded recursion. |
| 15–40 | Glass names / Schlick | Plant dispersion lab. |
| 40–55 | Depth 2 vs 5 | They compare stills. |
| 55–60 | Oracle screenshot cited | Circulate. |

Point them at `Advanced Computer Graphics/code/02-tracer.html` as the after-class check, not as the lecture.

---

## Lab

1. ior slider extra.
2. depth 2 vs 5.

---

## Homework

1. Written: TIR.
2. screenshots.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
const k = schlick(cos, 0.04); // mix reflect/refract
```

---

## Extra exercises

See [[Advanced Computer Graphics/exercises/Week 04]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. dispersion as required.
2. unbounded recursion.

## If we run long, cut

Microfacet in-tracer. Keep mirror + depth.

## If we run short, add

Depth 2 vs 5 stills.
