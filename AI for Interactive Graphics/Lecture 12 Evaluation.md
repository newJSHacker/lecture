# Lecture 12 — Evaluation

**Week 12 of 15** · AI for Interactive Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** eval table: task success, latency name, call count/$, harm, citation — not one lucky still  
**Success check:** they can score five outputs and pick one for the scene with costs counted

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `AI for Interactive Graphics/code/02-asset-table.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: a scored pick, not a vibe | Invariant: no secrets in the frontend; cite the model`

## Board at the end (they photograph this)

```
task success | latency (measured or blank) | calls/$ | harm | citation

one lucky screenshot  ≠  eval
mock: still count calls
no invented ms     no invented fps
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** Graphics papers measure error. AI features need task measures: did the user finish configuring? Hidden costs fail. One lucky screenshot is not eval. Harm checklist — not a legal memo.

**Ask:** If you did not count calls, what do you write in the $ column? Wait. Want: unknown — not a fake number.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *rubrics for gen*.

**Do not:** One lucky screenshot as eval.

### Minutes 10–12 — Frame

**Say:** Even mocks count calls. Latency: measure or omit. Harm: biased labels, unsafe images — a checklist, not a diagnosis.

**Ask:** What is task success for a configurator?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Rubric. Five columns.

**Board:** score 5. Pick 1. Count calls.

**Say:** Harm note. Citation of model.

**Ask:** Why count mock calls?

**They do:** Empty table; they fill two rows.

**Do not:** Put API keys in client JS. Skip integrity.

### Minutes 35–50 — Show

**Say:** Score 5 outputs; pick one. Plant lucky screenshot as eval. Plant hidden costs. Plant invented ms.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Fill five rows; circle the pick. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: cost column; one harm note. Homework: eval paragraph. Quiz: task success, count calls, no lucky still. Next: thin slice.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Rubric columns | Plant lucky still. |
| 15–40 | Score 5 / pick 1 | Plant hidden $. |
| 40–55 | Harm checklist | They write one note. |
| 55–60 | They count calls | Circulate. |

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

None this meeting.


## Extra exercises

See [[AI for Interactive Graphics/exercises/Week 12]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. one lucky screenshot as eval.
2. hidden costs.

## If we run long, cut

Harm seminar. Keep table + pick.

## If we run short, add

One harm note row.
