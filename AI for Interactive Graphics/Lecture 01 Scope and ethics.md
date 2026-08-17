# Lecture 1 — Scope and ethics

**Week 1 of 15** · AI for Interactive Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** this is not training GPT; human in the loop; no medical/legal product claims  
**Success check:** they can list three allowed and three forbidden uses and say exams stay human

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `AI for Interactive Graphics/code/01-proxy-mock.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: scope the course before a key exists | Invariant: no secrets in the frontend; cite the model`

## Board at the end (they photograph this)

```
human  +  model  +  graphics app

NOT:  train GPT/CUDA ML
NOT:  medical or legal advice as a product
NOT:  keys in Three.js
NOT:  unlabeled gen as 'I modeled this'

.env is server-side
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** APIs, images-as-textures, limits of 3D-gen, agents that drive a scene, latency, eval — not an ML degree and not a startup in 15 weeks. We do not train GPT. We do not ship medical or legal advice. Integrity from week 1.

**Ask:** Is a Midjourney albedo you did not label 'your model'? Wait. Want: no.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *what this course is not*.

**Do not:** Pasting OpenAI keys in Three.js.

### Minutes 8–12 — Frame

**Say:** Handbook: disclose tools; exams human. Harm: no CSAM, no non-consensual deepfakes, no medical advice as a claim. Keys never in the client — week 2 architecture, named today.

**Ask:** Where does a vendor key live?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Generative vs classical graphics. Both can be in a scene; only one is a dice roll.

**Board:** human + model + app. Strike train-GPT, strike medical/legal claims, strike VITE_SECRET.

**Say:** Asset table starts empty — still a table. Demo 01-proxy-mock.html as the later shape.

**Ask:** What is a forbidden product claim this term?

**They do:** Three allowed / three forbidden uses on paper.

**Do not:** Put API keys in client JS. Skip integrity.

### Minutes 35–50 — Show

**Say:** One-page ethics addendum for their future idea. Plant a key in client JS. Plant a medical chatbot. Strike both.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Allowed/forbidden list + 'no keys in frontend' line. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: list + API key policy. Homework: authorship policy. Quiz: frontend secrets, label gen, exam policy.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Scope: not training GPT | Plant startup pitch. |
| 10–30 | No medical/legal claims | Plant diagnostic app. |
| 30–45 | No VITE_SECRET | Plant key in Three.js. |
| 45–60 | They write three+three | Circulate. |

Point them at `AI for Interactive Graphics/code/01-proxy-mock.html` as the after-class check, not as the lecture.

---

## Lab

1. list three allowed / three forbidden uses.
2. API key policy.

---

## Homework

1. Written: authorship policy.
2. none.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```
.env is server-side. Never VITE_SECRET_KEY in a public repo.
```

---

## Extra exercises

See [[AI for Interactive Graphics/exercises/Week 01]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. pasting OpenAI keys in Three.js.
2. unlabeled Midjourney as 'I modeled this'.

## If we run long, cut

Harm slideshow. Keep scope + key rule.

## If we run short, add

API key policy sentence in the addendum.
