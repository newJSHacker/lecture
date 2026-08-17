# Lecture 4 — Scroll and camera

**Week 4 of 15** · Interactive Experience Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** scroll controls, storytelling  
**Success check:** Map scroll to a camera path **or** to a mix value.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `Interactive Experience/code/02-two-clocks.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: scroll controls, storytelling | Invariant: 3D and DOM are two clocks`

## Board at the end (they photograph this)

```
scroll y → camera or mix
Scroll strip.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** Narrative. Awwwards-style pages are often scroll → 3D.

**Ask:** Map scroll to a camera path **or** to a mix value? Wait seven seconds. Take two answers.

**Board:** parked strip. Then scroll y → camera or mix.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *scroll controls, storytelling*.

**Do not:** Full locomotive + 3 scenes as week 4.

### Minutes 10–12 — Frame

**Say:** Today’s question: scroll controls, storytelling. Kernel: scroll controls, storytelling. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: full locomotive + 3 scenes as week 4.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Narrative. Awwwards-style pages are often scroll → 3D.

**Say:** a11y. `prefers-reduced-motion`.

**Say:** Perf. Don't lerp 100 meshes from scroll without instancing.

**Ask:** Map scroll to a camera path **or** to a mix value? Wait seven seconds. Take two answers.

**They do:** On paper: reduced-motion CSS media extra.

**Do not:** fight React state with the frame loop silently.

### Minutes 35–50 — Show

**Say:** Live demo: Scroll 0–1 spins or dollies a glTF/primitive.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** reduced-motion CSS media extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: reduced-motion CSS media extra.; progress bar.. Homework: Written: skip/reduce policy.; demo.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: scroll controls, storytelling | Plant the first common mistake. |
| 10–30 | Scroll 0–1 spins or dollies a glTF/primitive. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Interactive Experience/code/02-two-clocks.html` as the after-class check, not as the lecture.

---

## Lab

1. reduced-motion CSS media extra.
2. progress bar.

---

## Homework

1. Written: skip/reduce policy.
2. demo.

---

## Quiz next meeting (they hear this now)

1. progress 0-1 (3)
2. reduced motion (4)
3. hijack risk (3)


## Snippet

```jsx
useFrame(() => { mesh.rotation.y = progress.current * Math.PI; });
```

---

## Extra exercises

See [[Interactive Experience/exercises/Week 04]].

---

## Notes you may still need (from the outline)

**1. Narrative.** Awwwards-style pages are often scroll → 3D. Students overbuild. One beat: scroll 0–1 rotates a product.

**2. a11y.** `prefers-reduced-motion`. A non-scroll path to the same content.

**3. Perf.** Don't lerp 100 meshes from scroll without instancing.

---

## Common mistakes

1. full locomotive + 3 scenes as week 4.
2. no alternative to scroll.

## If we run long, cut

Perf

## If we run short, add

progress bar.
