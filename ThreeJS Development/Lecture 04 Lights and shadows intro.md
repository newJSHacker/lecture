# Lecture 4 — Lights and shadows intro

**Week 4 of 15** · Three.js Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** dir/point/ambient  
**Success check:** Ambient + directional.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `ThreeJS Development/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: dir/point/ambient | Invariant: Three.js is an engine, not the algorithm`

## Board at the end (they photograph this)

```
shadow map size
Light + plane.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** Energy. Too many lights is a later clustered topic.

**Ask:** Ambient + directional? Wait seven seconds. Take two answers.

**Board:** parked strip. Then shadow map size.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *dir/point/ambient*.

**Do not:** 10 point lights as the aesthetic.

### Minutes 10–12 — Frame

**Say:** Today’s question: dir/point/ambient. Kernel: dir/point/ambient. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: 10 point lights as the aesthetic.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Energy. Too many lights is a later clustered topic.

**Say:** Shadows. Shadow mapping course in RTR.

**Say:** Demo. lights demo.

**Ask:** Ambient + directional? Wait seven seconds. Take two answers.

**They do:** On paper: light helper.

**Do not:** treat the inspector as the renderer. Local vendor only.

### Minutes 35–50 — Show

**Say:** Live demo: Lit cube + plane; toggle shadow.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** light helper.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: light helper.; mapSize 512 vs 2048 extra measure.. Homework: Written: acne.; Code: shadows.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: dir/point/ambient | Plant the first common mistake. |
| 10–30 | Lit cube + plane; toggle shadow. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `ThreeJS Development/code/` as the after-class check, not as the lecture.

---

## Lab

1. light helper.
2. mapSize 512 vs 2048 extra measure.

---

## Homework

1. Written: acne.
2. Code: shadows.

---

## Quiz next meeting (they hear this now)

1. castShadow (3)
2. ambient purpose (3)
3. mapSize (4)


## Snippet

```js
dir.castShadow = true; renderer.shadowMap.enabled = true;
```

---

## Extra exercises

See [[ThreeJS Development/exercises/Week 04]].

---

## Notes you may still need (from the outline)

**1. Energy.** Too many lights is a later clustered topic.

**2. Shadows.** Shadow mapping course in RTR. Here: enable and see acne.

**3. Demo.** lights demo.

---

## Common mistakes

1. 10 point lights as the aesthetic.
2. mapSize 8192 on integrated GPU.

## If we run long, cut

Demo

## If we run short, add

mapSize 512 vs 2048 extra measure.
