# Lecture 1 — Forward rendering review

**Week 1 of 15** · Real-Time Rendering  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** forward: one geometry pass; lights add in the FS  
**Success check:** they can draw the forward path and count draw calls without inventing fps

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `Real-Time Rendering/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: name the forward pass | Invariant: a frame is a named pass plus a budget; unnamed lights are not a path`

## Board at the end (they photograph this)

```
PASS: forward shade
  for each object:
    for each light:  add in FS

HDR leftover energy  →  later tonemap pass
do not invent fps
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** CG I and WebGL already light a cube. This course is production looks: PBR, HDR, shadows, a post stack you can name, and numbers you measured. A look without a stack graph is a screenshot.

**Ask:** Is deferred this week? Wait. Want: no.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *one pass, lights in FS*.

**Do not:** 10 lights on day one.

### Minutes 8–12 — Frame

**Say:** Forward: each object, for each light, add. Simple. Dies with many lights — clustered/deferred later. Lambert+Blinn can exceed 1; that is why HDR exists, not because we quote 60 fps.

**Ask:** Where do the lights run — CPU draw per light, or a loop in the FS?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** One pass box. Lights live in the FS this week — two is enough.

**Board:** for-each-light add. Circle 'name the pass'.

**Say:** Saturated LDR vs a fake HDR multiply. No CDN. Three.js is an oracle after the picture, not instead of it.

**Ask:** Why can Lambert+Blinn exceed 1?

**They do:** On paper: draw-call count for 1 cube, 2 lights, forward FS loop.

**Do not:** Invent fps numbers. Measure or omit.

### Minutes 35–50 — Show

**Say:** WebGL or Three.js cube, two lights. Saturated LDR vs HDR multiply. Plant ten lights on day one. Do not quote fps.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Draw-call count. Light loop in shader vs CPU. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: draw calls + loop place. Homework: forward vs another Mesh; clip vs no clip screenshot. Quiz: forward path, why HDR, deferred this week?

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Name the forward pass | Plant ten lights. |
| 10–30 | Two lights in FS | Plant '60 fps' with no table. |
| 30–45 | LDR clip vs HDR | They see >1 energy. |
| 45–60 | They count draw calls | Circulate. |

Point them at `Real-Time Rendering/code/` as the after-class check, not as the lecture.

---

## Lab

1. draw call count.
2. light loop in shader vs CPU.

---

## Homework

1. Written: forward vs 'just add another Mesh'.
2. screenshot clip vs no clip.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```glsl
vec3 c = albedo * (nDotL0 + nDotL1);
```

---

## Extra exercises

See [[Real-Time Rendering/exercises/Week 01]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. 10 lights on day one.
2. tonemap skipped then 'PBR looks grey'.

## If we run long, cut

Energy conservation proof. Keep named forward pass + two lights.

## If we run short, add

Light loop in FS vs extra draws — still no invented timings.
