# Lecture 4 — Scroll and camera

**Week 4 of 15** · Interactive Experience Development  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** scroll 0–1 drives one camera or mix; reduced-motion path  
**Success check:** they can map scroll progress to one rotation or dolly and name a non-scroll path

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `Interactive Experience/code/02-two-clocks.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: one beat, not a locomotive theme park | Invariant: 3D and DOM are two clocks`

## Board at the end (they photograph this)

```
scroll  0 ──────── 1
          ↓
   camera / mix / rotation

prefers-reduced-motion  →  same content, no forced scroll
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** Awwwards pages are often scroll → 3D. Students overbuild. One beat: progress 0–1 rotates a product. Capstone energy starts when there is a beat.

**Ask:** If the user cannot scroll, is the story gone? Wait. Want: no — a button or reduced-motion cut.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *scroll controls, storytelling*.

**Do not:** Full locomotive + 3 scenes as week 4.

### Minutes 10–12 — Frame

**Say:** useFrame reads progress, not setState of scroll every pixel. Do not lerp 100 meshes. Fluid images and viewport still apply from Web Tech.

**Ask:** Where does progress live — React state every pixel, or a ref the frame loop reads?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Narrative is a shot, not a second scene graph.

**Board:** 0–1 line. Camera or rotation only.

**Say:** prefers-reduced-motion. Progress bar is honest UX.

**Ask:** Why is locomotive + three scenes a week-4 fail?

**They do:** Sketch stacked copy vs 3D beat; mark the reduced-motion path.

**Do not:** Fight React state with the frame loop silently.

### Minutes 35–50 — Show

**Say:** Scroll 0–1 dollies or spins a primitive. Plant setState on every scroll event. Move progress to a ref.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Bind progress to rotation.y. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: reduced-motion extra; progress bar. Homework: one-beat storyboard. Quiz: 0–1, two clocks, reduced-motion.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Progress 0–1 | Plant full locomotive. |
| 15–40 | Drive one mesh | Plant 100 lerps. |
| 40–55 | Reduced-motion branch | They feel the skip. |
| 55–60 | They add a progress bar | Circulate. |

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

None this meeting.


## Snippet

```jsx
useFrame(() => { mesh.rotation.y = progress.current * Math.PI; });
```

---

## Extra exercises

See [[Interactive Experience/exercises/Week 04]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. full locomotive + 3 scenes as week 4.
2. no alternative to scroll.

## If we run long, cut

Lenis/locomotive. Keep one beat.

## If we run short, add

Progress bar as DOM, not a 3D ticker.
