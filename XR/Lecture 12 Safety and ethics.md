# Lecture 12 — Safety and ethics

**Week 12 of 15** · Virtual and Augmented Reality  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** guardian, seated option, no jumpscares as required, no secret recording  
**Success check:** they can ship a safety README: space, seated, data, epilepsy note

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `XR/code/02-safety.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: a lab that does not hurt people | Invariant: comfort and tracking beat extra polygons`

## Board at the end (they photograph this)

```
clear the space     sitting demos OK
no required jumpscares
no recording classmates in AR without consent
epilepsy note     (no 3 Hz strobe)

we do not give medical advice
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** Real rooms have tables. Forced standing-only as an exam is a fail. Secret recording is a fail. We name epilepsy risk; we do not practice medicine. Demo XR/code/02-safety.html.

**Ask:** If a student is seated, is the experience allowed to exist? Wait. Want: yes.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *boundaries, harassment, medical*.

**Do not:** Forced standing-only exam.

### Minutes 10–12 — Frame

**Say:** Single-user ethics still: AR cameras catch faces. Multiplayer moderation named if they ever add it — not this week. Course: no horror jumpscares as required content.

**Ask:** What goes in the safety README?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Boundaries. Guardian / play space.

**Board:** seated · consent · epilepsy note · no medical claims.

**Say:** Harassment: if social ever, moderation. Today: do not trap, do not record silently.

**Ask:** Why is a jumpscare the wrong required content?

**They do:** Draft the safety README headings.

**Do not:** Require a headset to pass week 1. Skip the desktop fallback.

### Minutes 35–50 — Show

**Say:** Safety README: space, seated, data. Plant standing-only exam. Plant secret recording. Plant a medical claim — strike it.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Write the README section. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: epilepsy note; no recording without consent. Homework: safety page. Quiz: seated, consent, no medical advice. Next: one verb.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Play space | Plant standing-only. |
| 15–40 | README: seated + data | Plant secret recording. |
| 40–55 | No medical claims | Strike the sentence. |
| 55–60 | They add epilepsy note | Circulate. |

Point them at `XR/code/02-safety.html` as the after-class check, not as the lecture.

---

## Lab

1. epilepsy note.
2. no recording classmates in AR without consent.

---

## Homework

1. Written: 1 page safety.
2. none.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Extra exercises

See [[XR/exercises/Week 12]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. forced standing-only exam.
2. secret recording.

## If we run long, cut

Policy lecture. Keep README + seated.

## If we run short, add

Consent line for AR camera.
