# Lecture 13 — Look-dev a scene

**Week 13 of 15** · Real-Time Rendering  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** one asset, full stack  
**Success check:** Load a glb or primitives.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 12 (10 min, paper or LMS).
- Demo: `Real-Time Rendering/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 13 | Goal: one asset, full stack | Invariant: a frame is a budget; name the pass`

## Board at the end (they photograph this)

```
dir + IBL + shadow + tonemap
Reference pair.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 12 quiz. Mark one item together. Then:

**Say:** Look-dev. This is a job.

**Ask:** Load a glb or primitives? Wait seven seconds. Take two answers.

**Board:** parked strip. Then dir + IBL + shadow + tonemap.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *one asset, full stack*.

**Do not:** Cinema screenshot from Unreal as 'the lab'.

### Minutes 10–12 — Frame

**Say:** Today’s question: one asset, full stack. Kernel: one asset, full stack. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: cinema screenshot from Unreal as 'the lab'.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Look-dev. This is a job.

**Say:** Honesty. If IBL is Three.js PMREM, say so.

**Say:** Cuts. Drop SSAO.

**Ask:** Load a glb or primitives? Wait seven seconds. Take two answers.

**They do:** On paper: toggle stack.

**Do not:** invent fps numbers. Measure or omit.

### Minutes 35–50 — Show

**Say:** Live demo: A still that matches a reference crop.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** toggle stack.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: toggle stack.; README.. Homework: Written: reference vs yours, three differences.; repo.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: one asset, full stack | Plant the first common mistake. |
| 10–30 | A still that matches a reference crop. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

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

1. what you configured vs wrote (4)
2. skip list (3)
3. device (3)


## Extra exercises

See [[Real-Time Rendering/exercises/Week 13]].

---

## Notes you may still need (from the outline)

**1. Look-dev.** This is a job. Reference, then stack, then budget.

**2. Honesty.** If IBL is Three.js PMREM, say so. If GGX is yours, say so.

**3. Cuts.** Drop SSAO. Keep metal-rough + shadow + tonemap.

---

## Common mistakes

1. cinema screenshot from Unreal as 'the lab'.

## If we run long, cut

Cuts

## If we run short, add

README.
