# Lecture 11 — Terrain

**Week 11 of 15** · Shader Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** height = fBm(xz); march the heightfield; fog; LOD step named  
**Success check:** they can set y = fbm(xz) and color a snow line without a DEM download

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 10 (10 min, paper or LMS).
- Demo: `Shader Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 11 | Goal: one sun, fog, height color | Invariant: terrain this week is a function of xz, not a mesh pipeline`

## Board at the end (they photograph this)

```
h = fbm(p.xz * scale)
map:  p.y - h

fog  =  mix(col, fogCol, 1 - exp(-k t))

LOD: step size may grow with t   (name; not required)
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 10 quiz. Mark one item together. Then:

**Say:** The classic IQ hills. DEM downloads are next year's GIS course. Unlimited steps is a hang, not a look. Pause time; debug a still camera.

**Ask:** Where does height live — a texture from NASA, or fBm(xz)? Wait. Want: fBm today.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *heightmap fBm, lod name*.

**Do not:** DEM downloads as the week.

### Minutes 10–12 — Frame

**Say:** One sun, height color, fog. Triplanar is a name, not required. Shadow extra if time — still a named second march.

**Ask:** What is LOD here?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Slice of hills. Camera looks down the +z or along the ground — freeze one.

**Board:** y = fbm(xz). Fog formula.

**Say:** Cap max steps with a uniform. Do not invent fps; if the machine dies, lower octaves.

**Ask:** Normal from height in one idea?

**They do:** On paper: snow line if h > threshold.

**Do not:** Paste a 200-line Shadertoy as the first kernel.

### Minutes 35–50 — Show

**Say:** Fullscreen terrain march; fog. Plant DEM as the week. Snow line extra.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** Snow line extra. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: snow + shadow extra if time. Homework: height vs mesh terrain; GLSL. Quiz: height fBm, normal from height, fog.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | h = fbm(xz) | Plant DEM download. |
| 10–30 | March + fog | Plant unlimited steps. |
| 30–45 | Max-steps uniform | Pause camera. |
| 45–60 | They add snow line | Circulate. |

Point them at `Shader Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. snow line extra.
2. shadow extra if time.

---

## Homework

1. Written: height vs mesh terrain.
2. GLSL.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```glsl
float h = fbm(p.xz * 0.25);
```

---

## Extra exercises

See [[Shader Programming/exercises/Week 11]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. DEM downloads as the week.
2. unlimited steps.

## If we run long, cut

Triplanar textures. Keep height + fog + step cap.

## If we run short, add

LOD as a name on the board.
