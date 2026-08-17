# Lecture 9 — Vision models

**Week 9 of 15** · AI for Interactive Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** image in, labels out  
**Success check:** Send a canvas snapshot (downscaled) to a mock/real vision endpoint.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `AI for Interactive Graphics/code/02-asset-table.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: image in, labels out | Invariant: no secrets in the frontend; cite the model`

## Board at the end (they photograph this)

```
frame → API → HUD
Snapshot button.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** Snapshot. Capture the canvas (or a crop) at 256px.

**Ask:** Send a canvas snapshot (downscaled) to a mock/real vision endpoint? Wait seven seconds. Take two answers.

**Board:** parked strip. Then frame → API → HUD.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *image in, labels out*.

**Do not:** Webcam to vendor 30fps class demo on classmates.

### Minutes 10–12 — Frame

**Say:** Today’s question: image in, labels out. Kernel: image in, labels out. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: webcam to vendor 30fps class demo on classmates.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Snapshot. Capture the canvas (or a crop) at 256px.

**Say:** Use. Describe a part, detect a QR, accessibility captions.

**Say:** Cost/latency. One shot on button, not every frame.

**Ask:** Send a canvas snapshot (downscaled) to a mock/real vision endpoint? Wait seven seconds. Take two answers.

**They do:** On paper: privacy note.

**Do not:** put API keys in client JS. Do not skip integrity.

### Minutes 35–50 — Show

**Say:** Live demo: Button: capture 256px snapshot; show returned label (mock OK).. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** privacy note.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: privacy note.; throttle.. Homework: Written: why not every frame.; demo.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: image in, labels out | Plant the first common mistake. |
| 10–30 | Button: capture 256px snapshot; show returned label (mock OK). | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `AI for Interactive Graphics/code/02-asset-table.html` as the after-class check, not as the lecture.

---

## Lab

1. privacy note.
2. throttle.

---

## Homework

1. Written: why not every frame.
2. demo.

---

## Quiz next meeting (they hear this now)

1. downscale (3)
2. privacy (4)
3. throttle (3)


## Snippet

```js
canvas.toBlob(cb, 'image/jpeg', 0.7);
```

---

## Extra exercises

See [[AI for Interactive Graphics/exercises/Week 09]].

---

## Notes you may still need (from the outline)

**1. Snapshot.** Capture the canvas (or a crop) at 256px. Send to a mock or real vision endpoint. Show the label on the HUD.

**2. Use.** Describe a part, detect a QR, accessibility captions.

**3. Cost/latency.** One shot on button, not every frame.

---

## Common mistakes

1. webcam to vendor 30fps class demo on classmates.
2. 4k PNG.

## If we run long, cut

Cost/latency

## If we run short, add

throttle.
