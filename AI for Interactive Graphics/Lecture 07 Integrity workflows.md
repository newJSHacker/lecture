# Lecture 7 — Integrity workflows

**Week 7 of 15** · AI for Interactive Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** asset table + prompt log; unlabeled gen is an integrity case  
**Success check:** they can fill a table for a mini scene even if every file is handmade

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `AI for Interactive Graphics/code/02-asset-table.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: a lab notebook for assets | Invariant: no secrets in the frontend; cite the model`

## Board at the end (they photograph this)

```
| file | source | license | generated? | prompt/model | human edits |

empty table because 'just a cube'  =  fail
labeled gen + human cleanup        =  OK
exams remain human
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** Good students keep a prompt log like a lab notebook. Unlabeled gen is an integrity case. Labeled gen with cleanup is fine. TAs will spot-check one asset. Demo 02-asset-table.html.

**Ask:** If it was 'just a cube,' do you still have a row? Wait. Want: yes.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *what students must log*.

**Do not:** Empty table because 'it was just a cube'.

### Minutes 10–12 — Frame

**Say:** Peer review of a stripped table. Template in the repo. Same rule as Teaching/12: disclose; explain.

**Ask:** What is the difference between labeled gen and a lie?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Process. The table is the kernel.

**Board:** six columns. Fill one handmade row.

**Say:** Spot-check. Prompts recorded.

**Ask:** Who is the table for — the model or the TA?

**They do:** Fill three rows (handmade allowed).

**Do not:** Put API keys in client JS. Skip integrity.

### Minutes 35–50 — Show

**Say:** Fill an asset table for a mini scene. Plant empty table. Plant missing prompts. Peer swap names stripped.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Three rows. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: peer review; template in repo. Homework: table in README. Quiz: columns, unlabeled = case, cube still has a row. Next: midterm then latency.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Columns | Plant empty table. |
| 15–40 | Fill handmade + gen | Plant unlabeled. |
| 40–55 | Peer review stripped | They mark a miss. |
| 55–60 | Template in repo | Circulate. |

Point them at `AI for Interactive Graphics/code/02-asset-table.html` as the after-class check, not as the lecture.

---

## Lab

1. Peer review of a classmate's table (names stripped).
2. Prompt log template in the repo.

---

## Homework

1. Written: exam vs homework AI policy.
2. Completed asset table.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```
| file | source | license | generated? | prompt/model | human edits |
```

---

## Extra exercises

See [[AI for Interactive Graphics/exercises/Week 07]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. empty table because 'it was just a cube'.
2. prompts not recorded.

## If we run long, cut

TA process lecture. Keep table + log.

## If we run short, add

Prompt log template file.
