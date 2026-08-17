# Lecture 2 — Color, pixels, and the framebuffer

**Week 2 of 15** · Computer Graphics I  
**Time:** 75 min lecture + 60 min live coding  
**Kernel this week:** alpha over; sRGB vs linear as a **named** problem  
**Board first:** two overlapping squares, straight alpha vs premultiplied  
**Success check:** they can write the `over` formula and the byte index `(y * width + x) * 4`.


This file is a **session guide** ([[Teaching/24 Session Guides]]) plus the detailed notes. Run the 75 minutes as **moves** (Say / Ask / Board / Slide / They do). Detailed notes follow.

## Before you enter

- Demo: `Computer Graphics/code/02-checker.html` (local, no CDN). Serve the folder if ES modules fail.
- Backup: board first — two overlapping squares, straight alpha vs premultiplied.
- Parked strip: `Lecture 2 | Color, pixels, and the framebuffer | Invariant: a picture is an array; putPixel lives in pixels`
- Quiz from last lecture (except Lecture 1 / midterm / presentations).

## Board at the end (they photograph this)

```
two overlapping squares, straight alpha vs premultiplied
Two squares, over.
sRGB curve sketch (not to scale; labeled).
Letterbox vs stretch.
```

## Slides today (cap: 6)

Photograph, animation, or 20pt code only. If a slide has the argument in sentences, delete the sentences and write them on the board.

## How to run this meeting

Use the **Timing** or **Classroom moves** table below as the 75-minute spine. For each block: **Say** the question, **Board** the picture, **They do** a fragment, **Do not** skip the attempt. Then stand up for live coding (60 min).

## Classroom moves (75 min)

| Min | Phase | Say / board / slide / they do |
| ---: | --- | --- |
| 0–10 | Quiz | Lecture 1 quiz. Mark “six spaces” together. |
| 10–25 | Build | Pixel = sample. **Board:** grid. **Ask:** CSS size vs `canvas.width`? **Slide:** a circle stretched by CSS (photo). |
| 25–45 | Build | **Board:** `over` formula in 0–1. **They do:** compute one blend on paper (white 0.5 over black). |
| 45–60 | Show | **Slide:** 50% gray 128 vs a linear blend photograph. **Say:** policy weeks 2–10 vs 11–12. **Do not:** ICC profiles. |
| 60–75 | Land | **Board:** index formula. Clear color is visible gray. Lab: `over` two squares. |

**Slides today (cap: 3):** stretched circle; 128-gray vs perceptual mid; optional ImageData dump.

---

## Timing

| Minutes | Do this |
| ---: | --- |
| 0–10 | Quiz Week 1 |
| 10–25 | Pixel as sample; resolution; aspect |
| 25–45 | RGB, alpha, compositing |
| 45–60 | sRGB vs linear (picture, not a full color-science course) |
| 60–75 | Aspect ratio, letterbox, framebuffer layout |

---

## Learning goals

1. Explain resolution vs CSS size vs framebuffer size.
2. Composite with **over** (Porter–Duff) at teaching level.
3. Say why 8-bit sRGB averages look too dark or too bright.
4. Compute aspect ratio and why a circle becomes an ellipse.
5. State byte order in `ImageData` (RGBA, 0–255).

---

## 1. Pixels and samples (15 min)

A pixel in this course is a **sample of color** at a grid location. Treating it as a little square is fine for raster rules; it is not a physical CRT phosphor.

**Resolution:** number of samples.  
**Density:** samples per inch (mention, do not grade).  
**Aspect:** `width / height` of the **framebuffer**, not of the window unless they match.

If the canvas is stretched with CSS, circles become ellipses. Fix: match backing store to CSS * devicePixelRatio (cap at 2), or letterbox.

---

## 2. Color and alpha (20 min)

`ImageData`: four uint8s, **RGBA**, unpadded rows.

Alpha 255 = opaque. Alpha 0 = invisible. This week we blend.

**Over** (straight, teaching):

```
out_rgb = src_rgb * src_a + dst_rgb * (1 - src_a)
out_a   = src_a + dst_a * (1 - src_a)
```

Work in 0–1, then convert to bytes. Premultiplied alpha is what GPUs often store; mention it; implement straight over in the lab.

Coverage vs transparency: a rasterized edge is a form of coverage. We will not do MSAA this term. A 50% alpha edge is a cheap fake.

---

## 3. sRGB vs linear (15 min)

Displays apply a curve. PNG and Canvas are typically **sRGB**. Light adds in **linear** intensity.

Demo they must see: blend black and white 50/50 in byte space → 128. That is not perceptually halfway, and it is not physically halfway.

Course policy:

- Weeks 2–10: store 8-bit as-is; do not pretend it is physically correct.
- Weeks 11–12: convert to linear for lighting, gamma-encode at the end.
- Never “fix” lighting by raising shininess until it looks Instagram.

---

## 4. Layout (10 min)

Index: `(y * width + x) * 4`.  
No row padding in `ImageData`.  
Clear color should be **visible** (0.1 gray), never (0,0,0) while debugging a black cube.

---

## Live coding (60 min)

1. Two overlapping translucent rectangles, `over`.
2. Slider for source alpha.
3. Side-by-side: sRGB 50% gray vs a labeled “this is not linear 0.5.”
4. Letterbox helper: given window and framebuffer aspect, compute a centered viewport rectangle (used again in Week 9).

---

## Lab

1. `overPixel(img, x, y, rgba)`.
2. Draw 8 translucent circles (or boxes) in a row with alpha 1/8, 2/8, …
3. A “wrong CSS stretch” checkbox that sets CSS size ≠ backing store, and a caption.

Done when over of opaque red on blue is red, and over of alpha 0 does not change the destination.

---

## Homework

1. Implement `over` with tests: opaque, invisible, 50% red on black.
2. Written: one paragraph on sRGB vs linear. No need for the full 2.4 gamma formula; `pow(c, 2.2)` is enough.
3. Written: a 16:9 framebuffer in a 4:3 window. Do you stretch or letterbox? Why?

---

## Quiz (10 min)

1. `ImageData` index of pixel (2, 1) in a width-10 image? (2 pts)
2. Write `over` for rgb assuming a in [0,1], ignore output alpha. (4 pts)
3. Why does a CSS-stretched canvas distort a circle? (2 pts)
4. Is byte 128 half as much light as 255? Yes/no. (2 pts)

---

## Common mistakes

- Blending in uint8 without converting to 0–1.
- Premultiplied and straight formulas mixed.
- `clear` with alpha 0 then wondering why the page shows through.
- Using `getContext('2d', { alpha: false })` and then debugging alpha.

---

## Board drawings

1. Two squares, over.
2. sRGB curve sketch (not to scale; labeled).
3. Letterbox vs stretch.


## Extra exercises

See [[Computer Graphics/exercises/Week 02]].
