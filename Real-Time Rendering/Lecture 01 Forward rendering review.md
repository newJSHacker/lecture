# Lecture 1 — Forward rendering review

**Week 1 of 15** · Real-Time Rendering  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** one pass, lights in FS  
**Success check:** Restate the forward path.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- No quiz (Lecture 1). Course contract lives in the land.
- Demo: `Real-Time Rendering/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 1 | Goal: one pass, lights in FS | Invariant: a frame is a budget; name the pass`

## Board at the end (they photograph this)

```
for each light: add
Forward boxes.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–8 — Hook

**Say:** Where we are. CG I and WebGL already light a cube.

**Ask:** Restate the forward path? Wait seven seconds. Take two answers.

**Board:** parked strip. Then for each light: add.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *one pass, lights in FS*.

**Do not:** 10 lights on day one.

### Minutes 8–12 — Frame

**Say:** Today’s question: one pass, lights in FS. Kernel: one pass, lights in FS. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: 10 lights on day one.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Where we are. CG I and WebGL already light a cube.

**Say:** Forward. Each object, for each light, add.

**Say:** Energy. Lambert + Blinn can exceed 1.

**Ask:** Restate the forward path? Wait seven seconds. Take two answers.

**They do:** On paper: draw call count.

**Do not:** invent fps numbers. Measure or omit.

### Minutes 35–50 — Show

**Say:** Live demo: A WebGL or Three.js cube with two lights; show saturated LDR vs a fake HDR multiply.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** draw call count.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: draw call count.; light loop in shader vs CPU.. Homework: Written: forward vs 'just add another Mesh'.; screenshot clip vs no clip.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: one pass, lights in FS | Plant the first common mistake. |
| 10–30 | A WebGL or Three.js cube with two lights; show saturated LDR vs a fake HDR multiply. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Real-Time Rendering/code/` as the after-class check, not as the lecture.

---

## Lab

1. draw call count.
2. light loop in shader vs CPU.

---

## Homework

1. Written: forward vs 'just add another Mesh'.
2. screenshot clip vs no clip.

---

## Quiz next meeting (they hear this now)

1. forward path (4)
2. why HDR (3)
3. deferred this week? (3)


## Snippet

```glsl
vec3 c = albedo * (nDotL0 + nDotL1);
```

---

## Extra exercises

See [[Real-Time Rendering/exercises/Week 01]].

---

## Notes you may still need (from the outline)

**1. Where we are.** CG I and WebGL already light a cube. This course is **production looks**: PBR, HDR, shadows, AO names, a post stack, and how to **profile**.

**2. Forward.** Each object, for each light, add. Simple. Dies with many lights — clustered/deferred later and in Advanced CG.

**3. Energy.** Lambert + Blinn can exceed 1. HDR buffers store that; tonemap at the end.

---

## Common mistakes

1. 10 lights on day one.
2. tonemap skipped then 'PBR looks grey'.

## If we run long, cut

Energy

## If we run short, add

light loop in shader vs CPU.
