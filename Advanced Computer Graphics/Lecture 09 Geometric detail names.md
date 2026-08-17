# Lecture 9 — Geometric detail names

**Week 9 of 15** · Advanced Computer Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** LOD swap by distance; Nanite is a visibility-buffer idea, not a glTF checkbox  
**Success check:** they can switch three LOD meshes, log tri count, and refuse 'we used Nanite' on a glTF

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `Advanced Computer Graphics/code/02-tracer.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: detail as a budget, named | Invariant: local lighting is bounce 0; GI is the rest`

## Board at the end (they photograph this)

```
lod.addLevel(high, 0)
lod.addLevel(low, 20)

hysteresis named     popping without it
Nanite / vis buffer  cartoon-level name
'we used Nanite' on a glTF  =  fail
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** Blender/RTR budgets meet algorithm names. UE5 Nanite is not a lab port. drei Detailed / Three.js LOD is the lab. Pixel-error sentence extra.

**Ask:** If you loaded one glTF, did you use Nanite? Wait. Want: no.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *LOD, tessellation, Nanite idea*.

**Do not:** 'we used Nanite' on a glTF.

### Minutes 10–12 — Frame

**Say:** Hysteresis extra. Tessellation named. Web: Three.LOD. Do not invent fps when they switch.

**Ask:** What do you log when LOD switches?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Distance swap. Count tris.

**Board:** addLevel. Nanite as idea, not a checkbox.

**Say:** Popping. Hysteresis name.

**Ask:** What is a visibility buffer in one cartoon sentence?

**They do:** Three boxes as LODs; distances labeled.

**Do not:** Start with a production path tracer.

### Minutes 35–50 — Show

**Say:** Three LOD meshes or boxes; switch; log tris. Plant Nanite-on-glTF. Plant pop without talking hysteresis.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Two levels, log count. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: hysteresis extra; pixel-error sentence. Homework: Nanite-is-not-glTF. Quiz: LOD, popping, vis-buffer name.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Three LODs | Plant Nanite checkbox. |
| 15–40 | Log tris | Plant no count. |
| 40–55 | Hysteresis name | Pop plant. |
| 55–60 | They switch distances | Circulate. |

Point them at `Advanced Computer Graphics/code/02-tracer.html` as the after-class check, not as the lecture.

---

## Lab

1. hysteresis extra.
2. pixel error sentence.

---

## Homework

1. Written: Nanite in 8 honest sentences.
2. LOD demo.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
lod.addLevel(high, 0); lod.addLevel(low, 20);
```

---

## Extra exercises

See [[Advanced Computer Graphics/exercises/Week 09]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. 'we used Nanite' on a glTF.
2. popping without hysteresis talk.

## If we run long, cut

Nanite impl. Keep LOD + honesty.

## If we run short, add

Pixel error sentence.
