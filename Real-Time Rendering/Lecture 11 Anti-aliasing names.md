# Lecture 11 — Anti-aliasing names

**Week 11 of 15** · Real-Time Rendering  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** MSAA, TAA, FXAA  
**Success check:** MSAA: samples at geometry edges, limited on deferred.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `Real-Time Rendering/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: MSAA, TAA, FXAA | Invariant: a frame is a budget; name the pass`

## Board at the end (they photograph this)

```
table: where / cost / blur
AA table.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Screenshot of the demo or a bug | photograph / animation / 20pt code only |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** Why aliasing. Edges, specular sparkle, thin geometry, alpha test.

**Ask:** MSAA: samples at geometry edges, limited on deferred? Wait seven seconds. Take two answers.

**Board:** parked strip. Then table: where / cost / blur.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *MSAA, TAA, FXAA*.

**Do not:** TAA as required homework.

### Minutes 10–12 — Frame

**Say:** Today’s question: MSAA, TAA, FXAA. Kernel: MSAA, TAA, FXAA. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: TAA as required homework.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Why aliasing. Edges, specular sparkle, thin geometry, alpha test.

**Say:** Deferred vs MSAA. MSAA hates deferred.

**Say:** Alpha. Alpha-to-coverage name.

**Ask:** MSAA: samples at geometry edges, limited on deferred? Wait seven seconds. Take two answers.

**They do:** On paper: written table.

**Do not:** invent fps numbers. Measure or omit.

### Minutes 35–50 — Show

**Say:** Live demo: Screenshot the same edge with AA off vs renderer antialias on vs a cheap FXAA-ish blur extra.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** written table.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: written table.; ghosting description from a video still extra.. Homework: Written: choose AA for a product viewer.; screenshots.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: MSAA, TAA, FXAA | Plant the first common mistake. |
| 10–30 | Screenshot the same edge with AA off vs renderer antialias on vs a cheap FXAA-ish blur extra. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Real-Time Rendering/code/` as the after-class check, not as the lecture.

---

## Lab

1. written table.
2. ghosting description from a video still extra.

---

## Homework

1. Written: choose AA for a product viewer.
2. screenshots.

---

## Quiz next meeting (they hear this now)

1. MSAA idea (3)
2. TAA risk (4)
3. FXAA (3)


## Snippet

```js
new THREE.WebGLRenderer({ antialias: true }); // MSAA-ish on forward
```

---

## Extra exercises

See [[Real-Time Rendering/exercises/Week 11]].

---

## Notes you may still need (from the outline)

**1. Why aliasing.** Edges, specular sparkle, thin geometry, alpha test.

**2. Deferred vs MSAA.** MSAA hates deferred. That's a reason for FXAA/TAA.

**3. Alpha.** Alpha-to-coverage name. Hair is hard.

---

## Common mistakes

1. TAA as required homework.
2. supersample 8× on a laptop as the lab.

## If we run long, cut

Alpha

## If we run short, add

ghosting description from a video still extra.
