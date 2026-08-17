# Lecture 3 — Architecture

**Week 3 of 15** · Capstone Project  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** named modules; labeled oracles; TA runs in three commands; no client secrets  
**Success check:** they can draw DOM / 3D / loaders / optional proxy and paste npm run dev in README

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `Capstone/code/03-budget.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: architecture as a one-pager | Invariant: the problem is users, not a tech list`

## Board at the end (they photograph this)

```
ui/     scene/     assets/     (optional) proxy/

oracles: physics, Raycaster, PMREM, LLM — labeled
npm i && npm run dev
no CDN     no secrets in client
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** Same as theses: modules with names. Rewriting architecture weekly with no diagram fails. Secrets in client fail. How a TA runs it is part of the architecture.

**Ask:** If the LLM is unlabeled, what is the integrity problem? Wait.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *modules, data, APIs*.

**Do not:** Rewriting architecture weekly with no diagram.

### Minutes 10–12 — Frame

**Say:** Folder skeleton. Empty CI optional extra. Serve local. Three commands in README.

**Ask:** What is an oracle here?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Boxes with names. Arrows are data.

**Board:** ui / scene / assets / proxy. Oracles listed.

**Say:** README run line. .env if AI — not in git.

**Ask:** Why three commands, not a wiki?

**They do:** Architecture one-pager sketch.

**Do not:** Start in an engine before the problem statement.

### Minutes 35–50 — Show

**Say:** Architecture in README. Plant weekly rewrite with no diagram. Plant client key. Plant CDN Three.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Folders + run line. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: skeleton; CI extra. Homework: one-pager in README. Quiz: modules, oracles, no client secrets.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Module boxes | Plant no diagram. |
| 15–40 | Oracles labeled | Plant secret in client. |
| 40–55 | README run | Plant CDN. |
| 55–60 | They mkdir | Circulate. |

Point them at `Capstone/code/03-budget.html` as the after-class check, not as the lecture.

---

## Lab

1. folder skeleton.
2. empty CI extra optional.

---

## Homework

1. Diagram + run instructions.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```
npm i && npm run dev
```

---

## Extra exercises

See [[Capstone/exercises/Week 03]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. rewriting architecture weekly with no diagram.
2. secrets in client.

## If we run long, cut

CI theatre. Keep diagram + run line.

## If we run short, add

Empty CI extra optional.
