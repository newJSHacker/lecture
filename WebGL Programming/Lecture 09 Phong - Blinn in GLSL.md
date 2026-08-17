# Lecture 9 — Phong / Blinn in GLSL

**Week 9 of 15** · WebGL Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** Blinn-Phong: H = normalize(L+V); normalize n in FS; gamma once  
**Success check:** they can write the half vector, a shininess slider, and pow(c, 1/2.2) at the end only

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `WebGL Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: a highlight you can explain | Invariant: interpolate then normalize; gamma twice is a bug; PBR is a later course`

## Board at the end (they photograph this)

```
H = normalize(L + V)
spec = pow(max(dot(N, H), 0), shininess)

gamma: pow(c, vec3(1.0/2.2))   once, at the end
normalize(v_n) in FS   (interpolation denormalizes)
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** Same as CG I week 11, now GLSL. Phong reflect vs Blinn half vector — we prefer Blinn in class. Demo 06-phong-cube.html.

**Ask:** Why normalize n in the fragment if the VS already did? Wait. Want: interpolation.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *varyings, gamma*.

**Do not:** Gamma twice.

### Minutes 10–12 — Frame

**Say:** Varyings. Shininess 8–128. Gate spec with ndotl so the back face is dark. Gamma: linear lighting, encode at the end. Not twice. PBR name only — quiz trap.

**Ask:** H vs R — which is Blinn?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Half vector on the board. Same N, L, V spaces.

**Board:** H line + gamma once.

**Say:** Two lights extra is add; energy not conserved — name it.

**Ask:** Where does gamma live — VS, FS start, or FS end?

**They do:** On paper: the H line and the spec pow.

**Do not:** Wrap the first triangle in Three.js. Unfreeze conventions.

### Minutes 35–50 — Show

**Say:** Blinn cube; shininess slider. Plant gamma twice. Plant n not normalized. Demo 06-phong-cube.html.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** gamma toggle. See the midtones. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: gamma toggle; two lights extra. Homework: why normalize n in FS; blinn. Quiz: half vector, gamma where, PBR? (name only).

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Lambert still there | Do not delete diffuse. |
| 10–30 | H + shininess | Plant Phong R if you want the contrast. |
| 30–45 | gamma once | Plant pow on inputs and output. |
| 45–60 | They toggle gamma | Circulate. |

Point them at `WebGL Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. gamma toggle.
2. two lights extra.

---

## Homework

1. Written: why normalize n in FS.
2. Code: blinn.

---

## Quiz next meeting (they hear this now)

None this meeting.


## Snippet

```glsl
vec3 h = normalize(l + v);
```

---

## Extra exercises

See [[WebGL Programming/exercises/Week 09]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. gamma twice.
2. n not normalized.

## If we run long, cut

Image-based lighting. Keep Blinn + gamma once.

## If we run short, add

Second light, additive.
