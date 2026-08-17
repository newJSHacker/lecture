# Lecture 1 — Scope and ethics

**Week 1 of 15** · AI for Interactive Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** what this course is not  
**Success check:** Define generative vs classical graphics.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `AI for Interactive Graphics/code/01-proxy-mock.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: what this course is not | Invariant: no secrets in the frontend; cite the model`

## Board at the end (they photograph this)

```
human + model + app
Human in the loop.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** IGWT angle. This is **AI for interactive graphics**: APIs, images-as-textures, limits of 3D generation, agents that drive a scene, latency, evaluation — not a ML theory degree and not 'make a startup in 15 weeks'.

**Ask:** generative vs classical graphics? Wait seven seconds. Take two answers.

**Board:** parked strip. Then human + model + app.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *what this course is not*.

**Do not:** Pasting OpenAI keys in Three.js.

### Minutes 8–12 — Frame

**Say:** Today’s question: what this course is not. Kernel: what this course is not. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: pasting OpenAI keys in Three.js.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** IGWT angle. This is **AI for interactive graphics**: APIs, images-as-textures, limits of 3D generation, agents that drive a scene, latency, evaluation — not a ML theory degree and not 'make a startup in 15 weeks'.

**Say:** Integrity. Students may use AI tools as in the handbook.

**Say:** Harm. No CSAM, no non-consensual deepfakes, no medical advice as a product claim.

**Ask:** generative vs classical graphics? Wait seven seconds. Take two answers.

**They do:** On paper: list three allowed / three forbidden uses.

**Do not:** put API keys in client JS. Do not skip integrity.

### Minutes 35–50 — Show

**Say:** Live demo: A 1-page ethics + integrity addendum for *their* future project idea.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** list three allowed / three forbidden uses.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: list three allowed / three forbidden uses.; API key policy.. Homework: Written: authorship policy.; none.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: what this course is not | Plant the first common mistake. |
| 10–30 | A 1-page ethics + integrity addendum for *their* future project idea. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. frontend secrets (4)
2. label gen assets (3)
3. exam policy (3)


## Snippet

```
.env is server-side. Never VITE_SECRET_KEY in a public repo.
```

---

## Extra exercises

See [[AI for Interactive Graphics/exercises/Week 01]].

---

## Notes you may still need (from the outline)

**1. IGWT angle.** This is **AI for interactive graphics**: APIs, images-as-textures, limits of 3D generation, agents that drive a scene, latency, evaluation — not a ML theory degree and not 'make a startup in 15 weeks'.

**2. Integrity.** Students may use AI tools as in the handbook. They must label generated assets. Exams remain human.

**3. Harm.** No CSAM, no non-consensual deepfakes, no medical advice as a product claim.

---

## Common mistakes

1. pasting OpenAI keys in Three.js.
2. unlabeled Midjourney as 'I modeled this'.

## If we run long, cut

Harm

## If we run short, add

API key policy.
