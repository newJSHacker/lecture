# Lecture 9 — Clip, NDC, viewport, depth buffer

**Week 9 of 15** · Computer Graphics I  
**Meeting:** 75 min lecture + 60 min live coding  
**Kernel:** ndc = clip.xyz/clip.w; viewport with y-flip; z-buffer compare documented; never near=0  
**Success check:** two overlapping triangles occlude correctly; disable depth shows painter’s-order bug; z as grayscale

This file is a **session guide** ([[Teaching/24 Session Guides]]). The 15-week markdown is the **course plan**, not this.

---

## Before you enter

- Quiz from Lecture 8 (10 min, paper or LMS).
- Demo: `Computer Graphics/code/09-scene-graph.html` (local, no CDN). If ES modules fail, `python -m http.server` in the course folder.
- Backup: the board photograph list below if the projector dies.
- Parked strip: `Lecture 9 | Goal: a correct 3D triangle rasterizer: transform, divide, viewport, depth | Invariant: a picture is an array; putPixel lives in pixels`

## Board at the end (they photograph this)

```
p_clip = P V M p
ndc = clip.xyz / clip.w          [−1,1] if inside

sx = (ndc.x*0.5+0.5)*width
sy = (1 − (ndc.y*0.5+0.5))*height    // canvas y down

z01 = ndc.z*0.5+0.5     pick 0-near or 1-near; match compare
if z < depth[i]: depth[i]=z; putPixel

drop triangle if any w ≤ eps     (full clipper not required)
```

## Slides today (cap: 6)

| # | What is on it | Why it is not the board |
| ---: | --- | --- |
| 1 | — | Most blocks have **no slide**. Argument on the board. |


---

## Lecture (75 min)

### Minutes 0–10 — Retrieve (quiz)

Hand out the Lecture 8 quiz. Mark one item together. Then:

**Say:** P is built. Today we divide, flip y because canvas grows down, and keep a second image called depth. A correct z-buffer on a plain canvas beats a pretty wrong cube.

**Ask:** Why flip y for Canvas? Wait. Want: NDC +Y vs canvas +Y down.

**Board:** parked strip. Then clip cube → square NDC → canvas, plus a y-flip.

**Slide:** none unless the table above has a photograph.

**They do:** write today’s question in their notes: *perspective divide, viewport, z-buffer rasterizer*.

**Do not:** Dividing before P (nonsense).

### Minutes 10–12 — Frame

**Say:** Clip volume −w≤x,y,z≤w. Straddle near → garbage divide; policy: drop if w≤eps or ndc out of range. Optional lerp-clip; no Sutherland–Hodgman. Affine z in NDC is acceptable if documented. Perspective-correct z is extra. Do not invent fps.

**Ask:** Who wins when two triangles overlap?

**Board:** today’s question in one line.

**Slide:** none.

**They do:** copy the parked invariant.

**Do not:** skip the attempt later to “cover more.”

### Minutes 12–35 — Build

**Say:** Divide after P, not before.

**Board:** clip cube → square NDC → canvas + y-flip. Z-buffer as a second image.

**Say:** Z-fighting: near too small, far too large, coplanar. Push near out. Polygon offset: name only.

**Ask:** Depth init value? Want: +∞ or 1.0 if using [0,1] far.

**They do:** On paper: y-flip formula, one picture. Why near=0.0001 is a bad idea.

**Do not:** Skip the attempt.

### Minutes 35–50 — Show

**Say:** Full cube, 12 triangles, PVM, divide, viewport, screen-space barycentric, z-buffer. Color=gray(z). Without depth, back faces scribble. Demo 12-zbuffer.html. Plant sy without flip then negating Ry forever. Plant clearing color but not depth.

**Slide:** none. Live editor or local demo. Zoom 140%.

**They do:** watch hands; then the same kernel on their machine when you say so.

**Do not:** type a 40-line starter you have not shown on the board. Do not hide the error.

### Minutes 50–65 — Attempt

**Say:** viewport(ndc,w,h) with a y-flip test. Eight minutes.

**They do:** alone or pairs, ~8 minutes. You do not help for the first 3 minutes.

**Board:** after they struggle, write one correct fragment.

**Do not:** live-code the attempt for them before they try.

### Minutes 65–75 — Land

**Say:** Lab: z-buffer cube; toggle depth; toggle z-visualize; a piercing triangle. Homework: init+compare documented. Quiz: NDC from clip, y-flip, depth init, who wins.

**Board:** add the invariant if it is not already in the parked strip.

**Do not:** “Any questions?” End on the lab hook.

---

## Live coding (60 min)

| Min | Beat | Plant / fix |
| ---: | --- | --- |
| 0–15 | Divide + print ndc | Plant dividing before P. |
| 15–40 | Viewport y-flip | Upside-down cube is this, not Ry. |
| 40–55 | Z-buffer two triangles | Disable depth = bug. |
| 55–60 | They paint z grayscale | Circulate. |

Point them at `Computer Graphics/code/09-scene-graph.html` as the after-class check, not as the lecture.

---

## Lab

1. `viewport(ndc, width, height)` with y-flip tests.
2. Z-buffer cube.
3. Keys: toggle depth, toggle z-visualize.
4. A second triangle piercing the cube; occlusion must be correct.

---

## Homework

1. Written: why `near = 0.0001` is a bad idea.
2. Code: init depth; compare documented.
3. Written: y-flip formula, one picture.

---

## Quiz next meeting (they hear this now)

1. NDC from clip? (2 pts)
2. Why flip y for Canvas? (2 pts)
3. Depth init value? (2 pts)
4. Two triangles overlap. Who wins? (4 pts)


## Extra exercises

See [[Computer Graphics/exercises/Week 09]].

---

## Notes you may still need (from the outline)

**1. Clip and near (15 min).** After `p_clip = P V M p`, the clip volume is (typical GL) −w ≤ x,y,z ≤ w.
If a triangle straddles the near plane, a naive divide produces garbage. **Course policy:** drop the triangle if any vertex has `w ≤ eps` or ndc out of range. Optional extra: lerp-clip against z=near. Full clipper is not required.
---

**2. NDC and viewport (15 min).** ```
ndc = clip.xyz / clip.w
```
NDC x,y,z in [−1,1] if inside the volume.
Canvas:
```
sx = (ndc.x * 0.5 + 0.5) * width
sy = (1 - (ndc.y * 0.5 + 0.5)) * height   // y-flip
```
Depth for the buffer: `z01 = ndc.z * 0.5 + 0.5` (0 near or 1 near — **pick one**, match compare).
---

**3. Z-buffer (20 min).** Array `depth[width*height]`, init to +∞ (or 1.0 if using [0,1] far).
For each pixel in the triangle:
```
z = interpolate (barycentric of clip-space z or ndc z)
if z < depth[i]:   // closer
    depth[i] = z
    putPixel(...)
```
**Perspective-correct z** is a later extra. Affine z in NDC is acceptable for the lab if documented.
Two overlapping triangles: the nearer color wins. Disable depth → painter’s order bug.
---

**4. Z-fighting (10 min).** Coplanar surfaces, or near too small and far too large: bits of z collapse. Fix: push near out, pull far in, add a polygon offset **name only**, or don’t stack two identical planes.
---

---

## Common mistakes

1. Dividing before P (nonsense).
2. Using clip.z as a pixel depth without mapping.
3. `sy` without flip: cube is upside-down, then they negate Ry forever.
4. Clearing color but not depth.

## If we run long, cut

Perspective-correct z. Keep divide + y-flip + z-buffer.

## If we run short, add

Culling as optional if depth is correct — Week 10.
