# Lecture 5 — fBm and octaves

**Week 5 of 15** · Shader Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** sum scaled noise  
**Success check:** Sum 4–6 octaves.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `Shader Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: sum scaled noise | Invariant: a shader is a program over pixels or vertices`

## Board at the end (they photograph this)

```
amp 1/2/4, freq 1/2/4
Octave stack.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** fBm. Fractional Brownian motion as a *recipe*, not a proof.

**Ask:** Sum 4–6 octaves? Wait seven seconds. Take two answers.

**Board:** parked strip. Then amp 1/2/4, freq 1/2/4.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *sum scaled noise*.

**Do not:** Unrolled 20 octaves.

### Minutes 10–12 — Frame

**Say:** Today’s question: sum scaled noise. Kernel: sum scaled noise. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: unrolled 20 octaves.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** fBm. Fractional Brownian motion as a *recipe*, not a proof.

**Say:** Parameters. octaves, lacunarity (~2), gain (~0.5).

**Say:** Warp. `noise(p + noise(p))` marble.

**Ask:** Sum 4–6 octaves? Wait seven seconds. Take two answers.

**They do:** On paper: warp extra.

**Do not:** paste a 200-line Shadertoy as the first kernel.

### Minutes 35–50 — Show

**Say:** Live demo: fBm slider for octaves; screenshot 1 vs 6.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** warp extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: warp extra.; measure cost sentence.. Homework: Written: one octave vs fBm.; GLSL fbm.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: sum scaled noise | Plant the first common mistake. |
| 10–30 | fBm slider for octaves; screenshot 1 vs 6. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. lacunarity (3)
2. why gain 0.5 (4)
3. mobile octaves (3)


## Snippet

```glsl
float fbm(vec2 p){ float a=0.5,s=0.0; for(int i=0;i<5;i++){ s+=a*noise(p); p*=2.0; a*=0.5;} return s; }
```

---

## Extra exercises

See [[Shader Programming/exercises/Week 05]].

---

## Notes you may still need (from the outline)

**1. fBm.** Fractional Brownian motion as a *recipe*, not a proof. Terrain height, clouds, marble (warp).

**2. Parameters.** octaves, lacunarity (~2), gain (~0.5). Students crank octaves until fps dies.

**3. Warp.** `noise(p + noise(p))` marble. Show once.

---

## Common mistakes

1. unrolled 20 octaves.
2. using fBm as lighting.

## If we run long, cut

Warp

## If we run short, add

measure cost sentence.
