# Lecture 9 — Vision models

**Week 9 of 15** · AI for Interactive Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** button-captured 256px snapshot to mock/real vision; never 30 fps of classmates  
**Success check:** they can capture a downscaled canvas still, show a label, and state the privacy note

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `AI for Interactive Graphics/code/02-asset-table.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: one shot, a label, not a webcam firehose | Invariant: no secrets in the frontend; cite the model`

## Board at the end (they photograph this)

```
button → canvas.toBlob jpeg q~0.7 → proxy/mock → HUD label
256px crop
not every frame
not webcam-to-vendor of classmates
throttle
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** Vision is image in, labels out. Webcam 30 fps of the room to a vendor fails ethics and budget. One shot on a button. Privacy note. No medical diagnosis labels as a product.

**Ask:** Why not send every frame? Wait. Want: cost, latency, privacy.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *image in, labels out*.

**Do not:** Webcam to vendor 30fps class demo on classmates.

### Minutes 10–12 — Frame

**Say:** Use: describe a part, QR, a11y captions. Proxy still holds the key. Throttle.

**Ask:** What is the privacy sentence?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Snapshot. Downscale.

**Board:** button, 256px, label. Strike 30 fps class demo.

**Say:** Harm: we do not claim a diagnostic.

**Ask:** When is a mock label enough?

**They do:** Privacy note + throttle on paper.

**Do not:** Put API keys in client JS. Skip integrity.

### Minutes 35–50 — Show

**Say:** Capture 256px; show mock label. Plant 4k PNG. Plant classmate webcam stream. Plant medical label.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** toBlob + mock label on HUD. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: privacy note; throttle. Homework: why not every frame. Quiz: 256px, button, no classmate firehose.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | 256px capture | Plant 4k. |
| 15–40 | Mock label HUD | Plant every-frame. |
| 40–55 | Privacy + no medical claim | Webcam plant. |
| 55–60 | They add throttle | Circulate. |

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

None this meeting.


## Snippet

```js
canvas.toBlob(cb, 'image/jpeg', 0.7);
```

---

## Extra exercises

See [[AI for Interactive Graphics/exercises/Week 09]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. webcam to vendor 30fps class demo on classmates.
2. 4k PNG.

## If we run long, cut

Cost spreadsheets. Keep one-shot + privacy.

## If we run short, add

Throttle on the button.
