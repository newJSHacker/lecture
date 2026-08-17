# Lecture 2 — Color, pixels, and the framebuffer

**Week 2 of 15** · Computer Graphics I  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** over: out_rgb = src*src_a + dst*(1-src_a); index (y*width+x)*4; sRGB named not solved  
**Success check:** they can write over in 0–1 and the byte index, and say byte 128 is not half the light

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 1 (10 min, paper or LMS).
- Demo: `Computer Graphics/code/02-checker.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 2 | Goal: stop treating 8-bit as linear light; composite two squares | Invariant: a picture is an array; putPixel lives in pixels`

## Board at the end (they photograph this)

```
index = (y * width + x) * 4     RGBA uint8

over (straight, 0–1):
  out_rgb = src_rgb * src_a + dst_rgb * (1 - src_a)
  out_a   = src_a + dst_a * (1 - src_a)

Weeks 2–10: store 8-bit as-is
Weeks 11–12: linear in, pow(c, 1/2.2) out

letterbox  ≠  stretch
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | CSS-stretched circle becoming an ellipse | photograph |
| 2 | 50% gray 128 vs a linear mid | photograph |

---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 1 quiz. Mark one item together. Then:

**Say:** Last week a pixel. Today the pixel has alpha and a lie: averaging 8-bit sRGB is not averaging light. We name the lie. We do not invent a color-science course.

**Ask:** Is byte 128 half as much light as 255? Wait. Want: no.

**Board:** parked strip. Then two overlapping squares, straight alpha vs premultiplied.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *alpha over; sRGB vs linear as a **named** problem*.

**Do not:** Blending in uint8 without converting to 0–1.

### Minutes 10–12 — Frame

**Say:** Pixel is a sample. Resolution is sample count; aspect is framebuffer width/height. ImageData is RGBA, unpadded. Premultiplied: name it; lab is straight over. Coverage vs transparency: name; no MSAA. Policy: weeks 2–10 as-is; 11–12 linear then gamma. Never ‘fix’ lighting with shininess.

**Ask:** What does width in the index formula mean — CSS pixels or canvas.width?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Clear color is visible gray, never (0,0,0) while debugging a black cube later.

**Board:** two overlapping squares; over in 0–1. They compute white 0.5 over black on paper.

**Say:** Letterbox vs stretch. Match backing store to CSS * dPR (cap 2) or letterbox. That helper returns in Week 9 as the viewport.

**Ask:** Write over for rgb, ignore output alpha. Work in 0–1.

**They do:** On paper: index of pixel (2,1) in width-10. Then 16:9 in a 4:3 window — stretch or letterbox?

**Do not:** Skip the attempt.

### Minutes 35–50 — Show

**Say:** Two translucent rectangles, alpha slider. Side-by-side 128-gray vs labeled ‘not linear 0.5.’ Demo 03-alpha-over.html. Plant blending in uint8. Plant getContext alpha:false then debugging alpha.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** overPixel on two boxes. Eight minutes. Convert to 0–1 first.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: overPixel; eight boxes alpha 1/8…; CSS-stretch checkbox with a caption. Homework: over tests (opaque, invisible, 50% red on black); sRGB paragraph; letterbox. Quiz: index, over, CSS stretch, 128 vs light.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–10 | Index formula + visible clear | Plant clear alpha 0; page shows through. |
| 10–30 | over two squares | Plant uint8 blend without /255. |
| 30–45 | 128 vs linear | Do not derive the 2.4 piecewise sRGB. |
| 45–60 | Letterbox helper sketch | Plant stretch as the default. |

Point them at `Computer Graphics/code/02-checker.html` as the after-class check, not as the lecture.

---

## Lab

1. `overPixel(img, x, y, rgba)`.
2. Draw 8 translucent circles (or boxes) in a row with alpha 1/8, 2/8, …
3. A “wrong CSS stretch” checkbox that sets CSS size ≠ backing store, and a caption.

---

## Homework

1. Implement `over` with tests: opaque, invisible, 50% red on black.
2. Written: one paragraph on sRGB vs linear. No need for the full 2.4 gamma formula; `pow(c, 2.2)` is enough.
3. Written: a 16:9 framebuffer in a 4:3 window. Do you stretch or letterbox? Why?

---

## Quiz next meeting (they hear this now)

1. `ImageData` index of pixel (2, 1) in a width-10 image? (2 pts)
2. Write `over` for rgb assuming a in [0,1], ignore output alpha. (4 pts)
3. Why does a CSS-stretched canvas distort a circle? (2 pts)
4. Is byte 128 half as much light as 255? Yes/no. (2 pts)


## Extra exercises

See [[Computer Graphics/exercises/Week 02]].

---

## Notes you may still need (from the outline)

**1. Pixels and samples (15 min).** A pixel in this course is a **sample of color** at a grid location. Treating it as a little square is fine for raster rules; it is not a physical CRT phosphor.
**Resolution:** number of samples.  
**Density:** samples per inch (mention, do not grade).  
**Aspect:** `width / height` of the **framebuffer**, not of the window unless they match.
If the canvas is stretched with CSS, circles become ellipses. Fix: match backing store to CSS * devicePixelRatio (cap at 2), or letterbox.
---

**2. Color and alpha (20 min).** `ImageData`: four uint8s, **RGBA**, unpadded rows.
Alpha 255 = opaque. Alpha 0 = invisible. This week we blend.
**Over** (straight, teaching):
```
out_rgb = src_rgb * src_a + dst_rgb * (1 - src_a)
out_a   = src_a + dst_a * (1 - src_a)
```
Work in 0–1, then convert to bytes. Premultiplied alpha is what GPUs often store; mention it; implement straight over in the lab.
Coverage vs transparency: a rasterized edge is a form of coverage. We will not do MSAA this term. A 50% alpha edge is a cheap fake.
---

**3. sRGB vs linear (15 min).** Displays apply a curve. PNG and Canvas are typically **sRGB**. Light adds in **linear** intensity.
Demo they must see: blend black and white 50/50 in byte space → 128. That is not perceptually halfway, and it is not physically halfway.
Course policy:
- Weeks 2–10: store 8-bit as-is; do not pretend it is physically correct.
- Weeks 11–12: convert to linear for lighting, gamma-encode at the end.
- Never “fix” lighting by raising shininess until it looks Instagram.
---

**4. Layout (10 min).** Index: `(y * width + x) * 4`.  
No row padding in `ImageData`.  
Clear color should be **visible** (0.1 gray), never (0,0,0) while debugging a black cube.
---

---

## Common mistakes

1. Blending in uint8 without converting to 0–1.
2. Premultiplied and straight formulas mixed.
3. `clear` with alpha 0 then wondering why the page shows through.
4. Using `getContext('2d', { alpha: false })` and then debugging alpha.

## If we run long, cut

ICC / premultiplied GPU storage. Keep over + the sRGB name.

## If we run short, add

Coverage as cheap 50% alpha on an edge — name only.
