# Lecture 12 — Profiling

**Week 12 of 15** · Real-Time Rendering  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** GPU vs CPU, budgets  
**Success check:** Use renderer.info / Spector.js name / Chrome GPU.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `Real-Time Rendering/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: GPU vs CPU, budgets | Invariant: a frame is a budget; name the pass`

## Board at the end (they photograph this)

```
draw calls, overdraw, ms
Budget sheet.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** Two clocks. CPU: JS, draw calls.

**Ask:** renderer.info / Spector.js name / Chrome GPU? Wait seven seconds. Take two answers.

**Board:** parked strip. Then draw calls, overdraw, ms.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *GPU vs CPU, budgets*.

**Do not:** 'it's 60 on my machine' with no numbers.

### Minutes 10–12 — Frame

**Say:** Today’s question: GPU vs CPU, budgets. Kernel: GPU vs CPU, budgets. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: 'it's 60 on my machine' with no numbers.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Two clocks. CPU: JS, draw calls.

**Say:** Tools. Spector.js, RenderDoc (desktop), three.js info, timestamp queries name.

**Say:** Student rule. A table with **device, resolution, what changed, ms**.

**Ask:** renderer.info / Spector.js name / Chrome GPU? Wait seven seconds. Take two answers.

**They do:** On paper: overdraw viz extra (additive white).

**Do not:** invent fps numbers. Measure or omit.

### Minutes 35–50 — Show

**Say:** Live demo: Profile a scene: one change (shadow map size or pixel ratio); record two rows.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** overdraw viz extra (additive white).

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: overdraw viz extra (additive white).; cut one pass.. Homework: Written: budget for *your* project device.; measured table.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: GPU vs CPU, budgets | Plant the first common mistake. |
| 10–30 | Profile a scene: one change (shadow map size or pixel ratio); record two rows. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Real-Time Rendering/code/` as the after-class check, not as the lecture.

---

## Lab

1. overdraw viz extra (additive white).
2. cut one pass.

---

## Homework

1. Written: budget for *your* project device.
2. measured table.

---

## Quiz next meeting (they hear this now)

1. CPU vs GPU bound (4)
2. overdraw (3)
3. why measure (3)


## Snippet

```js
console.table(renderer.info.render);
```

---

## Extra exercises

See [[Real-Time Rendering/exercises/Week 12]].

---

## Notes you may still need (from the outline)

**1. Two clocks.** CPU: JS, draw calls. GPU: fill rate, bandwidth, shader cost.

**2. Tools.** Spector.js, RenderDoc (desktop), three.js info, timestamp queries name.

**3. Student rule.** A table with **device, resolution, what changed, ms**. No fantasy.

---

## Common mistakes

1. 'it's 60 on my machine' with no numbers.
2. optimizing textures last when they are 8k.

## If we run long, cut

Student rule

## If we run short, add

cut one pass.
