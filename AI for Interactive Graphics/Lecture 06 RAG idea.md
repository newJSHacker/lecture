# Lecture 6 — RAG idea

**Week 6 of 15** · AI for Interactive Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** retrieve then generate  
**Success check:** RAG: search your notes, then ask the model.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `AI for Interactive Graphics/code/02-asset-table.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: retrieve then generate | Invariant: no secrets in the frontend; cite the model`

## Board at the end (they photograph this)

```
docs → chunks → query → prompt
Retrieve then prompt.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** Why. A museum app that answers from **your** captions, not from the model's memory.

**Ask:** RAG: search your notes, then ask the model? Wait seven seconds. Take two answers.

**Board:** parked strip. Then docs → chunks → query → prompt.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *retrieve then generate*.

**Do not:** Embeddings as required infrastructure week 6.

### Minutes 10–12 — Frame

**Say:** Today’s question: retrieve then generate. Kernel: retrieve then generate. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: embeddings as required infrastructure week 6.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Why. A museum app that answers from **your** captions, not from the model's memory.

**Say:** Toy. Split a few markdown files; keyword search is enough.

**Say:** Failure. Wrong chunk → confident nonsense.

**Ask:** RAG: search your notes, then ask the model? Wait seven seconds. Take two answers.

**They do:** On paper: a miss case.

**Do not:** put API keys in client JS. Do not skip integrity.

### Minutes 35–50 — Show

**Say:** Live demo: Query box over 3 local captions; show retrieved chunk + mocked answer.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** a miss case.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: a miss case.; cite filename.. Homework: Written: why retrieve.; demo.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: retrieve then generate | Plant the first common mistake. |
| 10–30 | Query box over 3 local captions; show retrieved chunk + mocked answer. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. chunk (3)
2. why cite (4)
3. miss (3)


## Snippet

```js
const hits = docs.filter(d => d.text.includes(q)).slice(0,3);
```

---

## Extra exercises

See [[AI for Interactive Graphics/exercises/Week 06]].

---

## Notes you may still need (from the outline)

**1. Why.** A museum app that answers from **your** captions, not from the model's memory.

**2. Toy.** Split a few markdown files; keyword search is enough. Vector DB optional extra.

**3. Failure.** Wrong chunk → confident nonsense. Show a miss.

---

## Common mistakes

1. embeddings as required infrastructure week 6.
2. no citations.

## If we run long, cut

Failure

## If we run short, add

cite filename.
