# Lecture 3 — UV patterns

**Week 3 of 15** · Shader Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** st = fract(uv * n); polar (r, a); checker from step(fract)  
**Success check:** they can make a checker from fract, not from a 4-pixel texture

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `Shader Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: UV as a plane you program | Invariant: a pattern is a function of uv (and time); a texture is optional`

## Board at the end (they photograph this)

```
st = fract(uv * n)

r = length(p)
a = atan(p.y, p.x)     // y, x  — not swapped

smoothstep / fwidth  on edges
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** Procedural is the Shadertoy muscle. If they load a 4-pixel checker PNG they skipped the course. Pause time; the pattern must still be a function.

**Ask:** What does fract(uv.x * 8) do? Wait.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *grid, polar, repeat*.

**Do not:** Texture2D of a 4px checker instead of learning fract.

### Minutes 10–12 — Frame

**Say:** Grid, polar, repeat. atan(y, x). Aliased step() is a teaching moment; smoothstep is the fix, not a style.

**Ask:** Why not texture2D of a tiny checker?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** UV plane. Scale, fract, step.

**Board:** polar. Circle argument order of atan.

**Say:** fwidth named. Brick is offset fract — they try after the checker.

**Ask:** fract vs mod in one sentence?

**They do:** On paper: checker from two step(fract) lines.

**Do not:** Paste a 200-line Shadertoy as the first kernel.

### Minutes 35–50 — Show

**Say:** Fullscreen checker + spinning polar stripes. Plant atan(x,y) swapped. Serve local. No CDN.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Brick pattern or a smoothstep circle. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: brick + AA circle. Homework: fract vs mod; snippet in the repo. Quiz: fract, atan, why smoothstep.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | fract checker | Plant a 4px texture instead. |
| 10–30 | Polar stripes | Plant atan swapped. |
| 30–45 | smoothstep edge | Aliased step() first. |
| 45–60 | They brick or AA | Circulate. Uniform for n. |

Point them at `Shader Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. brick pattern extra.
2. smoothstep anti-alias a circle.

---

## Homework

1. Written: fract vs mod.
2. GLSL snippet in the repo.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```glsl
float checker = step(0.5, fract(uv.x*8.0)) == step(0.5, fract(uv.y*8.0)) ? 0.2 : 0.8;
```

---

## Extra exercises

See [[Shader Programming/exercises/Week 03]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. texture2D of a 4px checker instead of learning fract.
2. atan(x,y) swapped.

## If we run long, cut

Every IQ pattern. Keep fract + polar + one AA.

## If we run short, add

mod as a name next to fract.
