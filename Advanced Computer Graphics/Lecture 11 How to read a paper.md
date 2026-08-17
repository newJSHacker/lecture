# Lecture 11 — How to read a paper

**Week 11 of 15** · Advanced Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** figures first; claim; limitation; IGWT connection; no ChatGPT summary as the note  
**Success check:** they can write a 1-page note on a named paper they opened, with one figure redrawn

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `Advanced Computer Graphics/code/02-tracer.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: read, do not summarize unseen | Invariant: local lighting is bounce 0; GI is the rest`

## Board at the end (they photograph this)

```
1 claim
1 algorithm picture (drawn)
1 limitation / threat
1 IGWT connection
BibTeX later

AI summary without opening the PDF  =  fail
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** Undergraduates drown in papers. Force: claim, picture, limit, connection. ChatGPT summary as the note fails. A paper they did not open fails. Skip proofs they cannot do; they must still say what is integrated.

**Ask:** If you cannot redraw figure 3, did you read it? Wait. Want: not yet.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *figures first, claims, threats*.

**Do not:** ChatGPT summary as the note.

### Minutes 10–12 — Frame

**Say:** TOG/I3D/EGSR or a PBRT chapter. One question for the authors extra.

**Ask:** What is a threat to validity here?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Figures first.

**Board:** four lines of a reading note.

**Say:** Name the paper on the parked strip.

**Ask:** What may you skip, and what must you still say?

**They do:** Redraw one figure from memory after a short look.

**Do not:** Start with a production path tracer.

### Minutes 35–50 — Show

**Say:** 1-page note on a named paper. Plant AI summary. Plant unread paper. Draw their figure.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Four lines: claim, picture, limit, IGWT. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: draw the figure; one author question. Homework: full page. Quiz: four lines, no fake-read. Next: prepare talks.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Named paper | Plant unread. |
| 15–40 | Four-line note | Plant ChatGPT note. |
| 40–55 | Redraw a figure | They draw. |
| 55–60 | IGWT connection | Circulate. |

Point them at `Advanced Computer Graphics/code/02-tracer.html` as the after-class check, not as the lecture.

---

## Lab

1. draw their figure from memory.
2. one question for the authors.

---

## Homework

1. Reading note due.
2. none.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Extra exercises

See [[Advanced Computer Graphics/exercises/Week 11]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. ChatGPT summary as the note.
2. paper they did not open.

## If we run long, cut

Proof reconstruction. Keep four lines.

## If we run short, add

One question for the authors.
