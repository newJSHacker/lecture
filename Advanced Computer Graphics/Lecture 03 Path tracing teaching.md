# Lecture 3 — Path tracing teaching

**Week 3 of 15** · Advanced Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** Monte Carlo paths; cosine-weighted hemisphere; accumulate spp — teaching tracer, not production  
**Success check:** they can accumulate a 2-sphere Lambert scene and say speckle is variance

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 2 (10 min, paper or LMS).
- Demo: `Advanced Computer Graphics/code/02-tracer.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 3 | Goal: a tiny tracer that is theirs | Invariant: local lighting is bounce 0; GI is the rest`

## Board at the end (they photograph this)

```
color += trace(ray);  n++;  display(color/n)

spp ↑  →  slower, cleaner     (measure spp, do not invent fps)
cosine hemisphere     NEE named
spheres + Lambert + one light  =  complete teaching tracer
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 2 quiz. Mark one item together. Then:

**Say:** Average many random paths. One path is not a tracer. Copied GPUPathTracer unread fails. We do not start with a production path tracer. Demo 02-tracer.html.

**Ask:** What is the speckle? Wait. Want: variance, not a bug in the sphere.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *Monte Carlo, cosine sample*.

**Do not:** One path and calling it a tracer.

### Minutes 10–12 — Frame

**Say:** Next event estimation named. Gamma encode display. One more bounce extra. Cornell extra. spp slider they can explain.

**Ask:** Why cosine-weighted for diffuse?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** MC. Mean of paths.

**Board:** accumulate / n. spp.

**Say:** Scope freeze: spheres + Lambert + one area light.

**Ask:** If n=1, what do you see?

**They do:** On paper: ray, bounce, sample light or hemisphere.

**Do not:** Start with a production path tracer.

### Minutes 35–50 — Show

**Say:** 2-sphere Lambert on Canvas; spp slider. Plant one path as done. Plant GPUPathTracer paste. Gamma encode.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Accumulate n samples on one pixel or a tiny buffer. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: gamma; extra bounce. Homework: variance paragraph. Quiz: MC, cosine, why not production tracer.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | One path vs many | Plant n=1 done. |
| 15–40 | Accumulate spp | Plant production tracer. |
| 40–55 | Gamma display | They see the lift. |
| 55–60 | They move spp | Circulate. No invented fps. |

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

None this meeting.


## Snippet

```js
color.add(trace(ray)); n++; display(color.clone().multiplyScalar(1/n));
```

---

## Extra exercises

See [[Advanced Computer Graphics/exercises/Week 03]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. one path and calling it a tracer.
2. copied GPUPathTracer unread.

## If we run long, cut

Full Cornell. Keep spheres + accumulate.

## If we run short, add

One more bounce extra.
