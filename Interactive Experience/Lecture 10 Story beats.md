# Lecture 10 — Story beats

**Week 10 of 15** · Interactive Experience Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** shot list, camera, light  
**Success check:** A 3-beat storyboard.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `Interactive Experience/code/02-two-clocks.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: shot list, camera, light | Invariant: 3D and DOM are two clocks`

## Board at the end (they photograph this)

```
beat = camera + copy + mesh
Storyboard.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** Experience vs demo. A cube is a demo.

**Ask:** A 3-beat storyboard? Wait seven seconds. Take two answers.

**Board:** parked strip. Then beat = camera + copy + mesh.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *shot list, camera, light*.

**Do not:** Novel in tooltips.

### Minutes 10–12 — Frame

**Say:** Today’s question: shot list, camera, light. Kernel: shot list, camera, light. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: novel in tooltips.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Experience vs demo. A cube is a demo.

**Say:** Data. JSON array of {t, cam, text}.

**Say:** Lights. One setup per beat or lerp.

**Ask:** A 3-beat storyboard? Wait seven seconds. Take two answers.

**They do:** On paper: JSON driven.

**Do not:** fight React state with the frame loop silently.

### Minutes 35–50 — Show

**Say:** Live demo: Three beats on a product or a tiny museum object.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** JSON driven.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: JSON driven.; screenshot contact sheet.. Homework: Written: shot list.; app.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: shot list, camera, light | Plant the first common mistake. |
| 10–30 | Three beats on a product or a tiny museum object. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. beat (3)
2. why JSON (4)
3. max beats this week (3)


## Snippet

```json
[{ "id": "hero", "copy": "…", "cam": [0,1,4] }]
```

---

## Extra exercises

See [[Interactive Experience/exercises/Week 10]].

---

## Notes you may still need (from the outline)

**1. Experience vs demo.** A cube is a demo. A beat is a **shot**. Capstone energy starts here.

**2. Data.** JSON array of {t, cam, text}. Don't bury copy in JSX only.

**3. Lights.** One setup per beat or lerp. Budget.

---

## Common mistakes

1. novel in tooltips.
2. cinematic 4-minute take.

## If we run long, cut

Lights

## If we run short, add

screenshot contact sheet.
