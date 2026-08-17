# Lecture 12 — Browser rendering pipeline

**Week 12 of 15** · Web Technologies  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** DOM → CSSOM → layout → paint → composite; transform vs top as a policy  
**Success check:** they can name the five words and say why animating top is more expensive than transform

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `Web Technologies/code/10-transform.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: name the pipeline, do not guess speed | Invariant: layout is geometry; paint is pixels; composite is layers — do not invent fps`

## Board at the end (they photograph this)

```
DOM  →  CSSOM  →  render tree  →  layout  →  paint  →  composite

transform / opacity   (composite)
top / width           (layout)

measure if you claim speed
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | Optional: a Layers panel screenshot | photo |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** A janky HUD over WebGL is this lecture. We name the pipeline. We do not invent milliseconds.

**Ask:** Does changing transform trigger layout? Wait. Want: usually no.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *DOM CSSOM layout paint composite*.

**Do not:** Animating left/top for everything.

### Minutes 10–12 — Frame

**Say:** Five stages. Reflow vs repaint teaching-level. will-change named as a last resort.

**Ask:** Which is cheaper to animate: top or transform?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Parse HTML → DOM. Parse CSS → CSSOM. Together: render tree.

**Board:** pipeline. Circle layout.

**Say:** DevTools performance is optional; the policy is enough: prefer transform.

**Ask:** What is paint?

**They do:** On paper: the five words in order.

**Do not:** Lecture HTML as a visual design tool. Use a CDN.

### Minutes 35–50 — Show

**Say:** Toggle a class that changes top vs transform. Do not quote fps. Demo 10-transform.html.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Write the pipeline from memory. Then one CSS animation using transform. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: transform animation. Homework: five words. Quiz: order, transform vs top, do not invent fps.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Five words | They copy. |
| 15–40 | top vs transform | No invented timings. |
| 40–55 | Layers name | Screenshot optional. |
| 55–60 | They write the list | Circulate. |

Point them at `Web Technologies/code/10-transform.html` as the after-class check, not as the lecture.

---

## Lab

1. Paint flashing experiment.
2. One forced-layout bug in a starter to fix.

---

## Homework

1. Written: pipeline boxes.
2. Code: CSS transform animation.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```css
.box { transform: translateX(20px); }
```

---

## Extra exercises

See [[Web Technologies/exercises/Week 12]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. Animating left/top for everything.
2. No DevTools.

## If we run long, cut

Compositor thread details. Keep five words + policy.

## If we run short, add

contain: layout name.
