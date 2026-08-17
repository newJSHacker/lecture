# Lecture 3 — UV patterns

**Week 3 of 15** · Shader Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** grid, polar, repeat  
**Success check:** Make a checker.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `Shader Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: grid, polar, repeat | Invariant: a shader is a program over pixels or vertices`

## Board at the end (they photograph this)

```
st = fract(uv * n)
UV plane.
Polar.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** Procedural. Patterns are functions of uv and time.

**Ask:** Make a checker? Wait seven seconds. Take two answers.

**Board:** parked strip. Then st = fract(uv * n).

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *grid, polar, repeat*.

**Do not:** Texture2D of a 4px checker instead of learning fract.

### Minutes 10–12 — Frame

**Say:** Today’s question: grid, polar, repeat. Kernel: grid, polar, repeat. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: texture2D of a 4px checker instead of learning fract.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Procedural. Patterns are functions of uv and time.

**Say:** polar. `r = length(p); a = atan(p.y,p.x);`

**Say:** AA. fwidth/smoothstep for edges.

**Ask:** Make a checker? Wait seven seconds. Take two answers.

**They do:** On paper: brick pattern extra.

**Do not:** paste a 200-line Shadertoy as the first kernel.

### Minutes 35–50 — Show

**Say:** Live demo: Fullscreen checker + spinning polar stripes.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** brick pattern extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: brick pattern extra.; smoothstep anti-alias a circle.. Homework: Written: fract vs mod.; GLSL snippet in the repo.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: grid, polar, repeat | Plant the first common mistake. |
| 10–30 | Fullscreen checker + spinning polar stripes. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. fract purpose (3)
2. atan (3)
3. why smoothstep (4)


## Snippet

```glsl
float checker = step(0.5, fract(uv.x*8.0)) == step(0.5, fract(uv.y*8.0)) ? 0.2 : 0.8;
```

---

## Extra exercises

See [[Shader Programming/exercises/Week 03]].

---

## Notes you may still need (from the outline)

**1. Procedural.** Patterns are functions of uv and time. This is the Shadertoy muscle.

**2. polar.** `r = length(p); a = atan(p.y,p.x);`

**3. AA.** fwidth/smoothstep for edges. Aliased step() is a teaching moment.

---

## Common mistakes

1. texture2D of a 4px checker instead of learning fract.
2. atan(x,y) swapped.

## If we run long, cut

AA

## If we run short, add

smoothstep anti-alias a circle.
