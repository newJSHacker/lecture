# Lecture 10 — Story beats

**Week 10 of 15** · Interactive Experience Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** shot list as data: {id, copy, cam}; three beats  
**Success check:** they can run a 3-beat story from JSON without burying copy in JSX

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `Interactive Experience/code/02-two-clocks.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: an experience, not a cube demo | Invariant: 3D and DOM are two clocks`

## Board at the end (they photograph this)

```
[{ id, copy, cam }]     ←  data, not JSX soup

beat 1  hero
beat 2  detail
beat 3  HUD / CTA

one light setup per beat or lerp; budget
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** A cube is a demo. A beat is a shot. Capstone energy: visitors do something in time. Novels in tooltips fail.

**Ask:** If I delete your JSX copy, does the story still exist in data? Wait.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *shot list, camera, light*.

**Do not:** Novel in tooltips.

### Minutes 10–12 — Frame

**Say:** JSON array. Camera per beat. Lights budgeted. Cinematic 4-minute take is a cut. Screenshot a contact sheet.

**Ask:** Why not bury strings only in JSX?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Experience vs demo. Write three beats.

**Board:** JSON row. cam as a triple.

**Say:** One light rig or lerp. Do not add a film lighting course.

**Ask:** What is a beat in one sentence?

**They do:** On paper: three {id, copy, cam} rows.

**Do not:** Fight React state with the frame loop silently.

### Minutes 35–50 — Show

**Say:** Three beats on a product or museum object. Plant copy only in JSX. Move to JSON.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** JSON-driven beat 1→2. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: JSON; contact sheet. Homework: shot list. Quiz: beat, data vs JSX, budgeted lights.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Three beats on paper | Plant a novel. |
| 15–40 | JSON → camera | Plant JSX-only copy. |
| 40–55 | Contact sheet | They screenshot. |
| 55–60 | They add beat 3 | Circulate. |

Point them at `Interactive Experience/code/02-two-clocks.html` as the after-class check, not as the lecture.

---

## Lab

1. JSON driven.
2. screenshot contact sheet.

---

## Homework

1. Written: shot list.
2. app.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```json
[{ "id": "hero", "copy": "…", "cam": [0,1,4] }]
```

---

## Extra exercises

See [[Interactive Experience/exercises/Week 10]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. novel in tooltips.
2. cinematic 4-minute take.

## If we run long, cut

Film lighting. Keep three beats + JSON.

## If we run short, add

Contact sheet of the three cameras.
