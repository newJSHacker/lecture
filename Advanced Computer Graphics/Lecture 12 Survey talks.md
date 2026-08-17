# Lecture 12 — Survey talks

**Week 12 of 15** · Advanced Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** 12 min teaching talk  
**Success check:** Each student (or pair) teaches one GI/volume/deferred topic.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `Advanced Computer Graphics/code/02-tracer.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: 12 min teaching talk | Invariant: local lighting is bounce 0; GI is the rest`

## Board at the end (they photograph this)

```
one method, one figure, one limit
Talk clock.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** Why. Advanced course = they can **teach**.

**Ask:** Each student (or pair) teaches one GI/volume/deferred topic? Wait seven seconds. Take two answers.

**Board:** parked strip. Then one method, one figure, one limit.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *12 min teaching talk*.

**Do not:** Reading Wikipedia on stage.

### Minutes 10–12 — Frame

**Say:** Today’s question: 12 min teaching talk. Kernel: 12 min teaching talk. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: reading Wikipedia on stage.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Why. Advanced course = they can **teach**.

**Say:** Topics. Photon mapping, DDGI, RESTIR names, neural radiance fields **as a survey** (not a full NeRF impl), SSS.

**Say:** NeRF/3DGS. Name, one figure, limit (dynamic scenes, editing).

**Ask:** Each student (or pair) teaches one GI/volume/deferred topic? Wait seven seconds. Take two answers.

**They do:** On paper: slides or board photos.

**Do not:** start with a production path tracer.

### Minutes 35–50 — Show

**Say:** Live demo: Talk rehearsal 5 min in lab; feedback.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** slides or board photos.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: slides or board photos.; bib.. Homework: Talk notes due Week 13–14 slot if needed.; none.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: 12 min teaching talk | Plant the first common mistake. |
| 10–30 | Talk rehearsal 5 min in lab; feedback. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. one figure (3)
2. one limit (4)
3. citation (3)


## Extra exercises

See [[Advanced Computer Graphics/exercises/Week 12]].

---

## Notes you may still need (from the outline)

**1. Why.** Advanced course = they can **teach**. Capstone energy.

**2. Topics.** Photon mapping, DDGI, RESTIR names, neural radiance fields **as a survey** (not a full NeRF impl), SSS.

**3. NeRF/3DGS.** Name, one figure, limit (dynamic scenes, editing). Not a required impl.

---

## Common mistakes

1. reading Wikipedia on stage.
2. unattributed figures.

## If we run long, cut

NeRF/3DGS

## If we run short, add

bib.
