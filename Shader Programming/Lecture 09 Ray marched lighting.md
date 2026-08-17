# Lecture 9 — Ray marched lighting

**Week 9 of 15** · Shader Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** secondary march toward L; soft = min(d/t); AO samples along n  
**Success check:** they can march a shadow ray and toggle a cheap AO

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `Shader Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: two rays: camera and light | Invariant: if map hits before the light, it is shadowed; AO is a fake, named`

## Board at the end (they photograph this)

```
cam ray  →  hit p
shadow   →  march p → L
  blocked if d hits before light

soft: track min(d/t)
AO:  sample SDF along n   (not SSAO unless you say so)
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** Last time: one ray. Today a second ray toward the light. Stencil shadows are a different course. SSAO is Real-Time Rendering — name the difference if it comes up.

**Ask:** If map(p) hits before L, is the point lit? Wait. Want: no.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *soft shadow, AO names*.

**Do not:** Stencil shadows speech.

### Minutes 10–12 — Frame

**Say:** Hard shadow is a hit. Soft is IQ's min d/t. AO darkens crevices. Material id from map() return is extra.

**Ask:** Why a second march?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Two arrows from p: to camera origin is the first ray already done; toward L is new.

**Board:** shadow() stub. Circle blocked.

**Say:** Pause time; debug the shadow with a still. Uniform for AO on/off.

**Ask:** Soft shadow in one phrase?

**They do:** On paper: steps of shadow() until blocked or arrived.

**Do not:** Paste a 200-line Shadertoy as the first kernel.

### Minutes 35–50 — Show

**Say:** Sphere+plane, soft-ish shadow. Plant a stencil-shadow speech. AO toggle.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** AO toggle. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: AO + material id extra. Homework: why second march; shadow(). Quiz: hit before light, soft idea, AO.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Shadow ray | Plant stencil speech. |
| 10–30 | Soft min(d/t) | Plant AO called SSAO without saying. |
| 30–45 | AO along n | Toggle uniform. |
| 45–60 | They add material id | Circulate. |

Point them at `Shader Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. AO toggle.
2. material id extra.

---

## Homework

1. Written: why second march.
2. Code: shadow().

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```glsl
float shadow(vec3 p, vec3 l){ /* march toward l, return 0 if blocked */ }
```

---

## Extra exercises

See [[Shader Programming/exercises/Week 09]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. stencil shadows speech.
2. AO as SSAO from RTR without saying so.

## If we run long, cut

Production IQ shadow. Keep second march + AO name.

## If we run short, add

Object id from map() as extra.
