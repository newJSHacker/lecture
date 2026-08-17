# Lecture 13 — A small sim studio

**Week 13 of 15** · GPU Programming  
**Meeting:** studio (not a content lecture)  
**Kernel:** choose ping-pong FS or WebGPU compute; freeze packing, dt, debug view of state  
**Success check:** they can run a small sim with a packing diagram, stable dt, and no readback every frame

This meeting is **studio**. Session guide: [[Teaching/24 Session Guides]].

---

## Before you enter

- Rubric / report headings on the parked strip.
- Clock visible.
- Demo only if a volunteer asks for a blocked kernel: `GPU Programming/code/01-pong.html`.
- Parked strip: `Lecture 13 | Goal: freeze and review | Invariant: if they cannot draw the memory layout, they are running a sample`

## Board at the end (they photograph this)

```
state  →  update kernel  →  draw

pick:  FBO A/B   or   storage buffer + compute
debug: show state as color
cuts:  drop fluids; keep particles + dt cap
cite:  Stam / IQ / samples
```

## Slides today (cap: 2)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture / studio (75 min)

### Minutes 0–10 — Frame

**Say:** This week you choose. Quality: stable dt, debug view of the state tex or buffer, no readback. Fluids drop if behind. Cite. Feature detect if WebGPU.

**Ask:** If you cannot draw the layout, what are you running? Wait. Want: a sample.

**They do:** write their cut list in one column.

**Do not:** introduce a new library today.

### Minutes 10–65 — Desk review

**Say:** N slider only if safe — a counted N, not a fantasy. Screenshot the debug view. README: packing + API.

**They do:** Draw the packing; screenshot debug. Eight minutes.

**Do not:** sit at the podium. Do not add features for them.

### Minutes 65–75 — Land

**Say:** Lab: N slider if safe + screenshot. Homework: packing + API; repo. No quiz. Next: project studio.

**Do not:** “Any questions?” End on the clock.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Circle one API | Plant both unfinished. |
| 10–30 | Packing on the board | Plant missing debug view. |
| 30–45 | Pause + dt cap | No readback. |
| 45–60 | They screenshot state | Circulate. |

This slot is **more studio**, not a hidden lecture.

---

## Lab

1. N slider if safe.
2. screenshot.

---

## Homework

1. Written: packing + API.
2. repo.

---

## Quiz next meeting

None this week.

## Extra exercises

See [[GPU Programming/exercises/Week 13]].

## Notes from the outline

_none_

## If we run long, cut

A new fluid solver. Keep one architecture + layout.

## If we run short, add

60s rehearsal of the packing diagram.
