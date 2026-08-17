# Lecture 3 — Path tracing teaching

**Week 3 of 15** · Advanced Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** Monte Carlo, cosine sample  
**Success check:** A camera ray, a bounce, a light sample **or** uniform hemisphere.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `Advanced Computer Graphics/code/02-tracer.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: Monte Carlo, cosine sample | Invariant: local lighting is bounce 0; GI is the rest`

## Board at the end (they photograph this)

```
throughput *= brdf; p += n
Paths + average.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** MC. Average many random paths.

**Ask:** A camera ray, a bounce, a light sample **or** uniform hemisphere? Wait seven seconds. Take two answers.

**Board:** parked strip. Then throughput *= brdf; p += n.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *Monte Carlo, cosine sample*.

**Do not:** One path and calling it a tracer.

### Minutes 10–12 — Frame

**Say:** Today’s question: Monte Carlo, cosine sample. Kernel: Monte Carlo, cosine sample. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: one path and calling it a tracer.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** MC. Average many random paths.

**Say:** Sampling. Cosine-weighted hemisphere for diffuse.

**Say:** Scope. Spheres + Lambert + one area light is a complete teaching tracer.

**Ask:** A camera ray, a bounce, a light sample **or** uniform hemisphere? Wait seven seconds. Take two answers.

**They do:** On paper: gamma encode display.

**Do not:** start with a production path tracer.

### Minutes 35–50 — Show

**Say:** Live demo: Accumulate a 2-sphere Lambert scene on Canvas; spp slider.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** gamma encode display.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: gamma encode display.; one more bounce extra.. Homework: Written: why noise.; code.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: Monte Carlo, cosine sample | Plant the first common mistake. |
| 10–30 | Accumulate a 2-sphere Lambert scene on Canvas; spp slider. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Advanced Computer Graphics/code/02-tracer.html` as the after-class check, not as the lecture.

---

## Lab

1. gamma encode display.
2. one more bounce extra.

---

## Homework

1. Written: why noise.
2. code.

---

## Quiz next meeting (they hear this now)

1. spp (3)
2. why random (4)
3. Lambert sample (3)


## Snippet

```js
color.add(trace(ray)); n++; display(color.clone().multiplyScalar(1/n));
```

---

## Extra exercises

See [[Advanced Computer Graphics/exercises/Week 03]].

---

## Notes you may still need (from the outline)

**1. MC.** Average many random paths. Variance is the speckle. More spp → slower, cleaner.

**2. Sampling.** Cosine-weighted hemisphere for diffuse. Next event estimation name.

**3. Scope.** Spheres + Lambert + one area light is a complete teaching tracer. Cornell box extra.

---

## Common mistakes

1. one path and calling it a tracer.
2. copied GPUPathTracer unread.

## If we run long, cut

Scope

## If we run short, add

one more bounce extra.
