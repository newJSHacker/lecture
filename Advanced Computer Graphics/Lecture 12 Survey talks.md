# Lecture 12 — Survey talks

**Week 12 of 15** · Advanced Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** prepare a 12 min teaching talk: one method, one figure, one limit, bibliography  
**Success check:** they can rehearse 5 min with a claim sentence and a cited figure

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `Advanced Computer Graphics/code/02-tracer.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: they can teach one name | Invariant: local lighting is bounce 0; GI is the rest`

## Board at the end (they photograph this)

```
12 min  +  5 questions   (next meeting)
one method · one figure · one limit · bib

topics: photon mapping, DDGI, ReSTIR names, SSS, NeRF/3DGS as survey
NeRF: name, figure, limit (edit/dynamic) — not a required impl
Wikipedia-on-stage  =  fail
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** Advanced course means they can teach. Next week is the talks. Today is content: structure, topics, what not to implement. Unattributed figures fail. Full NeRF training is skipped.

**Ask:** If you cannot state the limitation, what did you copy? Wait. Want: a demo.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *12 min teaching talk*.

**Do not:** Reading Wikipedia on stage.

### Minutes 10–12 — Frame

**Say:** Photon mapping, DDGI, ReSTIR names, SSS, neural radiance fields as survey. 3DGS: name and limit. Slides or board photos. Bib required.

**Ask:** What is the one sentence of the talk?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Why they teach. Capstone energy.

**Board:** method / figure / limit / bib. Clock.

**Say:** NeRF/3DGS survey only. No required impl.

**Ask:** What must a cited figure include?

**They do:** Talk outline: four bullets + bib key.

**Do not:** Start with a production path tracer.

### Minutes 35–50 — Show

**Say:** 5 min rehearsal in lab; feedback. Plant Wikipedia. Plant unattributed figure. Plant NeRF impl as required.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Write the claim sentence and limitation. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: slides or board photos; bib. Homework: freeze the talk. Quiz: four parts of a talk, NeRF not required. Next: presentations.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Talk spine | Plant Wikipedia. |
| 15–40 | 5 min rehearsal | Plant no limit. |
| 40–55 | Bib + figure credit | Unattributed plant. |
| 55–60 | They freeze the claim | Circulate. |

Point them at `Advanced Computer Graphics/code/02-tracer.html` as the after-class check, not as the lecture.

---

## Lab

1. slides or board photos.
2. bib.

---

## Homework

1. Talk notes due Week 13–14 slot if needed.
2. none.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Extra exercises

See [[Advanced Computer Graphics/exercises/Week 12]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. reading Wikipedia on stage.
2. unattributed figures.

## If we run long, cut

Second topic. Keep one talk spine.

## If we run short, add

Bib entries on the outline.
