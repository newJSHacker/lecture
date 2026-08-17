# Lecture 12 — When to stay on WebGL

**Week 12 of 15** · GPU Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** compatibility, tools  
**Success check:** Feature detect.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `GPU Programming/code/01-pong.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: compatibility, tools | Invariant: data lives where the kernel runs`

## Board at the end (they photograph this)

```
table: feature → API
Decision tree.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** Decision. IGWT is web.

**Ask:** Feature detect? Wait seven seconds. Take two answers.

**Board:** parked strip. Then table: feature → API.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *compatibility, tools*.

**Do not:** Rewriting the semester in three APIs.

### Minutes 10–12 — Frame

**Say:** Today’s question: compatibility, tools. Kernel: compatibility, tools. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: rewriting the semester in three APIs.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Decision. IGWT is web.

**Say:** Porting. Shaders rewrite.

**Say:** Project rule. Pick one API for the final unless you explicitly demo both.

**Ask:** Feature detect? Wait seven seconds. Take two answers.

**They do:** On paper: canIuse screenshot.

**Do not:** require CUDA. WebGL/WebGPU in the browser.

### Minutes 35–50 — Show

**Say:** Live demo: A one-page decision for *your* capstone-shaped idea.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** canIuse screenshot.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: canIuse screenshot.; risk list.. Homework: Written: decision memo 1 page.; none.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: compatibility, tools | Plant the first common mistake. |
| 10–30 | A one-page decision for *your* capstone-shaped idea. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `GPU Programming/code/01-pong.html` as the after-class check, not as the lecture.

---

## Lab

1. canIuse screenshot.
2. risk list.

---

## Homework

1. Written: decision memo 1 page.
2. none.

---

## Quiz next meeting (they hear this now)

1. one reason WebGL (3)
2. one reason WebGPU (4)
3. detect (3)


## Extra exercises

See [[GPU Programming/exercises/Week 12]].

---

## Notes you may still need (from the outline)

**1. Decision.** IGWT is web. WebGL2 still ships the catalog. WebGPU is the future compute/graphics API — teach it without stranding labs.

**2. Porting.** Shaders rewrite. Pipelines are more verbose. Gain: compute, less driver magic.

**3. Project rule.** Pick one API for the final unless you explicitly demo both.

---

## Common mistakes

1. rewriting the semester in three APIs.

## If we run long, cut

Project rule

## If we run short, add

risk list.
