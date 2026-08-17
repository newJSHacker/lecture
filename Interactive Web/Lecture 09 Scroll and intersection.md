# Lecture 9 — Scroll and intersection

**Week 9 of 15** · Interactive Web Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** IntersectionObserver callback; CSS position:sticky; no raw onscroll without throttle  
**Success check:** they reveal sections with IO and can stick a nav with CSS first

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `Interactive Web/code/09-gsap.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: scroll as a signal, not a per-pixel handler | Invariant: the browser can tell you when a box enters the viewport; scroll listeners are a last resort`

## Board at the end (they photograph this)

```
const io = new IntersectionObserver((ents) => {
  for (const e of ents) e.target.classList.toggle('in', e.isIntersecting);
});
io.observe(el);     io.disconnect() when done

position: sticky; top: 0;     /* CSS first */
onscroll without throttle     =  fail
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** Storytelling sites and later R3F scroll controls are this idea grown up. A scroll handler that writes layout every pixel is jank we will not measure as a fake fps — we just use IO.

**Ask:** Does IntersectionObserver fire on every scroll pixel? Wait. Want: no — it fires on threshold crossings.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *IO, sticky*.

**Do not:** Onscroll without throttle.

### Minutes 10–12 — Frame

**Say:** IO: reveal on enter, lazy class on images extra. Sticky: CSS first, not JS top=. If you must listen to scroll, rAF-throttle. Unobserve when the node goes away.

**Ask:** What is isIntersecting?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Observe, toggle a class, CSS does the fade. Do not set element.style.top in the callback.

**Board:** intersection ratio. sticky nav. disconnect.

**Say:** Lazy images: class that sets src or a data-src swap extra — still IO, not onscroll.

**Ask:** IO vs scroll listener — one sentence for the homework.

**They do:** On paper: lazy class on images extra — observe, swap, unobserve.

**Do not:** Start with Three.js. Canvas 2D is the kernel.

### Minutes 35–50 — Show

**Say:** Sections that fade in via IO. There is no dedicated IO file in code/; do not demo 09-gsap.html as this kernel. Plant onscroll that sets style.top. Plant IO never disconnected.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Lazy class on images extra. Sticky nav. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: lazy class + sticky nav. Homework: IO vs scroll listener; reveal. Quiz: IO callback, sticky, layout in scroll.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | observe + .in class | Plant onscroll. |
| 10–30 | several sections | Threshold 0.1 name. |
| 30–45 | sticky CSS nav | Plant JS stick. |
| 45–60 | They unobserve | Circulate. |

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

None this meeting.


## Snippet

```js
new IntersectionObserver((ents)=>{ /* toggle .in */ }).observe(el);
```

---

## Extra exercises

See [[Interactive Web/exercises/Week 09]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. onscroll without throttle.
2. IO never unobserved.

## If we run long, cut

Scroll-jank deep dive. Keep IO + sticky CSS.

## If we run short, add

sticky nav.
