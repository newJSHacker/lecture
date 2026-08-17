# Lecture 6 — RAG idea

**Week 6 of 15** · AI for Interactive Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** retrieve then generate; keyword search over local captions is enough  
**Success check:** they can show the retrieved chunk beside the answer and a miss case

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `AI for Interactive Graphics/code/02-asset-table.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: your captions, not the model's memory | Invariant: no secrets in the frontend; cite the model`

## Board at the end (they photograph this)

```
query → retrieve chunk → generate (or mock)
cite filename

keyword filter is a valid lab
vector DB optional extra

wrong chunk → confident nonsense
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** A museum app should answer from your captions. Embeddings as required infrastructure week 6 fail. Show a miss. Cite the file.

**Ask:** If retrieval misses, should the model still sound sure? Wait. Want: no — show the miss.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *retrieve then generate*.

**Do not:** Embeddings as required infrastructure week 6.

### Minutes 10–12 — Frame

**Say:** Split a few markdown files. Mock the generate step. No frontend secrets if a real model is used.

**Ask:** What do you display besides the answer?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Why RAG. Grounding.

**Board:** retrieve then generate. Cite filename.

**Say:** Failure: wrong chunk. They must see it.

**Ask:** Why is a vector DB not required today?

**They do:** Three local captions; one query that misses.

**Do not:** Put API keys in client JS. Skip integrity.

### Minutes 35–50 — Show

**Say:** Query box over 3 captions; show chunk + mocked answer. Plant no citation. Plant embeddings-required. Show a miss.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Filter + display hit. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: miss case; cite filename. Homework: miss paragraph. Quiz: retrieve-then-generate, cite, miss.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Local captions | Plant vector DB required. |
| 15–40 | Show the chunk | Plant no cite. |
| 40–55 | A miss case | Confident-nonsense plant. |
| 55–60 | They cite the file | Circulate. |

Point them at `AI for Interactive Graphics/code/02-asset-table.html` as the after-class check, not as the lecture.

---

## Lab

1. a miss case.
2. cite filename.

---

## Homework

1. Written: why retrieve.
2. demo.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
const hits = docs.filter(d => d.text.includes(q)).slice(0,3);
```

---

## Extra exercises

See [[AI for Interactive Graphics/exercises/Week 06]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. embeddings as required infrastructure week 6.
2. no citations.

## If we run long, cut

Embedding math. Keep retrieve + miss.

## If we run short, add

Cite filename on the HUD.
