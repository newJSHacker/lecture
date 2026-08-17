# Lecture 5 — Agents that act

**Week 5 of 15** · AI for Interactive Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** agent = loop + allowlisted tools (setColor, setCamera); no eval; log every action  
**Success check:** they can run a mock agent that calls setColor and show the tool log

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `AI for Interactive Graphics/code/02-asset-table.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: tools on a scene, not a generic chatbot | Invariant: no secrets in the frontend; cite the model`

## Board at the end (they photograph this)

```
thought → action → observe   (ReAct name)
tools = { setColor, resetCamera }   allowlist
max 4 steps
no eval     no shell
log every call
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** A chatbot that calls setMetalness is more IGWT than a generic assistant. Unbounded agents with shell access fail. Hidden tool logs fail. Mock LLM is first-class.

**Ask:** If the model says eval('…'), what does our proxy do? Wait. Want: refuse — not in the allowlist.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *tools, loops*.

**Do not:** Unbounded agent with shell access.

### Minutes 10–12 — Frame

**Say:** Confirm dialog extra. Max 4 steps. Keys still on the server. We are not training the model.

**Ask:** What is a tool in one sentence?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Graphics agents. Tools are functions we wrote.

**Board:** allowlist. Log. Max 4.

**Say:** ReAct as a name. Teaching level.

**Ask:** Why log tools?

**They do:** On paper: two tools and one refused action.

**Do not:** Put API keys in client JS. Skip integrity.

### Minutes 35–50 — Show

**Say:** Mock LLM calls setColor / resetCamera; log actions. Plant eval. Plant hidden log. Plant shell.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** One tool call + log line. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: confirm extra; max 4. Homework: allowlist paragraph. Quiz: tools, no eval, log.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Allowlist | Plant eval. |
| 15–40 | setColor log | Plant hidden log. |
| 40–55 | Max 4 steps | Unbounded plant. |
| 55–60 | They refuse a bad tool | Circulate. |

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

None this meeting.


## Snippet

```js
const tools = { setColor(hex){ mesh.material.color.set(hex); } };
```

---

## Extra exercises

See [[AI for Interactive Graphics/exercises/Week 05]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. unbounded agent with shell access.
2. hidden tool log.

## If we run long, cut

Full ReAct paper. Keep allowlist + log.

## If we run short, add

Max 4 steps on the board.
