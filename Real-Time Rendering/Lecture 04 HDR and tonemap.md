# Lecture 4 — HDR and tonemap

**Week 4 of 15** · Real-Time Rendering  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** HDR shade → tonemap pass (Reinhard or ACES name) → then sRGB encode  
**Success check:** they can store HDR, expose, Reinhard, and say why not clamp and why not tonemap per light

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `Real-Time Rendering/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: map HDR to the monitor without inventing scores | Invariant: tonemap is a named display pass; per-light tonemap is a bug`

## Board at the end (they photograph this)

```
PASS 1  shade in HDR     (sun >> 1)
PASS 2  tonemap          Reinhard: x/(1+x)   or ACES name
PASS 3  encode sRGB

order:  tonemap then encode
do not tonemap per light
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** Sun is >> 1. Bloom next week needs leftover energy. Clamp-to-1 throws the look away. We pick one operator and document it — we do not invent how many ms ACES costs.

**Ask:** Tonemap each light then add? Wait. Want: no.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *Reinhard / ACES names*.

**Do not:** Tonemap per light.

### Minutes 10–12 — Frame

**Say:** Reinhard, filmic, ACES — names. Exposure is a uniform before the operator. Gamma backwards (encode then tonemap) is a plant.

**Ask:** Why not clamp?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** HDR bar on the board: 0, 1, 10.

**Board:** three passes. Circle order vs gamma.

**Say:** False-color extra is a debug view of this buffer, not a fps claim.

**Ask:** Write Reinhard in one line.

**They do:** On paper: order shade → tonemap → encode.

**Do not:** Invent fps numbers. Measure or omit.

### Minutes 35–50 — Show

**Say:** Overbright cube; exposure; Reinhard. Plant tonemap per light. ACES as a comment name.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** ACES name in comments, or false-color HDR extra. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: ACES name + false-color. Homework: why not clamp; reinhard(). Quiz: Reinhard, exposure, order vs gamma.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | HDR buffer | Plant clamp. |
| 10–30 | Reinhard + exposure | Plant per-light tonemap. |
| 30–45 | Then encode | Plant gamma first. |
| 45–60 | They false-color | Circulate. No invented fps. |

Point them at `Real-Time Rendering/code/` as the after-class check, not as the lecture.

---

## Lab

1. ACES extra name in comments.
2. false-color HDR extra.

---

## Homework

1. Written: why not clamp.
2. Code: reinhard.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```glsl
vec3 reinhard(vec3 x){ return x / (1.0 + x); }
```

---

## Extra exercises

See [[Real-Time Rendering/exercises/Week 04]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. tonemap per light.
2. gamma then tonemap backwards.

## If we run long, cut

Full ACES fit. Keep Reinhard + named order.

## If we run short, add

ACES as a documented name.
