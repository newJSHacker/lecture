# Lecture 5 — Agents that act

**Week 5 of 15** · AI for Interactive Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** tools, loops  
**Success check:** An agent is a loop with **tools** (set color, load glTF, set camera).

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `AI for Interactive Graphics/code/02-asset-table.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: tools, loops | Invariant: no secrets in the frontend; cite the model`

## Board at the end (they photograph this)

```
observe → think → tool → observe
Loop + log.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** Graphics agents. A chatbot that calls `setMetalness(0.8)` is more IGWT than a generic assistant.

**Ask:** An agent is a loop with **tools** (set color, load glTF, set camera)? Wait seven seconds. Take two answers.

**Board:** parked strip. Then observe → think → tool → observe.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *tools, loops*.

**Do not:** Unbounded agent with shell access.

### Minutes 10–12 — Frame

**Say:** Today’s question: tools, loops. Kernel: tools, loops. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: unbounded agent with shell access.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Graphics agents. A chatbot that calls `setMetalness(0.8)` is more IGWT than a generic assistant.

**Say:** ReAct name. Thought + action.

**Say:** Safety. Allowlist tools.

**Ask:** An agent is a loop with **tools** (set color, load glTF, set camera)? Wait seven seconds. Take two answers.

**They do:** On paper: confirm dialog extra.

**Do not:** put API keys in client JS. Do not skip integrity.

### Minutes 35–50 — Show

**Say:** Live demo: A mock LLM (or real) that can call `setColor` / `resetCamera` on a Three.js scene; log actions.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** confirm dialog extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: confirm dialog extra.; max 4 steps.. Homework: Written: allowlist.; demo.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: tools, loops | Plant the first common mistake. |
| 10–30 | A mock LLM (or real) that can call `setColor` / `resetCamera` on a Three.js scene; log actions. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `AI for Interactive Graphics/code/02-asset-table.html` as the after-class check, not as the lecture.

---

## Lab

1. confirm dialog extra.
2. max 4 steps.

---

## Homework

1. Written: allowlist.
2. demo.

---

## Quiz next meeting (they hear this now)

1. tool (3)
2. why bound steps (4)
3. eval (3)


## Snippet

```js
const tools = { setColor(hex){ mesh.material.color.set(hex); } };
```

---

## Extra exercises

See [[AI for Interactive Graphics/exercises/Week 05]].

---

## Notes you may still need (from the outline)

**1. Graphics agents.** A chatbot that calls `setMetalness(0.8)` is more IGWT than a generic assistant.

**2. ReAct name.** Thought + action. Teaching level.

**3. Safety.** Allowlist tools. No `eval`.

---

## Common mistakes

1. unbounded agent with shell access.
2. hidden tool log.

## If we run long, cut

Safety

## If we run short, add

max 4 steps.
