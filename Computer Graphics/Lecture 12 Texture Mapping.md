# Lecture 12 — Texture mapping

**Week 12 of 15** · Computer Graphics I  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** UV interpolant; sampleNearest; albedo * Lambert; affine UV is wrong in perspective (picture)  
**Success check:** a textured cube or floor; UV debug (u,v,0); they can say texture is not lighting

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 11 (10 min, paper or LMS).
- Demo: `Computer Graphics/code/12-zbuffer.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 12 | Goal: UVs are just another interpolant | Invariant: a picture is an array; putPixel lives in pixels`

## Board at the end (they photograph this)

```
UV in [0,1]    pick image origin (PNG top-left vs glTF bottom-left) and freeze
wrap: u − floor(u)     clamp: min(1,max(0,u))

nearest: floor(u*width), floor(v*height)

affine screen UV bows on a perspective quad
correct: interpolate u/z, v/z, 1/z     (picture; extra to implement)

albedo = sample     color = lambert * albedo
mipmaps: name; lab is nearest
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 11 quiz. Mark one item together. Then:

**Say:** A texture is not a reason to skip normals. If it is upside-down, flip v=1−v once on the board — do not randomly swap four vertices. file:// may block image load: procedural checker is a valid lab.

**Ask:** Does texture replace lighting? Wait. Want: no.

**Board:** parked strip. Then a quad with (0,0),(1,0),(1,1),(0,1) labeled.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *UV, `sampleNearest`, textured Lambert*.

**Do not:** Integer UV 0–width mixed with 0–1.

### Minutes 10–12 — Frame

**Say:** Mag: nearest vs bilinear (name; extra). Min: many texels per pixel → aliasing; mipmaps are the word games use. Spec often not multiplied by albedo — policy. Do not invent fps.

**Ask:** Why affine UV fails in perspective?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Same barycentric as color and z.

**Board:** UV square on a mesh. Nearest vs bilinear 2×2. Trapezoid road, affine vs correct.

**Say:** Integer UV 0–width mixed with 0–1 is the classic smear.

**Ask:** Nearest sample formula.

**They do:** On paper: trapezoid road, affine vs correct. Mipmaps in three sentences.

**Do not:** Skip the attempt.

### Minutes 35–50 — Show

**Say:** Load PNG into ImageData or checker. Textured quad facing camera, then UVs on the cube. UV debug RGB=(u,v,0). Demo 15-texture.html. Plant one UV for the whole cube. Plant sampling v from the wrong origin then rotating the PNG.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** sampleNearest(tex,u,v) with clamp. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: textured cube or perspective floor (to see affine bug); UV debug; checker fallback. Homework: clamp vs repeat. Quiz: UV not a position, nearest, affine fail, texture≠lighting.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | UV on a quad | Plant origin confusion; freeze v-flip. |
| 15–40 | sampleNearest | Plant u in 0–width. |
| 40–50 | Perspective floor affine bug | Describe 1/z; extra to code. |
| 50–60 | Albedo * Lambert | Unlit texture is a debug view, not the shader. |

Point them at `Computer Graphics/code/12-zbuffer.html` as the after-class check, not as the lecture.

---

## Lab

1. `sampleNearest(image, u, v, mode)`.
2. Textured cube **or** a floor quad in perspective (to see affine bug).
3. UV debug view.
4. Procedural checker fallback.

---

## Homework

1. Written: affine vs perspective-correct UV, one picture of a trapezoid.
2. Code: clamp vs repeat demo.
3. Written: mipmaps in three sentences.

---

## Quiz next meeting (they hear this now)

1. UV of a vertex — is it a position? (2 pts)
2. Nearest sample formula. (2 pts)
3. Why affine UV fails in perspective. (4 pts)
4. Texture replaces lighting? Yes/no. (2 pts)


## Extra exercises

See [[Computer Graphics/exercises/Week 12]].

---

## Notes you may still need (from the outline)

**1. UV (15 min).** UV in [0,1] typically. `(0,0)` is which corner of the **image**? Canvas/PNG: often top-left. glTF: often bottom-left. **Pick one, write it on the board, stick to it.** If the texture is upside-down, flip v: `v = 1 - v`, do not randomly swap UVs on four vertices.
Wrap: `u = u - floor(u)` (repeat). Clamp: `u = min(1, max(0, u))`.
---

**2. Sampling (20 min).** Nearest:
```
x = floor(u * width)
y = floor(v * height)
```
with wrap/clamp before that.
Bilinear: four taps, lerp. Name; optional lab extra.
Minification: many texels per pixel → aliasing. Mipmaps: prefiltered levels. Required knowledge: the **word** and why games use them. Not required code.
---

**3. Perspective-correct (15 min).** Affine barycentric in **screen space** interpolates UV as if the triangle were flat on the screen. A perspective quad (road, floor) shows the classic bow-tie UV.
Teaching fix: interpolate `u/z`, `v/z`, `1/z`, then `u = (u/z) / (1/z)`. z from clip or view. Extra credit if they implement it; midterm-level: **describe** it.
---

**4. Shading (10 min).** ```
albedo = sample(tex, uv)   // linear if following Week 11
color = lambert * albedo + specular * light   // spec often not multiplied by albedo (policy)
```
A texture is not a reason to skip normals.
---

---

## Common mistakes

1. Integer UV 0–width mixed with 0–1.
2. Sampling with v from the wrong origin; “fixing” by rotating the PNG.
3. Perspective cube with one UV per cube (all faces the same smear).

## If we run long, cut

Mipmap chain. Keep nearest + affine picture.

## If we run short, add

Bilinear four taps as extra.
