# Lecture 9 — Scroll and intersection

**Week 9 of 15** · Interactive Web Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** IO, sticky  
**Success check:** IntersectionObserver.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `Interactive Web/code/09-gsap.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: IO, sticky | Invariant: time is rAF; input is events; draw is a function`

## Board at the end (they photograph this)

```
intersection ratio
Reveal.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** IO. Reveal on enter.

**Ask:** IntersectionObserver? Wait seven seconds. Take two answers.

**Board:** parked strip. Then intersection ratio.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *IO, sticky*.

**Do not:** Onscroll without throttle.

### Minutes 10–12 — Frame

**Say:** Today’s question: IO, sticky. Kernel: IO, sticky. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: onscroll without throttle.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** IO. Reveal on enter.

**Say:** Sticky. CSS first.

**Say:** Scroll jank. rAF-throttled listeners if you must.

**Ask:** IntersectionObserver? Wait seven seconds. Take two answers.

**They do:** On paper: Lazy class on images extra.

**Do not:** start with Three.js. Canvas 2D is the kernel.

### Minutes 35–50 — Show

**Say:** Live demo: Sections that fade in via IO.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Lazy class on images extra.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Lazy class on images extra.; sticky nav.. Homework: Written: IO vs scroll listener.; Code: reveal.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: IO, sticky | Plant the first common mistake. |
| 10–30 | Sections that fade in via IO. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Interactive Web/code/09-gsap.html` as the after-class check, not as the lecture.

---

## Lab

1. Lazy class on images extra.
2. sticky nav.

---

## Homework

1. Written: IO vs scroll listener.
2. Code: reveal.

---

## Quiz next meeting (they hear this now)

1. IO callback (4)
2. sticky (3)
3. layout in scroll (3)


## Snippet

```js
new IntersectionObserver((ents)=>{ /* toggle .in */ }).observe(el);
```

---

## Extra exercises

See [[Interactive Web/exercises/Week 09]].

---

## Notes you may still need (from the outline)

**1. IO.** Reveal on enter. Storytelling sites. R3F scroll later.

**2. Sticky.** CSS first.

**3. Scroll jank.** rAF-throttled listeners if you must.

---

## Common mistakes

1. onscroll without throttle.
2. IO never unobserved.

## If we run long, cut

Scroll jank

## If we run short, add

sticky nav.
