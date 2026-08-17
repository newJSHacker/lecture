# Lecture 4 — Materials in a tracer

**Week 4 of 15** · Advanced Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** metal, glass names  
**Success check:** Perfect mirror bounce.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `Advanced Computer Graphics/code/02-tracer.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: metal, glass names | Invariant: local lighting is bounce 0; GI is the rest`

## Board at the end (they photograph this)

```
reflect; refract; TIR
Reflect / refract.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** BXDF teaching. Mirror is easy.

**Ask:** Perfect mirror bounce? Wait seven seconds. Take two answers.

**Board:** parked strip. Then reflect; refract; TIR.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *metal, glass names*.

**Do not:** Dispersion as required.

### Minutes 10–12 — Frame

**Say:** Today’s question: metal, glass names. Kernel: metal, glass names. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: dispersion as required.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** BXDF teaching. Mirror is easy.

**Say:** Recursion. Max depth.

**Say:** Three.js. WebGLPathTracer / similar as **oracle** after theirs looks like noise.

**Ask:** Perfect mirror bounce? Wait seven seconds. Take two answers.

**They do:** On paper: ior slider extra.

**Do not:** start with a production path tracer.

### Minutes 35–50 — Show

**Say:** Live demo: A mirror sphere and a glass sphere (or fake glass with reflect-only if refract slips); still Lambert floor.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** ior slider extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: ior slider extra.; depth 2 vs 5.. Homework: Written: TIR.; screenshots.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: metal, glass names | Plant the first common mistake. |
| 10–30 | A mirror sphere and a glass sphere (or fake glass with reflect-only if refract slips); still Lambert floor. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. Schlick (3)
2. TIR (4)
3. max depth (3)


## Snippet

```js
const k = schlick(cos, 0.04); // mix reflect/refract
```

---

## Extra exercises

See [[Advanced Computer Graphics/exercises/Week 04]].

---

## Notes you may still need (from the outline)

**1. BXDF teaching.** Mirror is easy. Glass: `refract`, ior 1.5, Schlick mix. Microfacet in a tracer is RTR+this — optional extra.

**2. Recursion.** Max depth. Russian roulette name.

**3. Three.js.** WebGLPathTracer / similar as **oracle** after theirs looks like noise.

---

## Common mistakes

1. dispersion as required.
2. unbounded recursion.

## If we run long, cut

Three.js

## If we run short, add

depth 2 vs 5.
