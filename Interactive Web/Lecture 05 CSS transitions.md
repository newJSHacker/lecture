# Lecture 5 — CSS transitions

**Week 5 of 15** · Interactive Web Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** CSS transition on transform/opacity; hover/focus/class states; prefers-reduced-motion  
**Success check:** they lift a button on hover with transform and can disable the motion when reduced-motion is on

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 4 (10 min, paper or LMS).
- Demo: `Interactive Web/code/05-css.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 5 | Goal: a state change that eases, not a second animation engine | Invariant: transition specific properties; transform/opacity composite; transition:all is a smell`

## Board at the end (they photograph this)

```
.btn { transition: transform 0.2s ease; }
.btn:hover, .btn:focus { transform: translateY(-4px); }

@media (prefers-reduced-motion: reduce) {
  * { transition: none; }
}

width / top  →  layout    transform → composite
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 4 quiz. Mark one item together. Then:

**Say:** Not every motion is rAF. A HUD button that lifts is CSS. Animating width is layout tax. We name composite vs layout; we do not invent fps. Reduced motion is not optional politeness.

**Ask:** Is transition: all 1s a good default? Wait. Want: no — unknown properties, long layout.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *hover, states*.

**Do not:** Transition: all 1s.

### Minutes 10–12 — Frame

**Say:** States: hover, focus, class on. Properties: transform and opacity. Layout-triggering props jank. Inclusive: prefers-reduced-motion. Keyboard focus must lift too, not only hover.

**Ask:** Why not transition width to ‘grow’ a card?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** From / to are CSS states. The browser interpolates. No loop yet — that is keyframes next week.

**Board:** transform lift. reduced-motion query. Circle :focus.

**Say:** Class toggle from JS is the same transition. Do not start GSAP this week.

**Ask:** Does :hover fire on a touch phone? Want: unreliable — class or :focus-visible matters.

**They do:** On paper: reduced-motion media query that kills transitions.

**Do not:** Start with Three.js. Canvas 2D is the kernel.

### Minutes 35–50 — Show

**Say:** A button that lifts on hover; a class toggle. Demo Interactive Web/code/05-css.html shows keyframes + reduced motion — live-code the hover lift beside it. Plant transition:all. Plant width animation.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** reduced-motion query. Don't transition width — use transform. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: reduced-motion + no width transition. Homework: why transform; card. Quiz: which props, reduced motion, transition all smell.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | hover lift transform | Plant top: instead of transform. |
| 10–30 | class toggle + :focus | Plant hover-only, no keyboard. |
| 30–45 | reduced-motion | They toggle the OS/emulation. |
| 45–60 | They kill transition:all | Circulate. No fps. |

Point them at `Interactive Web/code/05-css.html` as the after-class check, not as the lecture.

---

## Lab

1. reduced-motion media query.
2. Don't transition width.

---

## Homework

1. Written: why transform.
2. Code: card.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```css
@media (prefers-reduced-motion: reduce){ * { transition: none !important; } }
```

---

## Extra exercises

See [[Interactive Web/exercises/Week 05]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. transition: all 1s.
2. ignoring reduced motion.

## If we run long, cut

Long motion sermon. Keep transform + reduced-motion.

## If we run short, add

Don't transition width — a side-by-side plant.
