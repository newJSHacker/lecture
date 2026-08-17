# Lecture 3 — Architecture

**Week 3 of 15** · Capstone Project  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** modules, data, APIs  
**Success check:** A diagram: DOM, 3D, loaders, optional proxy.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `Capstone/code/03-budget.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: modules, data, APIs | Invariant: the problem is users, not a tech list`

## Board at the end (they photograph this)

```
boxes: UI | scene | assets | optional AI
Four boxes.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** Architecture. Same as theses: modules with names.

**Ask:** A diagram: DOM, 3D, loaders, optional proxy? Wait seven seconds. Take two answers.

**Board:** parked strip. Then boxes: UI | scene | assets | optional AI.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *modules, data, APIs*.

**Do not:** Rewriting architecture weekly with no diagram.

### Minutes 10–12 — Frame

**Say:** Today’s question: modules, data, APIs. Kernel: modules, data, APIs. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: rewriting architecture weekly with no diagram.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Architecture. Same as theses: modules with names.

**Say:** Oracles. Physics, Raycaster, PMREM, LLM — labeled.

**Say:** Serve. How a TA runs it in 3 commands.

**Ask:** A diagram: DOM, 3D, loaders, optional proxy? Wait seven seconds. Take two answers.

**They do:** On paper: folder skeleton.

**Do not:** start in an engine before the problem statement.

### Minutes 35–50 — Show

**Say:** Live demo: Architecture one-pager in README.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** folder skeleton.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: folder skeleton.; empty CI extra optional.. Homework: Diagram + run instructions.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: modules, data, APIs | Plant the first common mistake. |
| 10–30 | Architecture one-pager in README. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. state where (4)
2. oracle (3)
3. run line (3)


## Snippet

```
npm i && npm run dev
```

---

## Extra exercises

See [[Capstone/exercises/Week 03]].

---

## Notes you may still need (from the outline)

**1. Architecture.** Same as theses: modules with names. `scene/`, `ui/`, `assets/`.

**2. Oracles.** Physics, Raycaster, PMREM, LLM — labeled.

**3. Serve.** How a TA runs it in 3 commands.

---

## Common mistakes

1. rewriting architecture weekly with no diagram.
2. secrets in client.

## If we run long, cut

Serve

## If we run short, add

empty CI extra optional.
