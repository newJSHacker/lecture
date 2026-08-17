# Lecture 9 — Environment and IBL taste

**Week 9 of 15** · Three.js Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** envMap, PMREM name  
**Success check:** RGBE/exr name.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `ThreeJS Development/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: envMap, PMREM name | Invariant: Three.js is an engine, not the algorithm`

## Board at the end (they photograph this)

```
scene.environment
Sphere.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** Look. Standard material needs an env to look 'PBR'.

**Ask:** RGBE/exr name? Wait seven seconds. Take two answers.

**Board:** parked strip. Then scene.environment.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *envMap, PMREM name*.

**Do not:** 500MB HDR as the lab.

### Minutes 10–12 — Frame

**Say:** Today’s question: envMap, PMREM name. Kernel: envMap, PMREM name. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: 500MB HDR as the lab.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Look. Standard material needs an env to look 'PBR'.

**Say:** Cost. Big HDR.

**Say:** Demo. env.

**Ask:** RGBE/exr name? Wait seven seconds. Take two answers.

**They do:** On paper: background vs env toggle.

**Do not:** treat the inspector as the renderer. Local vendor only.

### Minutes 35–50 — Show

**Say:** Live demo: A metallic sphere in an env.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** background vs env toggle.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: background vs env toggle.; intensity.. Homework: Written: env vs background.; Code: env.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: envMap, PMREM name | Plant the first common mistake. |
| 10–30 | A metallic sphere in an env. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `ThreeJS Development/code/` as the after-class check, not as the lecture.

---

## Lab

1. background vs env toggle.
2. intensity.

---

## Homework

1. Written: env vs background.
2. Code: env.

---

## Quiz next meeting (they hear this now)

1. environment (4)
2. PMREM (3)
3. budget (3)


## Snippet

```js
scene.environment = envTex;
```

---

## Extra exercises

See [[ThreeJS Development/exercises/Week 09]].

---

## Notes you may still need (from the outline)

**1. Look.** Standard material needs an env to look 'PBR'.

**2. Cost.** Big HDR. Budget.

**3. Demo.** env.

---

## Common mistakes

1. 500MB HDR as the lab.

## If we run long, cut

Demo

## If we run short, add

intensity.
