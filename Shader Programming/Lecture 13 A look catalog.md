# Lecture 13 — A look catalog

**Week 13 of 15** · Shader Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** four looks: pattern, noise, SDF, march-or-post — each with pause + one slider  
**Success check:** a contact sheet of four controlled stills, not four identical fBm screenshots

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 12 (10 min, paper or LMS).
- Demo: `Shader Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 13 | Goal: four looks you can defend | Invariant: a gallery is uniforms you can pause; a random Shadertoy account is not a portfolio`

## Board at the end (they photograph this)

```
1 pattern     fract / polar
2 noise       value / fBm
3 SDF         2D CSG
4 march|post  sphere or FBO filter

each:  pause time   +  one slider
cite copies
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 12 quiz. Mark one item together. Then:

**Say:** Craft, not a dump of tabs. RTR will put these ideas on meshes with PBR. Today: pause, uniform, debug view. Four identical fBm shots fail.

**Ask:** If time is always running, how do you debug a look? Wait. Want: pause uniform.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *portfolio of 4 looks*.

**Do not:** Four identical fBm screenshots.

### Minutes 10–12 — Frame

**Say:** Gallery page linking four local HTML/GLSL files. Reuse the shadertoy harness. No CDN.

**Ask:** What is baked vs a uniform?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Contact sheet on the board. Four boxes.

**Board:** the four slots. Circle pause.

**Say:** One original twist per look — a slider, not a new 400-line paste.

**Ask:** Why pause?

**They do:** On paper: which four files, and one uniform each.

**Do not:** Paste a 200-line Shadertoy as the first kernel.

### Minutes 35–50 — Show

**Say:** Gallery page, four links, local serve. Plant four identical fBm. Pause time on one look live.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Pause time on their first look. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: pause + twist. Homework: one paragraph per look; repo. Quiz: uniform vs baked, why pause, citation. Next: studio.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Four slots | Plant four identical fBm. |
| 10–30 | Harness links | Plant CDN. |
| 30–45 | Pause + slider | They feel debug. |
| 45–60 | They cite | Circulate. |

Point them at `Shader Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. pause time.
2. one original twist per look.

---

## Homework

1. Written: one paragraph per look.
2. repo.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Extra exercises

See [[Shader Programming/exercises/Week 13]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. four identical fBm screenshots.

## If we run long, cut

A fifth look. Keep four + pause.

## If we run short, add

Raw distance or uv debug key as a preview of studio.
