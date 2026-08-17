# Lecture 6 — Textures

**Week 6 of 15** · WebGL Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** upload, UV, sampling  
**Success check:** texImage2D.

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `WebGL Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: upload, UV, sampling | Invariant: CPU fills buffers; GPU runs the shader; P*V*M; CCW`

## Board at the end (they photograph this)

```
uv as color debug
UV.
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** Upload. async image onload.

**Ask:** texImage2D? Wait seven seconds. Take two answers.

**Board:** parked strip. Then uv as color debug.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *upload, UV, sampling*.

**Do not:** Sampling before upload done.

### Minutes 10–12 — Frame

**Say:** Today’s question: upload, UV, sampling. Kernel: upload, UV, sampling. We freeze conventions and we do not invent timings.

**Ask:** What would a wrong version of this look like? Want: sampling before upload done.

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Upload. async image onload.

**Say:** Debug. uv as color.

**Say:** Filtering. NEAREST vs LINEAR.

**Ask:** texImage2D? Wait seven seconds. Take two answers.

**They do:** On paper: uv debug.

**Do not:** wrap the first triangle in Three.js. Freeze conventions.

### Minutes 35–50 — Show

**Say:** Live demo: Textured quad then cube.. Zoom 140%. Read errors out loud.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** uv debug.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Photograph the board. Lab: uv debug.; wrap repeat vs clamp.. Homework: Written: flipY.; Code: sample.. Do not end on “any questions?” — end on the lab hook.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Start the kernel: upload, UV, sampling | Plant the first common mistake. |
| 10–30 | Textured quad then cube. | Fix on the board; they copy. |
| 30–45 | Second pass / tests | Do not hide the error. |
| 45–60 | They type; you circulate | Do not sit. |

Point them at `WebGL Programming/code/` as the after-class check, not as the lecture.

---

## Lab

1. uv debug.
2. wrap repeat vs clamp.

---

## Homework

1. Written: flipY.
2. Code: sample.

---

## Quiz next meeting (they hear this now)

1. texImage2D (3)
2. uv debug (4)
3. NEAREST (3)


## Snippet

```glsl
outColor = texture(u_tex, v_uv);
```

---

## Extra exercises

See [[WebGL Programming/exercises/Week 06]].

---

## Notes you may still need (from the outline)

**1. Upload.** async image onload. Premultiply options.

**2. Debug.** uv as color. [[WebGL/08 uv debug]] if present, else shader.

**3. Filtering.** NEAREST vs LINEAR. Mips named.

---

## Common mistakes

1. sampling before upload done.
2. wrong flipY.

## If we run long, cut

Filtering

## If we run short, add

wrap repeat vs clamp.
