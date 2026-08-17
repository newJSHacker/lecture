# Lecture 12 — Profiling

**Week 12 of 15** · Real-Time Rendering  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** CPU vs GPU clocks; table: device, resolution, what changed, ms — measure or omit  
**Success check:** they can record two rows after one change and never say 'it's 60' without numbers

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `Real-Time Rendering/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: two rows on a named device | Invariant: invented frame rates are a grading zero; a budget is a measured table`

## Board at the end (they photograph this)

```
CPU: JS, draw calls
GPU: fill, bandwidth, shader

table:
  device | res | change | ms or info.render

Spector.js / renderer.info / Chrome GPU  names
overdraw viz: additive white extra
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** Two clocks. Student rule: device, resolution, what changed, ms. Spector.js, RenderDoc, three.js info, timestamp queries — names. 'It's 60 on my machine' with no numbers fails.

**Ask:** If you did not measure, what do you write? Wait. Want: omit.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *GPU vs CPU, budgets*.

**Do not:** 'it's 60 on my machine' with no numbers.

### Minutes 10–12 — Frame

**Say:** One change: shadow map size or pixel ratio. Two rows. Overdraw viz extra. Cut one pass extra. Do not optimize 8k textures last if they are the problem — still measure.

**Ask:** CPU bound vs GPU bound in one idea?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Empty table on the board. Fill it live from this machine.

**Board:** the columns. Circle omit.

**Say:** console.table(renderer.info.render) as a snippet, not a fps fantasy.

**Ask:** What four columns?

**They do:** On paper: one hypothesized bottleneck — then they must measure or strike it.

**Do not:** Invent fps numbers. Measure or omit.

### Minutes 35–50 — Show

**Say:** Profile: one change; two rows on the named device. Plant 'it's 60'. No CDN tools that require a login wall — Spector as optional local.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Overdraw viz extra, or cut one pass. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: overdraw or cut pass. Homework: budget for *your* project device; measured table. Quiz: CPU vs GPU bound, overdraw, why measure.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Two clocks | Plant '60 fps'. |
| 10–30 | One change, two rows | Fill device + res. |
| 30–45 | info.render | Read the numbers out loud. |
| 45–60 | They cut one pass | Circulate. Omit if unmeasured. |

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

None this meeting.


## Snippet

```js
console.table(renderer.info.render);
```

---

## Extra exercises

See [[Real-Time Rendering/exercises/Week 12]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. 'it's 60 on my machine' with no numbers.
2. optimizing textures last when they are 8k.

## If we run long, cut

RenderDoc deep dive. Keep the table + one change.

## If we run short, add

Timestamp query as a name.
