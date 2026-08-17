# Lecture 13 — Look-dev a scene

**Week 13 of 15** · Real-Time Rendering  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** look-dev: one asset; dir + IBL + shadow + tonemap named; toggle stack  
**Success check:** they can load a glb or primitives, match a reference crop in words, and say what they configured vs wrote

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 12 (10 min, paper or LMS).
- Demo: `Real-Time Rendering/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 13 | Goal: one asset, full named stack | Invariant: honesty: if PMREM or GGX is Three.js, say so; Unreal stills are not the lab`

## Board at the end (they photograph this)

```
dir light + IBL lookup + shadow compare + tonemap
(+ bloom if earned)

cuts: drop SSAO; keep metal-rough + shadow + tonemap
reference crop  |  yours
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 12 quiz. Mark one item together. Then:

**Say:** Look-dev is a job: reference, then stack, then budget. Cinema from Unreal as 'the lab' fails. Local glb. No CDN HDR.

**Ask:** If IBL is Three.js PMREM, what do you write in the README? Wait. Want: that sentence.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *one asset, full stack*.

**Do not:** Cinema screenshot from Unreal as 'the lab'.

### Minutes 10–12 — Frame

**Say:** Toggle the stack. Device from last week's table. Cuts: drop SSAO.

**Ask:** What do you skip first?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Reference pair. Three differences they will have to name.

**Board:** dir + IBL + shadow + tonemap. Circle honesty.

**Say:** README: configured vs wrote.

**Ask:** Name today's required passes.

**They do:** On paper: skip list.

**Do not:** Invent fps numbers. Measure or omit.

### Minutes 35–50 — Show

**Say:** A still that matches a reference crop (local photo). Plant Unreal as the lab. Toggle stack.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Toggle stack + README bullets. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: toggles + README. Homework: three differences vs reference; repo. Quiz: configured vs wrote, skip list, device. Next: studio.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Name the stack | Plant Unreal screenshot. |
| 10–30 | Load glb/primitives | Plant CDN env. |
| 30–45 | Toggles | Honesty line in README. |
| 45–60 | They write three diffs | Circulate. No invented fps. |

Point them at `Real-Time Rendering/code/` as the after-class check, not as the lecture.

---

## Lab

1. toggle stack.
2. README.

---

## Homework

1. Written: reference vs yours, three differences.
2. repo.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Extra exercises

See [[Real-Time Rendering/exercises/Week 13]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. cinema screenshot from Unreal as 'the lab'.

## If we run long, cut

SSAO on the look. Keep metal-rough + shadow + tonemap.

## If we run short, add

Bloom only if leftover HDR is visible.
