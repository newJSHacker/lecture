# Lecture 11 — How to read a paper

**Week 11 of 15** · Advanced Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** figures first, claims, threats  
**Success check:** Pick a TOG/I3D/EGSR paper (or a chapter).

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `Advanced Computer Graphics/code/02-tracer.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: figures first, claims, threats | Invariant: local lighting is bounce 0; GI is the rest`

## Board at the end (they photograph this)

```
question → method → figure → limit
Claim / figure / limit.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** Reading. Students will fake-read.

**Ask:** Pick a TOG/I3D/EGSR paper (or a chapter)? Wait seven seconds. Take two answers.

**Board:** parked strip. Then question → method → figure → limit.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *figures first, claims, threats*.

**Do not:** ChatGPT summary as the note.

### Minutes 10–12 — Frame

**Say:** Today’s question: figures first, claims, threats. Kernel: figures first, claims, threats. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: ChatGPT summary as the note.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Reading. Students will fake-read.

**Say:** Math. Skip proofs they cannot yet do; they must still say what is being integrated.

**Say:** Cite. BibTeX in the report later.

**Ask:** Pick a TOG/I3D/EGSR paper (or a chapter)? Wait seven seconds. Take two answers.

**They do:** On paper: draw their figure from memory.

**Do not:** start with a production path tracer.

### Minutes 35–50 — Show

**Say:** Live demo: A 1-page reading note on a **named** paper.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** draw their figure from memory.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: draw their figure from memory.; one question for the authors.. Homework: Reading note due.; none.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: figures first, claims, threats | Plant the first common mistake. |
| 10–30 | A 1-page reading note on a **named** paper. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. claim (4)
2. limit (3)
3. IGWT link (3)


## Extra exercises

See [[Advanced Computer Graphics/exercises/Week 11]].

---

## Notes you may still need (from the outline)

**1. Reading.** Students will fake-read. Force: claim, one algorithm picture, one limitation, one IGWT connection.

**2. Math.** Skip proofs they cannot yet do; they must still say what is being integrated.

**3. Cite.** BibTeX in the report later.

---

## Common mistakes

1. ChatGPT summary as the note.
2. paper they did not open.

## If we run long, cut

Cite

## If we run short, add

one question for the authors.
