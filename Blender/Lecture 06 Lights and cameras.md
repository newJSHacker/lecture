# Lecture 6 — Lights and cameras

**Week 6 of 15** · Blender for Real-Time Graphics  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** area vs sun; exposure  
**Success check:** Add Sun and Area lights.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `Blender/code/03-budget.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: area vs sun; exposure | Invariant: units, facing, and budget travel with the asset`

## Board at the end (they photograph this)

```
sun for dir light; area for studio
Key/fill.
Frustum.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** Real-time vs Cycles. This course previews in Eevee or Material Preview so students see what a game-ish engine can do.

**Ask:** Add Sun and Area lights? Wait seven seconds. Take two answers.

**Board:** parked strip. Then sun for dir light; area for studio.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *area vs sun; exposure*.

**Do not:** Lighting with emission meshes only and calling it PBR.

### Minutes 10–12 — Frame

**Say:** Today’s question: area vs sun; exposure. Kernel: area vs sun; exposure. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: Lighting with emission meshes only and calling it PBR.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Real-time vs Cycles. This course previews in Eevee or Material Preview so students see what a game-ish engine can do.

**Say:** Light types. Sun ≈ directional.

**Say:** Camera. 35–50 mm product.

**Ask:** Add Sun and Area lights? Wait seven seconds. Take two answers.

**They do:** On paper: Disable extra lights.

**Do not:** model at unknown scale. Do not skip apply rotation.

### Minutes 35–50 — Show

**Say:** Live demo: Light a crate on a plane; one sun + one fill. Camera frame.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Disable extra lights.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: Disable extra lights.; FOV vs dolly extra.. Homework: Written: sun vs point in Three.js.; Turntable screenshot.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: area vs sun; exposure | Plant the first common mistake. |
| 10–30 | Light a crate on a plane; one sun + one fill. Camera frame. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `Blender/code/03-budget.html` as the after-class check, not as the lecture.

---

## Lab

1. Disable extra lights.
2. FOV vs dolly extra.

---

## Homework

1. Written: sun vs point in Three.js.
2. Turntable screenshot.

---

## Quiz next meeting (they hear this now)

1. sun maps to (3)
2. why one key light (4)
3. fov (3)


## Snippet

```
Light → Sun  |  Camera → 50 mm
```

---

## Extra exercises

See [[Blender/exercises/Week 06]].

---

## Notes you may still need (from the outline)

**1. Real-time vs Cycles.** This course previews in Eevee or Material Preview so students see what a game-ish engine can do. Cycles caustics are not the learning goal.

**2. Light types.** Sun ≈ directional. Point ≈ omni. Spot. Area. Three.js has the same names.

**3. Camera.** 35–50 mm product. 24 mm archviz. Sensor fit. This becomes `PerspectiveCamera.fov`.

---

## Common mistakes

1. Lighting with emission meshes only and calling it PBR.
2. ISO 6400 noise as style.

## If we run long, cut

Camera

## If we run short, add

FOV vs dolly extra.
