# Lecture 13 — A thin slice

**Week 13 of 15** · AI for Interactive Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** one AI-backed graphics feature: texture, copy, tool, or RAG caption — with logs  
**Success check:** they can demo the slice, show the asset table, and name a key-leak threat

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 12 (10 min, paper or LMS).
- Demo: `AI for Interactive Graphics/code/02-asset-table.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 13 | Goal: depth over a chatbot wrapper | Invariant: no secrets in the frontend; cite the model`

## Board at the end (they photograph this)

```
one feature in a scene
proxy/mock     asset table     eval row
README threats: key leak, ToS
cite model, date, prompts
wrapper chatbot with no 3D  =  fail
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 12 quiz. Mark one item together. Then:

**Say:** Capstone energy. Mock the model, keep the architecture. A wrapper around a chatbot with no 3D fails. No medical/legal claims in the slice.

**Ask:** If the vendor is down, does the architecture still demo? Wait. Want: yes — mock.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *one AI feature in a scene*.

**Do not:** Wrapper around a chatbot with no 3D.

### Minutes 10–12 — Frame

**Say:** Working slice + logs. Cuts allowed. Cite. Screenshot.

**Ask:** What is the one feature?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Slice. Depth.

**Board:** feature · logs · table · threats.

**Say:** Chatbot-only is a cut to fail.

**Ask:** What threat goes in the README?

**They do:** One-sentence feature + mock/real.

**Do not:** Put API keys in client JS. Skip integrity.

### Minutes 35–50 — Show

**Say:** Working slice + logs. Plant chatbot wrapper. Plant key in client. Plant medical claim.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Tighten the slice; fill threats. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: README threats; screenshot. Homework: freeze feature. Quiz: one feature, table, no secrets. Next: studio.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Name the feature | Plant chatbot wrapper. |
| 15–40 | Logs + table | Plant client key. |
| 40–55 | Threats README | Medical-claim plant. |
| 55–60 | They screenshot | Circulate. |

Point them at `AI for Interactive Graphics/code/02-asset-table.html` as the after-class check, not as the lecture.

---

## Lab

1. README threats (key leak, ToS).
2. screenshot.

---

## Homework

1. Written: architecture figure.
2. repo.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Extra exercises

See [[AI for Interactive Graphics/exercises/Week 13]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. wrapper around a chatbot with no 3D.

## If we run long, cut

Second feature. Keep one + logs.

## If we run short, add

Screenshot of HUD + scene.
