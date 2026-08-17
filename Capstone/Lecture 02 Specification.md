# Lecture 2 — Specification

**Week 2 of 15** · Capstone Project  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** MoSCoW is the grading contract; lab laptop first; explicit skips  
**Success check:** they can show Must/Should/Could/Won't plus five risks on one page

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `Capstone/code/02-readme.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: a spec a TA can mark | Invariant: the problem is users, not a tech list`

## Board at the end (they photograph this)

```
Must / Should / Could / Won't
Devices: lab laptop first     headset extra     phone extra
Skip: no multiplayer, no accounts, … (named)

risk table  5 rows
spec as a novel  =  fail
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** TAs cannot mark a dream. The spec is the contract. Novel-length specs fail. No risks fail. Demo 01-moscow.html.

**Ask:** If Must cannot run on the lab laptop, whose problem is that? Wait. Want: the spec's — cut or change Must.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *must / should / skip*.

**Do not:** Spec as a novel.

### Minutes 10–12 — Frame

**Say:** Wireframe HUD extra. Asset list extra. Headset extra, not Must, unless staff said so.

**Ask:** What belongs in Won't?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** MoSCoW. Must is the slice.

**Board:** four lists. Devices. Skips.

**Say:** Five risks. Likelihood × impact teaching-level.

**Ask:** Why list skips?

**They do:** Must vs Won't for their team, five lines each max.

**Do not:** Start in an engine before the problem statement.

### Minutes 35–50 — Show

**Say:** MoSCoW one page + 5-row risk table. Plant novel spec. Plant no risks. Plant headset as Must without staff.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Must list ≤ 7 bullets. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: HUD wireframe; asset list. Homework: spec page. Quiz: Must, skip, lab-laptop-first.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | MoSCoW | Plant novel. |
| 15–40 | Devices + skips | Plant headset Must. |
| 40–55 | Five risks | Plant no risks. |
| 55–60 | They freeze Must | Circulate. |

Point them at `Capstone/code/02-readme.html` as the after-class check, not as the lecture.

---

## Lab

1. wireframe HUD.
2. asset list.

---

## Homework

1. Spec v1 in repo.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Extra exercises

See [[Capstone/exercises/Week 02]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. spec as a novel.
2. no risks.

## If we run long, cut

Skip-list philosophy. Keep MoSCoW + risks.

## If we run short, add

Asset list extra.
