# Lecture 7 — Integrity workflows

**Week 7 of 15** · AI for Interactive Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** what students must log  
**Success check:** An asset table: source, license, gen?, prompt.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 6 (10 min, paper or LMS).
- Demo: `AI for Interactive Graphics/code/02-asset-table.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 7 | Goal: what students must log | Invariant: no secrets in the frontend; cite the model`

## Board at the end (they photograph this)

```
prompt log; asset table
Asset table.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 6 quiz. Mark one item together. Then:

**Say:** Process. Good students keep a prompt log like a lab notebook.

**Ask:** An asset table: source, license, gen?, prompt? Wait seven seconds. Take two answers.

**Board:** parked strip. Then prompt log; asset table.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *what students must log*.

**Do not:** Empty table because 'it was just a cube'.

### Minutes 10–12 — Frame

**Say:** Today’s question: what students must log. Kernel: what students must log. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: empty table because 'it was just a cube'.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Process. Good students keep a prompt log like a lab notebook.

**Say:** Grading. Unlabeled gen is an integrity case.

**Say:** TAs. Spot-check one asset per project.

**Ask:** An asset table: source, license, gen?, prompt? Wait seven seconds. Take two answers.

**They do:** On paper: Peer review of a classmate's table (names stripped).

**Do not:** put API keys in client JS. Do not skip integrity.

### Minutes 35–50 — Show

**Say:** Live demo: Fill an asset table for a mini scene (even if all handmade — still fill).. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Peer review of a classmate's table (names stripped).

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Peer review of a classmate's table (names stripped).; Prompt log template in the repo.. Homework: Written: exam vs homework AI policy.; Completed asset table.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: what students must log | Plant the first common mistake. |
| 10–30 | Fill an asset table for a mini scene (even if all handmade — still fill). | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. unlabeled gen (4)
2. what a log row contains (3)
3. TA spot-check (3)


## Snippet

```
| file | source | license | generated? | prompt/model | human edits |
```

---

## Extra exercises

See [[AI for Interactive Graphics/exercises/Week 07]].

---

## Notes you may still need (from the outline)

**1. Process.** Good students keep a prompt log like a lab notebook. Bad students paste.

**2. Grading.** Unlabeled gen is an integrity case. Labeled gen with human cleanup is fine.

**3. TAs.** Spot-check one asset per project.

---

## Common mistakes

1. empty table because 'it was just a cube'.
2. prompts not recorded.

## If we run long, cut

TAs

## If we run short, add

Prompt log template in the repo.
