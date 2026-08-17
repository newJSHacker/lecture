# Lecture 9 — Deferred idea

**Week 9 of 15** · Real-Time Rendering  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** deferred: G-buffer pass (albedo, n, depth, metal-rough) then light pass  
**Success check:** they can name G channels and show three debug panes without deferred-on-one-cube

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `Real-Time Rendering/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: name G then lights | Invariant: many lights, few G writes; a single cube does not earn deferred`

## Board at the end (they photograph this)

```
PASS 1  G-buffer   albedo | n | depth | metal-rough
PASS 2  lights     read G, add

MRT  name
debug panes  are  required
when not:  one cube, forward is enough
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** Why: many lights, objects write G once. Light pass reads G. WebGL MRT is a name. Students can fake G with extra textures. We do not invent how many lights 'hurt' — they count, or they omit.

**Ask:** Does deferred help one cube and one light? Wait. Want: no.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *G-buffer then lights*.

**Do not:** Deferred for a single cube.

### Minutes 10–12 — Frame

**Say:** Packed G. Debug view of n and albedo. Transparency and MSAA are later reasons to stay forward.

**Ask:** What goes in G?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Four panes. Label channels.

**Board:** G then light pass. Circle MRT.

**Say:** Written G layout is the lab if code time is short.

**Ask:** When do you not deferred?

**They do:** On paper: G layout (four rows).

**Do not:** Invent fps numbers. Measure or omit.

### Minutes 35–50 — Show

**Say:** Debug view: albedo | normals | depth. Plant deferred for a single cube. Count lights that would hurt forward — as a count, not an fps.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Count lights / written G layout. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: light count + G layout. Homework: when deferred wins; debug screenshot. Quiz: G channels, MRT, when not.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Name G pass | Plant one-cube deferred. |
| 10–30 | Three debug panes | Plant no debug views. |
| 30–45 | Light pass idea | Read G, add. |
| 45–60 | They write the layout | Circulate. |

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

None this meeting.


## Snippet

```glsl
layout(location=0) out vec4 gAlbedo;
```

---

## Extra exercises

See [[Real-Time Rendering/exercises/Week 09]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. deferred for a single cube.
2. no debug views.

## If we run long, cut

A full MRT engine. Keep named G + debug panes.

## If we run short, add

Transparency as a reason to stay forward.
