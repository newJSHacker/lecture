# Lecture 11 — Configurator + AI

**Week 11 of 15** · AI for Interactive Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** AI as salesperson on enums: validate {part, finish}; undo; no freeform shaders  
**Success check:** they can reject invalid JSON and apply a finish only from FINISHES

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `AI for Interactive Graphics/code/02-asset-table.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: constrained generation | Invariant: no secrets in the frontend; cite the model`

## Board at the end (they photograph this)

```
FINISHES = ['oak','steel','matte']
if (!FINISHES.includes(data.finish)) throw

AI proposes     schema validates     user confirms
undo every apply
freeform 'gold-er' writing shaders  =  fail
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** The configurator is structured. AI is a salesperson, not the CAD kernel. Freeform 'make it gold-er' that writes shaders fails. Validate. Confirm. Undo.

**Ask:** If the model returns finish: 'gold-er', what happens? Wait. Want: throw / reject, do not compile a shader.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *constrained generation*.

**Do not:** Freeform 'make it gold-er' writing new shaders.

### Minutes 10–12 — Frame

**Say:** Three finishes. Mock or real via proxy. Invalid JSON handling. Keys still server-side.

**Ask:** Who is allowed to invent a new part?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Enums. The 3D product already has parts.

**Board:** includes check. Confirm. Undo.

**Say:** Parse + validate. Never eval the payload.

**Ask:** Why confirm before apply?

**They do:** On paper: valid vs invalid payload.

**Do not:** Put API keys in client JS. Skip integrity.

### Minutes 35–50 — Show

**Say:** Three finishes; model may only pick among them; apply on confirm. Plant freeform shader. Plant no validate. Undo.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Reject invalid finish. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: invalid JSON; undo. Homework: schema paragraph. Quiz: enums, validate, undo.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | FINISHES enum | Plant freeform. |
| 15–40 | Validate + confirm | Plant no check. |
| 40–55 | Undo | They apply twice. |
| 55–60 | They handle bad JSON | Circulate. |

Point them at `AI for Interactive Graphics/code/02-asset-table.html` as the after-class check, not as the lecture.

---

## Lab

1. invalid JSON handling.
2. undo.

---

## Homework

1. Written: why allowlist.
2. demo.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
if (!FINISHES.includes(data.finish)) throw new Error('invalid');
```

---

## Extra exercises

See [[AI for Interactive Graphics/exercises/Week 11]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. freeform 'make it gold-er' writing new shaders.
2. no validate.

## If we run long, cut

Full CAD. Keep enums + undo.

## If we run short, add

Undo stack of one.
