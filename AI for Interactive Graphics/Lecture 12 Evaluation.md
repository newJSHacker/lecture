# Lecture 12 — Evaluation

**Week 12 of 15** · AI for Interactive Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** rubrics for gen  
**Success check:** A rubric: task success, latency, $, harm, citation.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `AI for Interactive Graphics/code/02-asset-table.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: rubrics for gen | Invariant: no secrets in the frontend; cite the model`

## Board at the end (they photograph this)

```
fidelity, latency, cost, harm
Score table.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** Eval. Graphics papers measure error.

**Ask:** A rubric: task success, latency, $, harm, citation? Wait seven seconds. Take two answers.

**Board:** parked strip. Then fidelity, latency, cost, harm.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *rubrics for gen*.

**Do not:** One lucky screenshot as eval.

### Minutes 10–12 — Frame

**Say:** Today’s question: rubrics for gen. Kernel: rubrics for gen. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: one lucky screenshot as eval.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Eval. Graphics papers measure error.

**Say:** Cost. Tokens / images counted.

**Say:** Harm. Biased labels, unsafe images — a checklist.

**Ask:** A rubric: task success, latency, $, harm, citation? Wait seven seconds. Take two answers.

**They do:** On paper: cost column.

**Do not:** put API keys in client JS. Do not skip integrity.

### Minutes 35–50 — Show

**Say:** Live demo: Score 5 outputs on a table; pick one for the scene.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** cost column.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: cost column.; one harm note.. Homework: Written: rubric filled.; table in repo.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: rubrics for gen | Plant the first common mistake. |
| 10–30 | Score 5 outputs on a table; pick one for the scene. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `AI for Interactive Graphics/code/02-asset-table.html` as the after-class check, not as the lecture.

---

## Lab

1. cost column.
2. one harm note.

---

## Homework

1. Written: rubric filled.
2. table in repo.

---

## Quiz next meeting (they hear this now)

1. why not cool-only (4)
2. cost (3)
3. harm (3)


## Extra exercises

See [[AI for Interactive Graphics/exercises/Week 12]].

---

## Notes you may still need (from the outline)

**1. Eval.** Graphics papers measure error. AI features need **task** measures: did the user finish configuring?

**2. Cost.** Tokens / images counted. Even mock: count calls.

**3. Harm.** Biased labels, unsafe images — a checklist.

---

## Common mistakes

1. one lucky screenshot as eval.
2. hidden costs.

## If we run long, cut

Harm

## If we run short, add

one harm note.
