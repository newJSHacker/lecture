# Lecture 6 — SDF 2D

**Week 6 of 15** · Shader Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** sdCircle = length(p)-r; min=union, max=intersection; smoothmin name  
**Success check:** they can write circle and box SDF and union two circles minus a box

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `Shader Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: a boolean logo from distances | Invariant: signed distance is a number; a mesh of a 2D logo is the wrong tool this week`

## Board at the end (they photograph this)

```
d = length(p) - r          // <0 inside

min(d1,d2)  union
max(d1,d2)  intersection
max(-d2,d1)  subtract

smoothmin  blends  (can break Lipschitz later)
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** A function returns signed distance. Rendering is smoothstep on d, or sphere tracing in 3D later. IQ's tables are the encyclopedia — we implement three primitives, not fifty.

**Ask:** Is d negative inside the circle? Wait. Want: yes if signed.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *circle, union, smooth*.

**Do not:** Polygon meshes for a 2D logo in a shader course.

### Minutes 10–12 — Frame

**Say:** CSG: min/max. Onion is abs(d)-t. Unsigned-only cannot subtract cleanly.

**Ask:** Why signed, not only |d|?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Circle. Then box as a named sdBox they copy from the board, not from a 200-line paste.

**Board:** CSG tree for two circles minus a box.

**Say:** fwidth AA on the edge. Pause time; the logo is a still you debug.

**Ask:** Union in one operation?

**They do:** On paper: d for a circle at origin radius 0.3.

**Do not:** Paste a 200-line Shadertoy as the first kernel.

### Minutes 35–50 — Show

**Say:** Boolean logo: two circles minus a box. Plant unsigned distance only. AA with fwidth.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Onion (abs(d)-t) extra. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: onion + AA. Homework: why signed; sdCircle + sdBox. Quiz: union op, smoothmin idea, inside sign.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | sdCircle | Plant a triangle mesh logo. |
| 10–30 | CSG logo | Plant unsigned only. |
| 30–45 | fwidth AA | Aliased step(d). |
| 45–60 | They onion | Circulate. Uniform r. |

Point them at `Shader Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. onion (abs(d)-t) extra.
2. AA with fwidth.

---

## Homework

1. Written: why signed.
2. Code: sdCircle + sdBox.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```glsl
float sdCircle(vec2 p, float r){ return length(p) - r; }
```

---

## Extra exercises

See [[Shader Programming/exercises/Week 06]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. polygon meshes for a 2D logo in a shader course.
2. unsigned distance only.

## If we run long, cut

Fifty IQ primitives. Keep circle, box, one CSG.

## If we run short, add

smoothmin as a name; warn Lipschitz.
