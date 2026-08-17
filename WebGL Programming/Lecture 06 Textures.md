# Lecture 6 — Textures

**Week 6 of 15** · WebGL Programming  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** texImage2D upload, UV, NEAREST vs LINEAR; uv as color debug  
**Success check:** they sample a local image after onload and can debug UV as color

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 5 (10 min, paper or LMS).
- Demo: `WebGL Programming/code/` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 6 | Goal: a textured quad you can debug | Invariant: sampling before upload is black; UV is the map, not the mesh`

## Board at the end (they photograph this)

```
img.onload → texImage2D → generateMipmap (named)
outColor = texture(u_tex, v_uv);

DEBUG: outColor = vec4(v_uv, 0, 1);

NEAREST vs LINEAR     REPEAT vs CLAMP_TO_EDGE
UNPACK_FLIP_Y_WEBGL
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 5 quiz. Mark one item together. Then:

**Say:** A missing texture is an async bug until you prove UV. uv as color is the flashlight. Local file, no CDN. Demos 05-canvas-texture.html and 08-uv-debug.html.

**Ask:** If the quad is black, is it the shader or onload? Wait. Want: often onload — sampling before upload.

**Board:** parked strip. Then today’s picture.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *upload, UV, sampling*.

**Do not:** Sampling before upload done.

### Minutes 10–12 — Frame

**Say:** Upload from Image or canvas. Premultiply named. Filtering: NEAREST vs LINEAR; mips named. flipY surprises PNG vs WebGL.

**Ask:** What does UV (0,0) mean on the image?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Async. Draw a placeholder color until the texture is ready.

**Board:** uv as color. Then texture().

**Say:** wrap REPEAT vs CLAMP. One axis at a time.

**Ask:** Why not fetch a texture from a CDN in this program?

**They do:** On paper: the onload → texImage2D sequence.

**Do not:** Wrap the first triangle in Three.js. Unfreeze conventions.

### Minutes 35–50 — Show

**Say:** Textured quad then cube. Plant sampling before upload. Plant wrong flipY. Demo 05-canvas-texture.html, 08-uv-debug.html.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** uv debug as color, then sample. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: uv debug; wrap repeat vs clamp. Homework: flipY; sample. Quiz: texImage2D, uv debug, NEAREST.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Create texture + bind | Plant TEXTURE0 vs uniform 1. |
| 10–30 | Canvas texture 05 | Plant draw before onload. |
| 30–45 | uv as color 08 | They see stretch. |
| 45–60 | They sample | Circulate. Local only. |

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

None this meeting.


## Snippet

```glsl
outColor = texture(u_tex, v_uv);
```

---

## Extra exercises

See [[WebGL Programming/exercises/Week 06]].

---

## Notes you may still need (from the outline)

_none_

---

## Common mistakes

1. sampling before upload done.
2. wrong flipY.

## If we run long, cut

sRGB framebuffer details. Keep upload + uv debug.

## If we run short, add

wrap REPEAT vs CLAMP on one axis.
