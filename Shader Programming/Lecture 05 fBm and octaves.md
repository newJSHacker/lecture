# Lecture 5 — fBm and octaves

**Week 5 of 15** · Shader Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** fBm: sum a*noise(p); p*=2; a*=0.5 — 4–6 octaves  
**Success check:** they can sum 4–6 octaves and name lacunarity and gain

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `Shader Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: octaves as a stack you can turn down | Invariant: fBm is a recipe; cranking octaves until the machine cries is not a measurement`

## Board at the end (they photograph this)

```
octave   freq     amp
  0       1       0.5
  1       2       0.25
  2       4       0.125

lacunarity ~ 2     gain ~ 0.5
do not unroll 20
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | 1 octave vs 6, same uv | photograph |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** Fractional Brownian motion is a recipe, not a proof. Terrain and marble later are this sum. If they unroll twenty octaves, we do not invent fps — we turn octaves down or we omit the speed claim.

**Ask:** What does gain 0.5 do to amplitude each octave? Wait.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *sum scaled noise*.

**Do not:** Unrolled 20 octaves.

### Minutes 10–12 — Frame

**Say:** Parameters: octaves, lacunarity, gain. Warp `noise(p + noise(p))` once. fBm is not lighting.

**Ask:** Why not 20 octaves on a laptop?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Stack amplitudes. Draw three sine-ish layers.

**Board:** the table. Circle 5 as the lab default.

**Say:** One sentence of cost: more octaves = more hash. Measure if you claim; otherwise omit.

**Ask:** Lacunarity in one sentence?

**They do:** On paper: the for-loop of fbm(vec2).

**Do not:** Paste a 200-line Shadertoy as the first kernel.

### Minutes 35–50 — Show

**Say:** fBm slider for octaves; screenshot 1 vs 6. Plant 20 unrolled octaves. Warp extra after they have the sum.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Warp extra, or write the cost sentence. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: warp + cost sentence. Homework: one octave vs fBm; GLSL fbm. Quiz: lacunarity, gain 0.5, mobile octaves.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | One octave | They see value noise again. |
| 10–30 | Octave slider | Plant 20 octaves; no invented fps. |
| 30–45 | Warp once | marble = noise(p+noise(p)). |
| 45–60 | They write fbm() | Circulate. Uniform octaves. |

Point them at `Shader Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. warp extra.
2. measure cost sentence.

---

## Homework

1. Written: one octave vs fBm.
2. GLSL fbm.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```glsl
float fbm(vec2 p){ float a=0.5,s=0.0; for(int i=0;i<5;i++){ s+=a*noise(p); p*=2.0; a*=0.5;} return s; }
```

---

## Extra exercises

See [[Shader Programming/exercises/Week 05]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. unrolled 20 octaves.
2. using fBm as lighting.

## If we run long, cut

Domain warp catalog. Keep 5 octaves + names.

## If we run short, add

Measure one sentence if they insist on speed.
