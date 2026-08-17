# Lecture 10 — Fire water smoke

**Week 10 of 15** · Shader Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** domain warp uv; fBm as mask; study then shrink a catalog look  
**Success check:** they ship a ~40-line fire/water/smoke with a citation and one original uniform

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 9 (10 min, paper or LMS).
- Demo: `Shader Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 10 | Goal: one look you can explain | Invariant: unread 400-line paste is a clip; a paused uniform is a program`

## Board at the end (they photograph this)

```
uv' = uv + k * noise(uv)

fire:  warp + fBm mask + palette
water: height fBm → n; fresnel name; sky gradient

cite what you copied
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 9 quiz. Mark one item together. Then:

**Say:** Read the catalog, then shrink. Pasting aurora.glsl as homework fails integrity. Water: normals from height, fresnel as a name, reflection as a gradient sky — not a path tracer.

**Ask:** What do you write in the comment if you started from fire.glsl? Wait. Want: the source.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *domain, lookup, noise*.

**Do not:** Pasting aurora.glsl as the homework.

### Minutes 10–12 — Frame

**Say:** Domain, lookup, noise. One parameter that is yours — a uniform they can pause. No CDN; local glsl.

**Ask:** Why a 40-line fire instead of 400?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Warp the domain. Mask with fBm. Palette is a mix, not a 4K texture from the internet.

**Board:** layers. Circle citation.

**Say:** Ethics: comment the copy. Teaching/12.

**Ask:** Fresnel in one sentence (name-level)?

**They do:** On paper: three functions you will reuse, named.

**Do not:** Paste a 200-line Shadertoy as the first kernel.

### Minutes 35–50 — Show

**Say:** A 40-line fire or water from WebGL/shadertoy; cite. Plant aurora.glsl paste. Pause time; one slider that is theirs.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** One original uniform. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: your parameter + screenshot. Homework: three reused functions; your GLSL. Quiz: domain warp, why cite, fresnel name.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Warp uv | Plant unread 400 lines. |
| 10–30 | 40-line fire/water | Plant no citation. |
| 30–45 | Pause + one slider | Their parameter. |
| 45–60 | They comment the source | Circulate. |

Point them at `Shader Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. one parameter that is yours.
2. screenshot.

---

## Homework

1. Written: three functions you reused.
2. Your GLSL.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

See `WebGL/shadertoy/fire.glsl` — then write a smaller `mainImage`.

---

## Extra exercises

See [[Shader Programming/exercises/Week 10]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. pasting aurora.glsl as the homework.
2. no citation.

## If we run long, cut

Full Navier–Stokes. Keep warp + cite + one uniform.

## If we run short, add

Palette as mix of three colors.
