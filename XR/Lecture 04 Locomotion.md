# Lecture 4 — Locomotion

**Week 4 of 15** · Virtual and Augmented Reality  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** teleport + snap turn as default policy; smooth optional behind a setting  
**Success check:** they can teleport to a floor hit and snap 30°; smooth is not the only path

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 3 (10 min, paper or LMS).
- Demo: `XR/code/02-safety.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 4 | Goal: locomotion that does not assume a stomach | Invariant: comfort and tracking beat extra polygons`

## Board at the end (they photograph this)

```
default:  teleport  +  snap ~30°
optional: smooth     behind a setting
never:    fly by default

raycast floor → on select, move rig to hit
vignette named extra
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 3 quiz. Mark one item together. Then:

**Say:** Vection makes people sick. Teleport + snap is the student policy unless they document otherwise. Smooth-only is a fail. Flying by default is a fail.

**Ask:** Who is the locomotion for — the demo reel or the person in the chair? Wait.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *teleport vs smooth*.

**Do not:** Smooth locomotion only, no option.

### Minutes 10–12 — Frame

**Say:** A plane is enough; navmesh named. Blink fade extra. Inline: click-to-move on the plane. Comfort leftover in week 8.

**Ask:** Why hide smooth behind a setting?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Comfort first. Policy on the board.

**Board:** teleport vs smooth. Snap 30°.

**Say:** Seated still works. No headset lottery for the lab.

**Ask:** What is snap turn for?

**They do:** Sketch floor hit → rig move; mark snap.

**Do not:** Require a headset to pass week 1. Skip the desktop fallback.

### Minutes 35–50 — Show

**Say:** Teleport on select-hit; snap 30°. Plant smooth-only. Plant flying. Inline click-to-move.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Teleport to plane hit (or inline analog). Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: disable smooth or hide it; vignette extra. Homework: policy paragraph. Quiz: default locomotion, snap, no fly.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Policy: teleport+snap | Plant smooth-only. |
| 15–40 | Floor hit → move | Plant fly. |
| 40–55 | Inline click-to-move | Lottery plant. |
| 55–60 | They add snap | Circulate. |

Point them at `XR/code/02-safety.html` as the after-class check, not as the lecture.

---

## Lab

1. disable smooth or hide behind a setting.
2. vignette extra.

---

## Homework

1. Written: why teleport default.
2. demo.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```js
// raycast floor → on select, camera-parent to hit point
```

---

## Extra exercises

See [[XR/exercises/Week 04]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. smooth locomotion only, no option.
2. flying by default.

## If we run long, cut

Blink shader. Keep teleport + policy.

## If we run short, add

Vignette name extra.
