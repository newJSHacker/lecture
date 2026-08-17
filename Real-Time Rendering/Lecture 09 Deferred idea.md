# Lecture 9 — Deferred idea

**Week 9 of 15** · Real-Time Rendering  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** G-buffer then lights  
**Success check:** Name G-buffer channels.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `Real-Time Rendering/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: G-buffer then lights | Invariant: a frame is a budget; name the pass`

## Board at the end (they photograph this)

```
albedo n depth → light pass
G panes.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** Why. Many lights, few objects that write G-buffer.

**Ask:** G-buffer channels? Wait seven seconds. Take two answers.

**Board:** parked strip. Then albedo n depth → light pass.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *G-buffer then lights*.

**Do not:** Deferred for a single cube.

### Minutes 10–12 — Frame

**Say:** Today’s question: G-buffer then lights. Kernel: G-buffer then lights. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: deferred for a single cube.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Why. Many lights, few objects that write G-buffer.

**Say:** What goes in G. albedo, metallic-rough, normals, depth.

**Say:** WebGL. MRT names.

**Ask:** G-buffer channels? Wait seven seconds. Take two answers.

**They do:** On paper: count lights that would hurt forward.

**Do not:** invent fps numbers. Measure or omit.

### Minutes 35–50 — Show

**Say:** Live demo: Debug view: albedo | normals | depth as three panes (can be extra FBOs or Three.js).. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** count lights that would hurt forward.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: count lights that would hurt forward.; written G layout.. Homework: Written: when deferred wins.; debug screenshot.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: G-buffer then lights | Plant the first common mistake. |
| 10–30 | Debug view: albedo | normals | depth as three panes (can be extra FBOs or Three.js). | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Real-Time Rendering/code/` as the after-class check, not as the lecture.

---

## Lab

1. count lights that would hurt forward.
2. written G layout.

---

## Homework

1. Written: when deferred wins.
2. debug screenshot.

---

## Quiz next meeting (they hear this now)

1. G channels (4)
2. MRT (3)
3. when not to deferred (3)


## Snippet

```glsl
layout(location=0) out vec4 gAlbedo;
```

---

## Extra exercises

See [[Real-Time Rendering/exercises/Week 09]].

---

## Notes you may still need (from the outline)

**1. Why.** Many lights, few objects that write G-buffer. Light pass reads G and adds.

**2. What goes in G.** albedo, metallic-rough, normals, depth. Packed.

**3. WebGL.** MRT names. Students can draw a **debug view** of n and albedo from a fake G (multiple targets or just extra textures).

---

## Common mistakes

1. deferred for a single cube.
2. no debug views.

## If we run long, cut

WebGL

## If we run short, add

written G layout.
