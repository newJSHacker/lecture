# Lecture 11 — Anti-aliasing names

**Week 11 of 15** · Real-Time Rendering  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** name MSAA (edge samples), FXAA (post), TAA (history) — table, not a homework TAA  
**Success check:** they can fill where / cost-idea / blur and choose AA for a product viewer in words

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `Real-Time Rendering/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: a table you can defend | Invariant: AA is a named technique; 8× supersample on a laptop is not the lab; do not invent fps`

## Board at the end (they photograph this)

```
        where           blur risk
MSAA    geometry edge   low      (hates deferred)
FXAA    post            some
TAA     history         ghosting

alpha-to-coverage  name
TAA not required homework
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Same edge: off vs renderer AA vs cheap blur | photograph |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** Aliasing: edges, specular sparkle, thin geo, alpha test. MSAA hates deferred — that is a reason for FXAA/TAA. We screenshot; we do not invent milliseconds.

**Ask:** Why is TAA not the required homework? Wait. Want: ghosting, history, too much for a week.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *MSAA, TAA, FXAA*.

**Do not:** TAA as required homework.

### Minutes 10–12 — Frame

**Say:** Forward antialias: true is MSAA-ish. FXAA is a post pass. Hair is hard. Alpha-to-coverage named.

**Ask:** What is TAA's main artifact?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Table: where / cost-idea / blur. Cost-idea is 'samples' or 'history', not a fake ms.

**Board:** the table. Circle deferred vs MSAA.

**Say:** Ghosting description from a video still extra.

**Ask:** MSAA in one sentence?

**They do:** On paper: fill the three-row table.

**Do not:** Invent fps numbers. Measure or omit.

### Minutes 35–50 — Show

**Say:** Same edge: AA off vs renderer antialias vs cheap FXAA-ish blur. Plant TAA as required HW. Plant 8× SS as the lab.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Written table. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: table + ghosting extra. Homework: choose AA for a product viewer; screenshots. Quiz: MSAA idea, TAA risk, FXAA.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Why aliasing | They list edges. |
| 10–30 | Three screenshots | Plant invented fps. |
| 30–45 | Deferred vs MSAA | Name the conflict. |
| 45–60 | They fill the table | Circulate. |

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

None this meeting.


## Snippet

```js
new THREE.WebGLRenderer({ antialias: true }); // MSAA-ish on forward
```

---

## Extra exercises

See [[Real-Time Rendering/exercises/Week 11]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. TAA as required homework.
2. supersample 8× on a laptop as the lab.

## If we run long, cut

Implement TAA. Keep names + screenshots.

## If we run short, add

Alpha-to-coverage as a name.
