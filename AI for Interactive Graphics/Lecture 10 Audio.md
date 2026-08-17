# Lecture 10 — Audio

**Week 10 of 15** · AI for Interactive Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** STT/TTS as names; captions required; push-to-talk; never always-on mic default  
**Success check:** they can push-to-talk a mock transcript into a tool (color or camera) with captions on

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `AI for Interactive Graphics/code/02-asset-table.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: voice as an input, captions as the product | Invariant: no secrets in the frontend; cite the model`

## Board at the end (they photograph this)

```
push-to-talk → STT (mock OK) → tool
TTS optional     captions always
mic indicator
Web Speech API named     vendor STT via proxy
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** Captions are required even if TTS is the fun part. Always-on mic as default fails. TTS without captions fails. XR later: still captions on a panel. No medical dictation product.

**Ask:** If the speaker is muted, can they still use the feature? Wait. Want: yes — captions / HUD.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *STT/TTS names*.

**Do not:** Always-on mic as default.

### Minutes 10–12 — Frame

**Say:** Proxy for vendor STT. Mic indicator. Keys not in the client.

**Ask:** Why push-to-talk?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** a11y first. Captions.

**Board:** PTT → transcript → setColor. Mic indicator.

**Say:** Always-on is a plant.

**Ask:** Where do captions live in XR?

**They do:** PTT flow on paper plus captions.

**Do not:** Put API keys in client JS. Skip integrity.

### Minutes 35–50 — Show

**Say:** PTT → mock transcript → set color or camera beat. Plant always-on. Plant TTS without captions.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Mock transcript applies one tool. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: captions on; mic indicator. Homework: PTT paragraph. Quiz: captions, PTT, no always-on.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Captions required | Plant TTS-only. |
| 15–40 | PTT → tool | Plant always-on mic. |
| 40–55 | Mic indicator | They add it. |
| 55–60 | They apply setColor | Circulate. |

Point them at `AI for Interactive Graphics/code/02-asset-table.html` as the after-class check, not as the lecture.

---

## Lab

1. captions on.
2. mic indicator.

---

## Homework

1. Written: always-on mic policy.
2. demo.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Extra exercises

See [[AI for Interactive Graphics/exercises/Week 10]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. always-on mic as default.
2. TTS without captions.

## If we run long, cut

XR voice spatialization. Keep PTT + captions.

## If we run short, add

Mic indicator.
